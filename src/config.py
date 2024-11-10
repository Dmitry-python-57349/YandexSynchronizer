import os.path
from os import getenv
from dotenv import load_dotenv, find_dotenv

ENV_FILE = ".env"
DEFAULT_SYNC_DELAY = 5

if not find_dotenv(ENV_FILE):
    exit(f"Can't find {ENV_FILE} file in project!")
load_dotenv()

env_data = {
    "OAuth_TOKEN": getenv("OAuth_TOKEN"),
    "USER_DISK_URL": getenv("USER_DISK_URL"),
    "UPLOAD_FILE_URL": getenv("UPLOAD_FILE_URL"),
}

local_dir = getenv("LOCAL_DIR_PATH")

if local_dir:
    if os.path.exists(local_dir):
        if os.path.isdir(local_dir):
            env_data["LOCAL_DIR_PATH"] = getenv("LOCAL_DIR_PATH")
        else:
            exit("По данному пути расположена не дериктория!")
    else:
        exit("Такой дериктории не существует!")
else:
    exit("Не указана локальная директория!")

try:
    env_data["SYNC_DELAY"] = int(getenv("SYNC_DELAY"))
except TypeError:
    env_data["SYNC_DELAY"] = DEFAULT_SYNC_DELAY
