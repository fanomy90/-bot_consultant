from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#Список файлов в корневом каталоге
#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#print(file_list)
#took = False
#for file1 in file_list:
#  print('title: %s, id: %s' % (file1['title'], file1['id']))


#Список файлов в папке title: TelBot1, id: 1kFTSpQ65BY64sDa9YE8P_u0Jk-tKqZAG
fileList = drive.ListFile({'q': "'1kFTSpQ65BY64sDa9YE8P_u0Jk-tKqZAG' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))




