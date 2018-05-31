import json
import boto3
from jinja2 import Environment, FileSystemLoader


def cloudtrail(credentials):
    session = boto3.session.Session(**credentials)
    client = session.client('cloudtrail')
    return client.lookup_events()

def create_html(result):
    filename = "template.html"
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
    template = env.get_template(filename)
    html = template.render(result)
    return html

def get(credentials):
    """
    :type secrets: dict
    credentials = {
        "aws_access_key_id": "",
        "aws_secret_access_key": "",
        "region_name": "ap-northeast-1"
    }
    """
    result = cloudtrail(credentials)
    html = create_html(result)
    return html
