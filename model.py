import requests


def getImageUrlFrom(query):
    giphy_request_link = "https://api.giphy.com/v1/gifs/search?api_key=7BbMzq8ZT7aldPWWINWFUCtlZ1a7gVZq&q=dog&limit=25&offset=0&rating=g&lang=en"
    response = requests.get(giphy_request_link).json()
    return response["data"][0]["images"]["fixed_height"]["url"]

