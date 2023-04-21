
def api_plantilla_hello():
    return "Hello, api_plantilla!"


def get_helpers():
    return {
        "api_plantilla_hello": api_plantilla_hello,
    }
