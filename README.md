<h1>Синхронизатор файлов</h1>
Программу для синхронизации файлов на компьютере пользователя с Яндекс Диском. 
Программа отслеживает изменения файлов в указанной директории на компьютере 
и автоматически выполняет соответствующие действия на Яндекс Диске
при появлении, изменении или удалении файлов. 
<h2>Начало работы</h2>
Необходимо:
<br> 
<p>1) Установить зависимости</p>
<pre>
pip install -r requirements.txt
</pre>
<p>2) Создать файл .env</p>
<pre>
OAuth_TOKEN=y0_AgAAAAB6Abr7AAzAzAAAAAEX4zINAADeBmuv9a5EMb-hC4Y5dfKcTgoPkw
USER_DISK_URL=https://cloud-api.yandex.net/v1/disk/resources?path=
UPLOAD_FILE_URL=https://cloud-api.yandex.net/v1/disk/resources/upload?path=
LOCAL_DIR_PATH= Путь до директории
SYNC_DELAY= Задержка для повторной синхронизации
</pre>

После данных операций запустить файл main.py
<pre>
python src/main.py
</pre>