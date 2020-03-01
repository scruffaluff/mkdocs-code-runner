"""Resuable testing fixtures for mkdocs-code-runner."""


import pathlib

import pytest


@pytest.fixture(scope="session")
def markdown() -> str:
    """Markdown text for testing.

    Return:
        Markdown text.
    """

    path = pathlib.Path(__file__).parent / "./data/sample.md"
    return path.read_text()
