import requests
import configuration
import data
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)
# response = post_new_order();
# print(response.status_code)

# Запрос на получение заказа по номеру трека заказа.
def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
                        params={'t': track_number})
