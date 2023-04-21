from flask import Blueprint


api_plantilla = Blueprint(
    "api_plantilla", __name__)


def page():
    return "Hello, api_plantilla!"


api_plantilla.add_url_rule(
    "/api_plantilla/page", view_func=page)


def get_blueprints():
    return [api_plantilla]
