"""Unit tests for library integration."""


import pathlib

import toml
import pytest

import mkdocs_code_runner
from mkdocs_code_runner import lib


def test_findall(markdown: str) -> None:
    """Check that the JavaScript code is correctly found."""

    query = "div.code-runner"

    expected = "let x = 3;" "\nconsole.log(x + 1);"

    actual = list(lib.findall(markdown, query))[0]
    assert actual == expected


def test_findall_empty(markdown: str) -> None:
    """Check that no JavaScript script code is found."""

    query = "div.mock-class"

    with pytest.raises(StopIteration):
        next(lib.findall(markdown, query))


def test_runner(markdown: str) -> None:
    """Check that the JavaScript code is correctly append to markdown."""

    query = "div.code-runner"

    expected = markdown + (
        "\n<script>"
        '\nwindow.addEventListener("load", () => {'
        "\nlet x = 3;"
        "\nconsole.log(x + 1);"
        "\n});"
        "\n</script>"
    )

    actual = lib.runner(markdown, query)
    assert actual == expected


def test_version() -> None:
    """Check that all the version tags are in sync."""

    pyproject_path = pathlib.Path(mkdocs_code_runner.__file__).parents[2] / "pyproject.toml"
    expected = toml.load(pyproject_path)["tool"]["poetry"]["version"]

    actual = mkdocs_code_runner.__version__
    assert actual == expected
