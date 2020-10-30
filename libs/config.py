
from os import environ
from dotenv import load_dotenv


from pathlib import Path
env_path = Path('.') / '.env'

if env_path:
    load_dotenv(dotenv_path=env_path)

REQUIRED_ENV_VARS = ["MONGO_URI_SOURCE", "MONGO_SOURCE_DATABASE", "MONGO_SOURCE_COLLECTION", "MONGO_URI_DESTINATION", "MONGO_DESTINATION_DATABASE", "MONGO_DESTINATION_COLLECTION"]

for var in REQUIRED_ENV_VARS:
    if var not in environ:
        raise EnvironmentError("Failed because {} is not set.".format(var))

DELETE_SOURCE = environ.get("DELETE_SOURCE", False)
MONGO_URI_SOURCE = environ["MONGO_URI_SOURCE"]
MONGO_SOURCE_DATABASE = environ["MONGO_SOURCE_DATABASE"]
MONGO_SOURCE_COLLECTION = environ["MONGO_SOURCE_COLLECTION"]

MONGO_URI_DESTINATION = environ["MONGO_URI_DESTINATION"]
MONGO_DESTINATION_DATABASE = environ["MONGO_DESTINATION_DATABASE"]
MONGO_DESTINATION_COLLECTION = environ["MONGO_DESTINATION_COLLECTION"]
