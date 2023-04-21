"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.api_plantilla.logic import validators


def test_api_plantilla_reauired_with_valid_value():
    assert validators.api_plantilla_required("value") == "value"


def test_api_plantilla_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.api_plantilla_required(None)
