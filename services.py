import requests

from urllib.parse import urlparse


def get_short_link(api_token: str, long_url: str) -> str:
    bitly_api_url = 'https://api-ssl.bitly.com/v4/bitlinks'

    headers = {
        'Authorization': f'Bearer {api_token}'
    }

    payload = {
        'long_url': long_url
    }

    response = requests.post(bitly_api_url, headers=headers, json=payload)
    response.raise_for_status()

    response_data = response.json()
    return response_data['link']


def count_clicks_for_short_link(api_token: str, short_url: str) -> int:
    headers = {
        'Authorization': f'Bearer {api_token}'
    }

    parsed = urlparse(short_url)
    bitly_id = parsed.netloc + parsed.path

    bitly_api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitly_id}/clicks/summary'
    response = requests.get(bitly_api_url, headers=headers)
    response.raise_for_status()

    response_data = response.json()
    return response_data['total_clicks']


def is_bitlink(api_token: str, url: str) -> bool:
    headers = {
        'Authorization': f'Bearer {api_token}'
    }

    parsed = urlparse(url)
    bitly_id = parsed.netloc + parsed.path

    bitly_api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitly_id}'
    response = requests.get(bitly_api_url, headers=headers)

    return response.ok
