# meme-api

## 📃 Description
Simple meme API for sending memes to my friends when having a meme competition.


## API Reference

#### Get all meme links 

```
  GET /memes
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `N/A` | `null` | All available links to categorised memes that are subdivided based on Subreddit names. |

*Sample Response*
```json
{
    "meme_links": [
        "memes/HistoryMemes",
        "memes/memes",
        "memes/ProgrammerHumor"
    ]
}
```

#### Get a random meme

```
  GET /memes/{meme_category}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `meme_category`      | `string` | **Required**. Id of item to fetch |

*Sample Response*

<img width="100px" src="https://i.redd.it/9gxl4twutke51.jpg" />

## 👩‍💻 Stack
[![Stack](https://skillicons.dev/icons?i=python,fastapi&theme=dark)](https://skillicons.dev)
