# Королева Ксения, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# Функция для номера трека нового заказа
def get_new_order_track():
    order_response = sender_stand_request.post_new_order(data.order_body)
    return order_response.json()["track"]

# Тест: Проверяем, что по треку заказа можно получить данные о заказе
def test_get_order_by_track_success_response():

    # В переменную new_order_track сохраняется трекер заказа
    new_order_track = get_new_order_track()

    # В переменную order_response сохраняется результат запроса на получения заказа по треку заказа
    order_response = sender_stand_request.get_order_by_track(new_order_track)

    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200