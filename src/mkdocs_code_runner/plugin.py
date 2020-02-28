"""Plugin for executing JavaScript code."""


import re
from typing import List

from mkdocs import plugins
from mkdocs.config import base
from mkdocs.structure import files, pages


class CodeRunner(plugins.BasePlugin):
    """Plugin for executing JavaScript code."""

    def on_page_markdown(
        self, markdown: str, page: pages.Page, config: base.Config, files: files.Files
    ) -> str:
        """Edit page copying JavaScript code into script element."""

        for match in findall(markdown):
            code = match.strip()
            script = f"\n<script>\n{code}\n</script>"
            markdown += script

        return markdown


def findall(markdown: str) -> List[str]:
    """Find all matching code blocks.

    Args:
        markdown: Text to parse.

    Return:
        Text from code blocks.
    """

    regex = re.compile(
        """
        <div\\s+class="code-runner">  # Match query element start
        \\s+```javascript\\s+         # Find JavaScript code block start
        (.*?)                         # Capture JavaScript code
        ```\\s+                       # Find JavaScript code block end
        </div>                        # Match query element end
        """,
        re.DOTALL | re.MULTILINE | re.VERBOSE,
    )

    return regex.findall(markdown)
