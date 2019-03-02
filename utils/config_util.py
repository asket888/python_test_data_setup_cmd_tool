import json


def get_env(env):
    if env.upper() == "DEV":
        return _read_config("config.json", "DEV")
    elif env.upper() == "UAT":
        return _read_config("config.json", "UAT")
    elif env.upper() == "LOCALHOST":
        return _read_config("config.json", "LOCALHOST")
    else:
        raise TypeError("Unexpected environment value")
    

def _read_config(file, tag):
    with open(file) as json_file:
        as_dict = json.load(json_file)[tag]
        return as_dict
