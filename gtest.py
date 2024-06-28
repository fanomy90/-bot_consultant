from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
# Путь до JSON-файла с ключами
json_keyfile = '/home/projects/Bot_consultant/client_secrets.json'
# Аутентификация с использованием client_secrets.json и scope для Google Диска
gauth = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
gauth.credentials = credentials
# Создание объекта GoogleDrive
gdrive = GoogleDrive(gauth)
# Функция для получения списка файлов
def list_files():
    try:
        # Запрос на получение списка файлов без каких-либо фильтров
        file_list = gdrive.ListFile().GetList()
        if not file_list:
            print("На Google Диске нет доступных файлов.")
        else:
            print("Список файлов на Google Диске:")
            for file in file_list:
                print('Title: %s, ID: %s' % (file['title'], file['id']))
    except Exception as e:
        print("Произошла ошибка при получении списка файлов:", e)
# Вызов функции для получения списка файлов
list_files()
