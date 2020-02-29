"""Unit tests for library integration."""


import pathlib

import toml

import mkdocs_code_runner


def test_version() -> None:
    """Check that all the version tags are in sync."""

    pyproject_path = pathlib.Path(mkdocs_code_runner.__file__).parents[2] / "pyproject.toml"
    expected = toml.load(pyproject_path)["tool"]["poetry"]["version"]

    actual = mkdocs_code_runner.__version__
    assert actual == expected
