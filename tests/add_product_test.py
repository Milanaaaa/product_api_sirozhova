import requests
from data.api_root import api_root

# корректные данные
print(requests.post(api_root + 'product',
                    json={'scu': 15656239, 'name': 'телевизор', 'type': 'техника', 'cost': '800'}).json())

# нет типа
print(requests.post(api_root + 'product', json={'scu': 78996456, 'name': 'кружка', 'cost': '50'}).json())

# цена типа int
print(
    requests.post(api_root + 'product', json={'scu': 75161451, 'name': 'микроволновка', 'type': 'техника', 'cost': 300}).json())

# имя типа int
print(requests.post(api_root + 'product', json={'scu': 15981326, 'name': 123, 'type': 'посуда', 'cost': '50'}).json())
