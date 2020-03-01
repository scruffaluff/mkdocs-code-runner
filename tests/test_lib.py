"""Unit tests for library integration."""


import pathlib

import toml

import mkdocs_code_runner
from mkdocs_code_runner import lib


def test_findall() -> None:
    """Check that the JavaScript code is correctly found."""

    query = "div.code-runner"
    markdown = """
    <div class="code-runner">

    ```javascript
    let x = 3;
    console.log(x + 1);
    ```

    """

    expected = """
    let x = 3;
    console.log(x + 1);
    """.strip()

    actual = list(lib.findall(markdown, query))[0]
    assert actual == expected


def test_version() -> None:
    """Check that all the version tags are in sync."""

    pyproject_path = pathlib.Path(mkdocs_code_runner.__file__).parents[2] / "pyproject.toml"
    expected = toml.load(pyproject_path)["tool"]["poetry"]["version"]

    actual = mkdocs_code_runner.__version__
    assert actual == expected
