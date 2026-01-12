import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"
USER_ID = 1

# Вспомогательная функция для проверки структуры пользователя
def assert_user_structure(data, check_id=None):
    # Обязательные поля верхнего уровня
    required_keys = {'id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'}
    assert set(data.keys()) >= required_keys, f"Missing keys in response: {required_keys - set(data.keys())}"

    # Проверка address
    address = data['address']
    address_keys = {'street', 'suite', 'city', 'zipcode', 'geo'}
    assert set(address.keys()) >= address_keys, f"Missing address keys: {address_keys - set(address.keys())}"

    # Проверка geo
    geo = address['geo']
    geo_keys = {'lat', 'lng'}
    assert set(geo.keys()) >= geo_keys, f"Missing geo keys: {geo_keys - set(geo.keys())}"

    # Проверка company
    company = data['company']
    company_keys = {'name', 'catchPhrase', 'bs'}
    assert set(company.keys()) >= company_keys, f"Missing company keys: {company_keys - set(company.keys())}"

    # Проверка типов и значений
    assert isinstance(data['id'], int), "id must be an integer"
    assert isinstance(data['name'], str) and data['name'], "name must be a non-empty string"
    assert '@' in data['email'], "email must contain '@'"

    if check_id is not None:
        assert data['id'] == check_id, f"Expected id={check_id}, got {data['id']}"


# 1. GET — получить пользователя
def test_get_user():
    response = requests.get(f"{BASE_URL}/users/{USER_ID}")
    
    # Проверка статуса
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    
    # Проверка структуры
    assert_user_structure(data, check_id=USER_ID)
    
    # Дополнительная проверка данных
    assert data['id'] == USER_ID
    assert '@' in data['email']


# 2. POST — создать пользователя
def test_post_user():
    new_user = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }

    response = requests.post(f"{BASE_URL}/users", json=new_user)
    
    # Проверка статуса
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    data = response.json()
    
    # Проверка структуры
    assert_user_structure(data)
    
    # Проверка значений
    assert data['name'] == "Test User"
    assert data['email'] == "test@example.com"


# 3. PUT — обновить пользователя
def test_put_user():
    updated_user = {
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@example.com",
        "address": {
            "street": "Updated Street",
            "suite": "Apt. 100",
            "city": "New City",
            "zipcode": "12345-6789",
            "geo": {
                "lat": "0.0000",
                "lng": "0.0000"
            }
        },
        "phone": "000-000-0000",
        "website": "updated.org",
        "company": {
            "name": "Updated Co",
            "catchPhrase": "Updated catchphrase",
            "bs": "updated bs"
        }
    }

    response = requests.put(f"{BASE_URL}/users/{USER_ID}", json=updated_user)
    
    # Проверка статуса
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    
    # Проверка структуры
    assert_user_structure(data, check_id=USER_ID)
    
    # Проверка обновлённых значений
    assert data['name'] == "Updated User"
    assert data['email'] == "updated@example.com"