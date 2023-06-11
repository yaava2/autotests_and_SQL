# Валентина Куракина, 5-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import requests

URL_SERVICE = "https://dd30979c-5aa9-4029-9a4e-b26d078cfc97.serverhub.praktikum-services.ru"
USERS_ORD = "/api/v1/orders/track"
CREATE_ORD = "/api/v1/orders"

def post_new_order(body):
    return requests.post(URL_SERVICE + CREATE_ORD,
                         json=body,
                         headers=data.headers)

def get_order_by_track(track_ord):
    return requests.get(URL_SERVICE + USERS_ORD,
                        params={"t": track_ord})

# Тест 1. Успешное получение заказа по треку
def test_get_order_by_track():
    # создание заказа
    response = post_new_order(data.order)
    track_ord = response.json().get("track")

    # получение заказа по треку
    response = get_order_by_track(track_ord)

    # проверка
    assert response.status_code == 200

