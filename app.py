from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

course = {
    "Backend": "Backend",
    "Frontend": "Frontend",
    "Mobile" : "Mobile",
    "Marketing": "Marketing"
}

def get_accurate_time():
    utc_now = datetime.now(pytz.utc)
    utc_time = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    return utc_time

@app.route('/api', methods=['GET'])
def get_course():
    """get the second argument
    """
    track = request.args.get('track')
    slack_name = request.args.get('slack_name')
    
    course_track = course.get(track)
    if not course_track:
        return jsonify({"error": "The track doesn't exist"}), 400
    
    current_day = datetime.now().strftime("%A")

    utc_time = get_accurate_time()

    github_repo = "https://github.com/jaredatandi/HNG-api"
    github_file = "https://github.com/jaredatandi/HNG-api"

    