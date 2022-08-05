import os
import pafy
import random as r
import time


yes = [
    'да',
    'продолжим',
    'ага',
    'конечно',
    'разумеется',
    'определенно'
    ]

no = [
    'нет',
    'неа',
    'не'
    ]

what = [
    'не понял',
    'что?',
    'Попробуй ещё раз',
    'я Вас не понимаю, попробуйте ещё раз'
    ]

# Получаем имя пользователя
login = os.getlogin()
# Ввести API Ключ Youtube data v3
pafy.set_api_key('API KEY')
# путь по умолчанию
default_path = f'C:\\Users\\{login}\\Videos\\youtube'


def get_all_urls(playlist_url):
    '''Функция принимает ссылку на url плейлиста и возвращает список url адресов каждого видео'''
    try:
        playlist = pafy.get_playlist2(playlist_url)
        return playlist
    except Exception as e:
        print(e)


def download_video_from_pl(urls, path):
    '''Функция принимает список от url адресов и путь к папке, после чего скачивает каждый файл'''
    idx = 1
    for url in urls:
        print(f'{idx} из {len(urls)}. {url.title}')
        try:
            best = url.getbest()
            best.download(filepath = path, quiet = False)
        except Exception as e:
            print(e)
        idx += 1

    

def create_path(folder_name):
    '''фунцкия принимает имя для папки, после чего создает её'''
    def create_subdir():
        new_dir = f'{default_path}\\{folder_name}'
        if os.path.exists(new_dir):
            pass
        else:
            os.mkdir(new_dir)
        return new_dir

    if os.path.exists(default_path):
        new_path = create_subdir()
    else:
        os.mkdir(default_path)
        new_path = create_subdir()      
    return new_path


def name_folder(playlist_url):
    '''функция принимает url плейлиста и предоставляет выбор назвать список также или переименовать'''
    try:
        pl_title = pafy.get_playlist2(playlist_url).title
        decision = input(f'{pl_title} - назвать папку так или переименовать?\n')
        if decision in yes:
            new_path = create_path(pl_title)
        elif decision in no:
            new_folder = input('Введи название новой папки:\n')
            new_path = create_path(new_folder)
        else:
            print(r.choice(what))
        return new_path
    except Exception as e:
        print(e)


def playlist_download():
    try:
        playlist_url = input('Введи URL плейлиста:\n')
        the_path = name_folder(playlist_url)
        urls = get_all_urls(playlist_url)
        print(f'Будет скачено {len(urls)} видеофайлов.')
        download_video_from_pl(urls, the_path)
    except Exception as e:
        print(e)


def video_download(url):
    try:
        video = pafy.new(url)
        best = video.getbest()
        best.download(filepath = default_path, quiet = False)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try: 
        while True:
            print('Загрузчик для Youtube на Python 3'
            '\nЧто желаете?')
            menu = input('1. Скачать Плейлист?'
            '\n2. Скачать только 1 видеофайл?'
            '\nВведи свой вариант:')
            if menu == '1':
                playlist_download()
                quit()
            elif menu == '2':
                url = input('Введи URL: ')
                video_download(url)
                quit()
            else:
                print('Выбери 1 или 2')
                time.sleep(2)
                os.system('cls')
    except KeyboardInterrupt:
        print('\nВыход из программы. Всего доброго!')
        quit()

