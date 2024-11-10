import json
import os

from config import env_data
from requests import Session
from datetime import datetime


class CloudConnector:
    def __init__(self, cloud_dir: str = "YandexSynchronizer"):
        self.sep = "%2F"
        self.cloud_dir = cloud_dir
        self.user_disk_url = f"{env_data["USER_DISK_URL"]}{self.cloud_dir}"
        self.upload_file_url = (f"{env_data["UPLOAD_FILE_URL"]}{self.cloud_dir}{self.sep}"
                                + "{sync_file}&overwrite=true")
        self.HEADERS = {
            "Authorization": f"OAuth {env_data.get('OAuth_TOKEN')}",
            "Content-Type": "application/json",
        }
        self.upload_file_path = f"{env_data['LOCAL_DIR_PATH']}" + "/{file_name}"

    def get_files_data(self) -> dict[str, float]:
        with Session() as session:
            response = session.get(
                url=self.user_disk_url,
                headers=self.HEADERS,
            )
            data = json.loads(response.content)
            try:
                msg = data["message"]
                session.put(
                    url=self.user_disk_url,
                    headers=self.HEADERS,
                )
                return self.get_files_data()
            except KeyError:
                ...
            result_data = dict()
            for file in data.get("_embedded", {}).get("items", {}):
                result_data.update({file["name"]: datetime.fromisoformat(file["modified"]).timestamp()})
            return result_data

    def upload_file(self, file_path: str | None = None, filename: str | None = None):
        if filename:
            path = self.upload_file_path.format(file_name=filename)
        else:
            path = file_path

        with Session() as session:
            response = session.get(
                url=self.upload_file_url.format(sync_file=path.split("/")[-1]),
                headers=self.HEADERS,
            )
            try:
                href = json.loads(response.content).get("href")
            except KeyError:
                return
            with open(path, "r") as file:
                session.put(
                    url=href,
                    data=file,
                )

    def delete_file(self, filename: str):
        with Session() as session:
            response = session.delete(
                url=self.user_disk_url + self.sep + filename,
                headers=self.HEADERS,
            )


class LocalConnector:
    def __init__(self):
        self.sep = "/"
        self.dir_path = env_data["LOCAL_DIR_PATH"]

    def get_files_data(self) -> dict[str, float]:
        dir_files = os.listdir(self.dir_path)
        result_data = dict()
        for file in dir_files:
            new_path = self.dir_path + self.sep + file
            if not os.path.isfile(new_path):
                continue
            result_data.update({file: os.path.getmtime(new_path)})
        return result_data
