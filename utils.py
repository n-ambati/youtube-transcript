from urllib.parse import urlparse
import validators
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(video_url):
    valid_url = validators.url(video_url)

    if valid_url:
        parsed_url = urlparse(video_url)
        try:
            query = parsed_url.query.split('v=')[1]
            return query
        except IndexError:
            raise Exception("Invalid YouTube Url")


def extract_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript.sort(key=lambda x: x['text'])
    return transcript


def search_transcript(transcript, keyword):
    filtered_transcript = filter(lambda x: keyword.lower() in x['text'].lower(), transcript)
    filtered_transcript = list(filtered_transcript)
    filtered_transcript.sort(key=lambda x: x['start'])
    return filtered_transcript


def main():
    video_id = get_video_id('https://www.youtube.com/watch?v=zUUkiEllHG0')
    transcript = extract_transcript(video_id)
    print(search_transcript(transcript, 'valid'))


if __name__ == '__main__':
    main()
