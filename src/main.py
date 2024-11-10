from time import sleep
from config import env_data
from sync_core import FileSynchronizer
from loguru import logger
from requests.exceptions import ConnectionError

if __name__ == "__main__":
    sync_engine = FileSynchronizer()
    try:
        while True:
            try:
                sync_engine.synchronize()
            except ConnectionError:
                logger.error("Соединение разорвано!")
            sleep(env_data["SYNC_DELAY"])
    except KeyboardInterrupt:
        exit("Stopped program!")
