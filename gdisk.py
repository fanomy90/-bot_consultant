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
    try:
        # Получение файла по ID
        google_file = drive.CreateFile({'id': id_file})
        google_file.FetchMetadata()
        # Определение временного имени файла для скачивания
        filename = f"/tmp/{id_file}"
        # Проверка наличия ссылки на скачивание
        if 'downloadUrl' in google_file:
            google_file.GetContentFile(filename=filename)
            print(f"Файл {id_file} успешно скачан.")
        elif 'exportLinks' in google_file:
            export_link = google_file['exportLinks']['application/pdf']  # или другой доступный формат
            google_file.GetContentFile(filename=filename, mimetype='application/pdf')
            print(f"Файл {id_file} успешно экспортирован и скачан.")
        else:
            print("Файл не доступен для скачивания.")
            return None
        # Чтение содержимого файла
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        # Удаление временного файла
        if os.path.isfile(filename):
            os.remove(filename)
            print("Временный файл удален.")
        else:
            print("Временный файл не найден.")
        return content
    except Exception as e:
        print("Произошла ошибка при скачивании файла:", e)
        return None