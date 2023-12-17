import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body)

def get_order_by_track(track):
    order_parametr = data.order_parametr.copy()
    order_parametr["t"] = track
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,  # подставляем полный url
                        params=order_parametr)