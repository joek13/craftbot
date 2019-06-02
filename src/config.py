import toml
import logging
import os

EXAMPLE_CONFIG="""\"token\"=\"\" # the bot's token
\"command_prefix\"=\"++\" # the bot's prefix to use for commands (e.g. ++help)
\"server_ip\"=\"\" # the IP of the server to check status of
"""

def load_config(path="./config.toml"):
    """Loads the config from `path`"""
    if os.path.exists(path) and os.path.isfile(path):
        config = toml.load(path)
        return config
    else:
        with open(path, "w") as config:
            config.write(EXAMPLE_CONFIG)
            logging.warn(
                f"No config file found. Creating a default config file at {path}"
            )
        raise ValueError("Please fill in your config file.")
