from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gdrive = GoogleDrive(gauth)

def read_file(id_file):
    metadata = dict(id=id_file)

    google_file = gdrive.CreateFile(metadata=metadata)

    google_file.GetContentFile(filename=id_file)

    content_bytes = google_file.content;  # BytesIO

    string_data = content_bytes.read().decode('utf-8')
    path = str('C:\\PyCharm\Projects\\team1_telebot1\\')
    file = str(path+id_file)
    if os.path.isfile(file):
        os.remove(file)
        print("success")
    else:
        print("File doesn't exists!")

    return string_data


if __name__ == '__main__':
    gdrive = GoogleDrive(gauth)

    ID_FILE = '1HPyjS65Zs59cplr2kVkuaxNXjzCrKlBK'

    string_data = read_file(id_file=ID_FILE)

    print(string_data)

