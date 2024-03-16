# Ольга Сушко, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import sending_requests
def get_trask_number_of_order():
    track_number = sending_requests.post_new_order()  # сохраняем ответ, при создании нового заказа.
    return track_number.json()["track"]               # сохраняем полученный трек

def test_create_and_track_order():
    track_number = get_trask_number_of_order()
    get_response = sending_requests.get_order_info(track_number)    # сохранияем результат запроса на получение инфы по треку
    assert get_response.status_code == 200                          # проверка, что код ответа 200

