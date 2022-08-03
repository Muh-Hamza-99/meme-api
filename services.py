from typing import List
import os
import random
from fastapi import UploadFile
import time

def get_image_filenames(folder_name: str) -> List[str]:
    return os.listdir(folder_name)

def select_random_image(folder_name: str) -> str:
    images = get_image_filenames(folder_name)
    random_image = random.choice(images)
    path = f"{folder_name}/{random_image}"
    return path

def get_folder_links() -> List[str]:
    development_folders = ["venv", "__pycache__"]
    folder_content = os.listdir("./")
    folders = [resource for resource in folder_content if ("." not in resource) and (resource not in development_folders) ]
    links = [f"memes/{folder}" for folder in folders]
    return links

# def is_image(filename: str) -> bool:
#     valid_extensions = (".png", ".jpg", ".jpeg", ".gif")
#     return filename.endswith(valid_extensions)

# def upload_image(folder_name: str, image: UploadFile):
#     if is_image(image.filename):
#         timestamp = time.strftime("%Y%m%d-%H%M%S")
#         image_name = timestamp + image.filename.replace(" ", "-")
#         with open(f"{folder_name}/{image_name}", "wb+") as image_file_upload:
#             image_file_upload.write(image.file.read())
#         return f"{folder_name}/{image_name}"
#     return None