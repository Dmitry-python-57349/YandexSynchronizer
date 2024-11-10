from models import CloudConnector, LocalConnector
from loguru import logger


class FileSynchronizer:
    def __init__(self, cloud_dir: str | None = None):
        self.cloud: CloudConnector = CloudConnector(cloud_dir=cloud_dir) if cloud_dir else CloudConnector()
        self.local: LocalConnector = LocalConnector()

    def synchronize(self):
        cloud_files = self.cloud.get_files_data()
        local_files = self.local.get_files_data()

        for cloud_file in cloud_files:
            if cloud_file not in local_files:
                self.cloud.delete_file(filename=cloud_file)
                logger.info(f"Файл {cloud_file} удален с облачного хранилища!")
                continue
            if local_files[cloud_file] > cloud_files[cloud_file]:
                self.cloud.upload_file(filename=cloud_file)
                logger.info(f"Файл {cloud_file} успешно перезаписан!")

        for local_file in local_files:
            if local_file not in cloud_files:
                self.cloud.upload_file(filename=local_file)
                logger.info(f"Файл {local_file} добавлен в облачное хранилище!")

        logger.info("Синхрогизация проведена успешно!")
