import os
from flask import Flask
from trail import get

app = Flask(__name__)

@app.route("/")
def get_root():
    credentials = {
        "aws_access_key_id": os.environ["aws_access_key_id"],
        "aws_secret_access_key": os.environ["aws_secret_access_key"],
        "region_name": "ap-northeast-1"
    }
    return get(credentials)

if __name__ == "__main__":
    app.run(host="0.0.0.0")