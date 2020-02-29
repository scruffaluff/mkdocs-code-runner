"""Plugin for executing JavaScript code."""


import re
from typing import Iterator

import bs4
from mkdocs import plugins
from mkdocs.config import base, config_options
from mkdocs.structure import files, pages


class CodeRunner(plugins.BasePlugin):
    """Plugin for executing JavaScript code."""

    config_scheme = (("query", config_options.Type(str, default="div.code-runner")),)

    def on_page_markdown(
        self, markdown: str, page: pages.Page, config: base.Config, files: files.Files
    ) -> str:
        """Edit page copying JavaScript code into script element."""

        element = "\n<script>\n{}\n</script>"
        listener = 'window.addEventListener("load", () => {{\n{}\n}});'
        script = element.format(listener)

        for code in findall(markdown, self.config["query"]):
            markdown += script.format(code)

        return markdown


def findall(markdown: str, query: str) -> Iterator[str]:
    """Find all matching code blocks.

    Args:
        markdown: Text to parse.

    Return:
        Text from code blocks.
    """

    regex = re.compile(
        """
        \\s+```javascript\\s+         # Find JavaScript code block start
        (.*?)                         # Capture JavaScript code
        \\s+```\\s+                       # Find JavaScript code block end
        """,
        re.DOTALL | re.MULTILINE | re.VERBOSE,
    )

    soup = bs4.BeautifulSoup(markdown, "html.parser")
    for match in soup.select(query):
        yield from regex.findall(match.text)
