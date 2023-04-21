import ckan.plugins.toolkit as tk
import ckanext.api_plantilla.logic.schema as schema


@tk.side_effect_free
def api_plantilla_get_sum(context, data_dict):
    tk.check_access(
        "api_plantilla_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.api_plantilla_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'api_plantilla_get_sum': api_plantilla_get_sum,
    }
