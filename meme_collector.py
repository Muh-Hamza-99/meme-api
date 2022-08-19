import os
import dotenv 
import praw
import urllib.parse as parse
import requests
import shutil

dotenv.load_dotenv()

def create_reddit_client():
    client = praw.Reddit(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        user_agent=os.environ["USER_AGENT"],
    )
    return client

def is_image(post):
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False

def get_image_urls(client: praw.Reddit, subreddit_name: str, limit: int):
    hot_memes = client.subreddit(subreddit_name).hot(limit=limit)
    image_urls = []
    for post in hot_memes:
        if is_image(post):
            image_urls.append(post.url)
    return image_urls

def get_image_name(image_url: str) -> str:
    image_name = parse.urlparse(image_url)
    return os.path.basename(image_name.path)

def create_folder(folder_name: str):
    try:
        os.mkdir(folder_name)
    except OSError:
        print(f"Added to existing folder: {folder_name}!")
    else:
        print(f"{folder_name} created!")

def download_image(folder_name: str, raw_response, image_name: str):
    create_folder(folder_name)
    with open(f"{folder_name}/{image_name}", "wb") as image_file:
        shutil.copyfileobj(raw_response, image_file)


def collect_memes(subreddit_name: str, limit: int=20):
    client = create_reddit_client()
    image_urls = get_image_urls(client=client, subreddit_name=subreddit_name, limit=limit)
    for image_url in image_urls:
        image_name = get_image_name(image_url)
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True
            download_image(subreddit_name, response.raw, image_name)
 
if __name__ == "__main__":
    collect_memes(subreddit_name="HistoryMemes")
