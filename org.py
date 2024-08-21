#!/bin/python3
import os
import platform

# make it so that it can be ran anywhere in the system and still
# find the downloads folders
# should be cross platform

class Organizer:
    files = []
    folders = ['imgs', 'pdfs', 'videos', 'archives', 'exes', 'else', 'docs', 'excel', 'powerpoint']
    imgs = ['.jpg','.jpeg','.png','.gif',
            '.bmp','.tiff','.tif','.svg',
            '.webp','.ico','.heic','.heif',
            '.raw','.psd','.ai',]
    videos = ['.mp4','.avi','.mov','.mkv',
              '.flv','.wmv','.webm','.mpeg',
              '.mpg','.rm','.mts','.ts',
              '.3gp','.ogv',]
    archives = ['.zip','.rar','.tar','.gz',
                '.7z','.bz2','.xz','.iso',
                '.cab','.arj','.lzh','.z',
                '.ace','.pak',]
    exes = ['.exe','.bat','.sh','.cmd',
            '.bin','.app','.msi','.pkg',
            '.out','.jar','.run',]
    word_docs = ['.doc','.docx','.dot','.dotx',
                 '.docm','.dotm','.odt',]
    excel = ['.xls','.xlsx','.xlsm','.xlsb',
             '.xlt','.xltx','.xltm','.ods',]
    powerpoint = ['.ppt','.pptx','.pptm','.pot',
                  '.potx','.potm','.pps','.ppsx',
                  '.ppsm',]

    def __init__(self):
        try:
            self.files = os.listdir()
        except:
            print("Can't find Downloads folder")
            exit()
        for i in self.folders:
            self.checkDirExist(i, self.files)

        for i in self.files:
            self.checkFileType(i)


    def checkDirExist(self, i: str, files: list) -> None:
        if i not in files:
            os.mkdir(i)

    def checkFileType(self, i: str) -> None:
        if i in self.folders:
            return
        try:
            extension = i.split('.')[-1] 
        except Exception as e:
            print(e)
            return

        extension = f'.{extension}'
        if extension in self.imgs:
            os.rename(f'./{i}', f'./imgs/{i}')
        elif extension in self.videos:
            os.rename(f'./{i}', f'./videos/{i}')
        elif extension == '.pdf':
            os.rename(f'./{i}', f'./pdfs/{i}')
        elif extension in self.archives:
            os.rename(f'./{i}', f'./archives/{i}')
        elif extension in self.exes:
            os.rename(f'./{i}', f'./exes/{i}')
        elif extension in self.word_docs:
            os.rename(f'./{i}', f'./docs/{i}')
        elif extension in self.excel:
            os.rename(f'./{i}', f'./excel/{i}')
        elif extension in self.powerpoint:
            os.rename(f'./{i}', f'./powerpoint/{i}')
        else:
            os.rename(f'./{i}', f'./else/{i}')

if __name__ == '__main__':
    Organizer()
