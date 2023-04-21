"""Tests for views.py."""

import pytest

import ckanext.api_plantilla.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "api_plantilla")
@pytest.mark.usefixtures("with_plugins")
def test_api_plantilla_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("api_plantilla.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, api_plantilla!"
