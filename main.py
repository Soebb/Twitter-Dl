from flask import Flask, request, jsonify
from pdb import set_trace

from downlaoder import download_tweet

app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(error):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return {
        'error': str(error),
    }

@app.route("/")
def index():
    return {
        "message": "Hello, World!"
    }


@app.route("/tweet/dl")
def tweet_dl():
    tweet_id = request.args.get("tweet_id")
    if type(tweet_id) is type(None):
        return {
            "error": "No tweet_id provided"
        }, 400
    
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
