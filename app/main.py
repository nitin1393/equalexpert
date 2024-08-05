from flask import Blueprint, jsonify
import requests
from app import cache
import logging

logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)

@main.route('/<username>')
@cache.cached(timeout=50)
def index(username):
    try:
        url = f"https://api.github.com/users/{username}/gists"
        logger.info(f"Request URL: {url}")
        payload = {}
        headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.info(f"Response: {response}")
        
        if response.status_code == 200:
            logger.info(f"Successful request for user: {username}")
            return jsonify(response.json())
        else:
            logger.error(f"Failed to retrieve data for user: {username}, Status Code: {response.status_code}")
            return jsonify({'error': 'Failed to retrieve data'}), response.status_code

    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception: {e}")
        return jsonify({'error': 'Request exception occurred'}), 500
