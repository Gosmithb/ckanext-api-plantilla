"""Tests for helpers.py."""

import ckanext.api_plantilla.helpers as helpers


def test_api_plantilla_hello():
    assert helpers.api_plantilla_hello() == "Hello, api_plantilla!"
