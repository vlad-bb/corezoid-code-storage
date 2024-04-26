import requests


URL = 'https://heureka-hajus-ai-tools.koyeb.app/api/1/products/availability?products[0][id]=ABC123&products[0][count]=1'


def handle(data):
    response = requests.get(url=URL)

    data["res"] = {
        "code": response.status_code,
        "body": response.json(),
    }

    return data
