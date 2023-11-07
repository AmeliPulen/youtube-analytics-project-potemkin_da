import os

from googleapiclient.discovery import build


class Video():

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        """
        Инициализировать экземпляр класса на основании введенного ID видео
        """
        self.video_id = video_id
        """
        Создать экземпляр класса на основании данных полученных из запроса
        """
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']


    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):

    def __init__(self, vid_id, playlist_id):
        super().__init__(vid_id)
        self.playlist_id = playlist_id


