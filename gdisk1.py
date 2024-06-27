#Работы с файлами ответов из гугл диска
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gdrive = GoogleDrive(gauth)
#Чтение фала с гугл диска по id переданного из основного скрипта
def read_file(id_file):
    metadata = dict(id=id_file)
    google_file = gdrive.CreateFile(metadata=metadata)
    google_file.GetContentFile(filename=id_file)
    content_bytes = google_file.content  # BytesIO
    answer = content_bytes.read().decode('utf-8')
    #Проверка наличия временного файла скаченного с гугл диска
    #path = str('C:\\PyCharm\Projects\\team1_telebot1\\')
    path = str('C:\\Users\\skiner\\PyCharmProjects\\telebot1\\')
    file = str(path+id_file)
    if os.path.isfile(file):
        os.remove(file)
        print("временный файл удален")
    else:
        print("временный файл не найден")

    return answer

