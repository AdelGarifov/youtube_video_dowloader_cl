# Загрузчик видео с youtube cl

## Требования
1. Смотреть requirements.txt
2. Python 3.9.6
3. **!!! Для работы нужен ключ от youtube data v3**
https://developers.google.com/youtube/v3/getting-started

на 32й строке
```python
# Ввести API Ключ Youtube data v3
pafy.set_api_key('API KEY')
```

Работает с файловой системой Windows, под Unix систему не подойдёт.
Сохраняет в папку документ/youtube/название плейлиста

Два режима:
1. Скачать видео с плейлиста;
2. Скачать отдельное видео по ссылке

В следующей версии добавлю режим скачивания звуковыъ дорожек
Используется библиотека pafy

Сделал чисто по фану, может кому лень самому делать. Вот ловите)

> [!NOTE]
> Если какое-то видео не скачалось и выдало ошибку. Просто перезапустите скрипт и укажите ту же директорию. Он пройдется по всем видео и скачает только то, что не получилось. Ничего удалять не надо.