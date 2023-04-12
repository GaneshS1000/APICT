import pytest

from utils.apiutils import getAPIData, postAPIData
from utils.myconfigparser import getPetAPIURL

baseURI = getPetAPIURL()
petID = '198'

@pytest.fixture
def add_pet():
    url = baseURI
    payload = {"id": int(petID), "name": "Cutie", "status": "pending"}
    resp = postAPIData(url, payload)
    pet_ID = resp.json()['id']
    print(pet_ID)
    yield pet_ID

def test_getPetByID(add_pet):
    url = baseURI + str(add_pet)
    headers = {'Content-Type': 'application/json'}
    print("RequestURL: " + url)
    resp = getAPIData(url, headers)
    assert resp.json()
    print(resp.json())
    assert resp.status_code == 200