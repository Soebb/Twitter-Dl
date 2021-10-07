from flask import Flask, request

from downlaoder import download_tweet

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "message": "Hello, World!"
    }


@app.route("/tweet/dl")
def tweet_dl():
    tweet_id = request.args.get("tweet_id")
    links = download_tweet(tweet_id)
    if links == 'Not Found':
        return {
            "status": 404,
            "message": "Not Found"
        }, 404
    elif links == 'Media Not Found':
        return {
            "status": 404,
            "message": "Media Not Found"
        }, 404
    else:
        return {
            "status": 200,
            "message": "Success",
            "links": links
        }, 200


app.run(
    debug=True,
)
