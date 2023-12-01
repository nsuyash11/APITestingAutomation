import requests, jsonpath

token_url = "http://thetestingworldapi.com/token"

api_url = "http://thetestingworldapi.com/api/stdetails"


def test_getAccessToken():
    data = {"grant_type": "password", "username": "admin", "password": "adminpass"}

    res = requests.post(token_url, data)

    global access_token
    access_token = jsonpath.jsonpath(res.json(), "access_token")[0]
    assert access_token != None


def test_oauthAPI():
    # access_token = "100abc"
    header = {"Authorization": "Bearer " + access_token}

    id = 1104
    api_full_url = api_url + "/" + str(id)
    res = requests.get(api_full_url, header)
    res_code = res.status_code
    res_body = res.json()

    print(res_code)
    print(res_body)

    assert res_code == 200
