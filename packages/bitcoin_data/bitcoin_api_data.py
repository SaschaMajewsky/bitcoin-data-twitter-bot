import requests


def get_btc_current_blockheight():
    response = requests.get('https://blockstream.info/api/blocks/tip/height')
    return response.json()
