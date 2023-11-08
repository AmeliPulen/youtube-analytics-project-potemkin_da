import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:


    def __init__(self, channel_id: str) -> None:
        """
        Инициализация экземпляра класса из данных, полученных по API
        """
        self.__channel_id = channel_id
        channel = youtube.channels().list(
            id=self.__channel_id,
            part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description'][:68]
        self.url = f"https://www.youtube.com/{channel['items'][0]['snippet']['customUrl']}"
        self.subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} {self.url}'


    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def print_info(self):
        """
        Выводит информацию о канале
        """
        print(f"Channel ID: {self.__channel_id}\n"
              f"Title: {self.title}\n"
              f"Description: {self.description}\n"
              f"Channel Link: {self.url}\n"
              f"Subscriber count: {self.subscriber_count}\n"
              f"Video count: {self.video_count}\n"
              f"View count: {self.view_count}")

    @property
    def channel_id(self):
        """
        Возвращает ID канала
        """
        return self.__channel_id


    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с Youtube API
        """
        return youtube

    def to_json(self, filename):
        """
        Сохраняет в файл значение атрибутов экземпляров Channel
        """
        with open(filename, 'w', encoding='utf-8') as file:
            data = {
                'Title': self.title,
                'Description': self.description,
                'Channel Link': self.url,
                'Subscriber count': self.subscriber_count,
                'Video count': self.video_count,
                'View count': self.view_count
            }
        json.dumps(data, indent=2, ensure_ascii=False)
