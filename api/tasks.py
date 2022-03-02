import logging
# import schedule
# import time

from celery import shared_task
from main.settings import DEVELOPER_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, QUERY_TERM

# from celery.schedules import crontab
# from celery.decorators import periodic_task
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# # Periodic Task that runs every minute fetching videos from youtube data api and populating it in the APIVideos Table.
# @periodic_task(
#     run_every=(crontab(minute='*/1')),
#     name="search_youtube",
#     ignore_result=True)

@shared_task
def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY, cache_discovery=False)

    search_response = youtube.search().list(
        q=QUERY_TERM,
        part='id,snippet',
        type='video',
        order='date',
        maxResults=10,
        publishedAfter='2022-02-28T11:37:41.228849Z',
    ).execute()

    return search_response

# schedule.every(10).seconds.do(youtube_search)
# while True:
#     schedule.run_pending()
#     time.sleep(1)