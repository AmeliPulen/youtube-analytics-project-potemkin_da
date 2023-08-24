import json
import os

from googleapiclient.discovery import build


class Channel:
    def __init__ (self, channel_id: str) -> None:
        self.channel_id = channel_id

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # получаем данные о канале по его id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


        def print_info(dict_to_print: dict) -> None:
            """Выводит словарь в json-подобном удобном формате с отступами"""
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


        print_info(channel)

