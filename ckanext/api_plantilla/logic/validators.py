import ckan.plugins.toolkit as tk


def api_plantilla_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "api_plantilla_required": api_plantilla_required,
    }
