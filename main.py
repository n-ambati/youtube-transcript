from flask import Flask, request, jsonify
from flask_cors import CORS
# from werkzeug.exceptions import BadRequestKeyError

import utils


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/transcript', methods=['GET'])
def get_transcript():
    if 'vid' in request.args:
        video_id = request.args['vid']
        try:
            transcript = utils.extract_transcript(video_id)
            return jsonify(transcript)
        except Exception as e:
            return jsonify(
                [
                    {'Error': str(e)}
                ]
            )

    if 'url' in request.args:
        video_url = request.args['url']
        try:
            video_id = utils.get_video_id(video_url)
            transcript = utils.extract_transcript(video_id)
            return jsonify(transcript)
        except Exception as e:
            return jsonify(
                [
                    {'Error': str(e)}
                ]
            )

    return jsonify([{'Error': 'Bad Request'}])
