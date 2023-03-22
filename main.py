import os
import argparse
import services

from dotenv import load_dotenv
from requests.exceptions import HTTPError


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')

    return parser


def main():
    load_dotenv()
    api_token = os.environ.get('API_TOKEN')

    parser = create_arg_parser()
    namespace = parser.parse_args()

    url = namespace.url

    try:
        if not services.is_bitlink(api_token, url):
            print('Битлинк:', services.get_short_link(api_token, url))
        else:
            print('По вашей ссылке прошли:', services.count_clicks_for_short_link(api_token, url), 'раз(а)')
    except HTTPError as e:
        print(e.response.text)
        response_data = e.response.json()
        if response_data['message'] == 'MONTHLY_ENCODE_LIMIT_REACHED':
            print('Исчерпан месячный лимит создания коротких ссылок')
            return
        print('Не правильная ссылка. Пример: https://google.com или https://bit.ly/FgdGt')


if __name__ == '__main__':
    main()
