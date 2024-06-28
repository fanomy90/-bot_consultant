#Работы с файлами ответов из гугл диска
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os

# Путь до JSON-файла с ключами
json_keyfile = '/home/projects/Bot_consultant/client_secrets.json'
# Аутентификация с использованием client_secrets.json
gauth = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
gauth.credentials = credentials
# gauth.LocalWebserverAuth()
# Создание объекта GoogleDrive
drive = GoogleDrive(gauth)
# Чтение файла с Google Drive по id
def read_file(id_file):
    metadata = {'id': id_file}
    google_file = drive.CreateFile(metadata=metadata)
    google_file.GetContentFile(filename=id_file)
    content_bytes = google_file.content  # BytesIO
    answer = content_bytes.read().decode('utf-8')

    # Проверка и удаление временного файла
    path = '/home/projects/Bot_consultant/tmp/'
    file_path = os.path.join(path, id_file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("Временный файл удален")
    else:
        print("Временный файл не найден")

    return answer