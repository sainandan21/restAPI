#Imported pytest for testing purpose
import pytest
#Created one end point using flask (for manual testing purpose)
from main import main
#Imported requests to deal with the HTTP methods and also to print the status code of the response
import requests

#fixture is like a prerequist for the other function. we can envoke this fixture function
# in other fuction calling.
@pytest.fixture
def client():
    # test client means a client is requesting the data same like user.
    with main.test_client() as client:
        yield client

#Manula Testing
@pytest.mark.parametrize("endpoint",["/restapi"])
def test_api_endpoint(client,endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200
    print("Status Code:", response.status_code)
    print()
    #assert response.data.decode('utf-8') == "Hello"

#Automation testing
# we can keep any public API inside the mark parameter.
@pytest.mark.parametrize("api_endpoint", [
    # "https://jsonplaceholder.typicode.com/posts/1"
    "https://api.publicapis.org/entries"
    # Add more API endpoints to test
])
#This function will check whether the given API sends any response code.
# and also it compares the response code
def test_public_api(api_endpoint):
    response = requests.get(api_endpoint)
    assert response.status_code == 200
    print("Status Code:", response.status_code)

if __name__ == '__main__':
    pytest.main()
