from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

def create_and_upload_file(file_name='test.txt', file_content='DUUUDE!'):
    try:
        drive = GoogleDrive(gauth)
        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(file_content)
        my_file.Upload()
        return f'File {file_name} was uploaded!'
    except Exception as _ex:
        return 'Got some trouble'
def main():
    print(create_and_upload_file(file_name='hello.txt', file_content='Hello'))

if __name__ == '__main__':
    main()
