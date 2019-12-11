from http import HTTPStatus
from random import randint
import json
import pytest
import requests


@pytest.mark.parametrize('product', [('Xiaomi Redmi Note 8')])
def test_search_product(product):
    url = 'https://api.mercadolibre.com/sites/MLA/search?q={}'.format(product)
    r = requests.get(url)
    response = json.loads(r.content)
    total_productos = response['paging']['total']

    assert r.status_code == HTTPStatus.OK
    assert total_productos > 0
    assert len(response['results']) <= response['paging']['limit']

    random_num = randint(1, len(response['results']))
    random_item = response['results'][random_num]
    id = random_item['id']

    url = 'https://api.mercadolibre.com/items/{}'.format(id)
    r2 = requests.get(url)
    response2 = json.loads(r2.content)

    assert r.status_code == HTTPStatus.OK
    assert response2['title'] == random_item['title']
    assert response2['price'] == random_item['price']
    assert response2['currency_id'] == random_item['currency_id']
    assert response2['accepts_mercadopago'] == random_item['accepts_mercadopago']
    assert response2['shipping']['free_shipping'] == random_item['shipping']['free_shipping']
