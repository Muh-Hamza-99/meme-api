from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

import services

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Welcome to the Meme API!" }

@app.get("/memes")
def get_meme_links():
    meme_links = services.get_folder_links()
    return { "meme_links": meme_links }

@app.get("/memes/{meme_subreddit}")
def get_memes(meme_subreddit):
    image_path = services.select_random_image(meme_subreddit)
    return FileResponse(image_path)

# @app.post("/programmer-memes")
# def create_programmer_meme(image: UploadFile = File(...)):
#     file_path = services.upload_image("ProgrammerHumor", image)
#     if file_path is None:
#         return HTTPException(status_code=409, detail="Incorrect file type")
#     return FileResponse(file_path)