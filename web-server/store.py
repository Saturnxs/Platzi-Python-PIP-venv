import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    categories = r.json()
    print(categories)
    for category in categories:
        print(category['name'])