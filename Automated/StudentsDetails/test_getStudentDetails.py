import requests

url = "https://thetestingworldapi.com/api/studentsDetails"


def test_001_getStudentsDetails():
    urlPathParam = ""
    full_url = url + urlPathParam

    res = requests.get(full_url)
    res_body = res.json()
    res_code = res.status_code

    print(res_code)
    print(res_body)
    assert res_code == 200


def test_002_getStudentDetailsById():
    id = 9373704
    urlPathParam = "/" + str(id)
    full_url = url + urlPathParam

    res = requests.get(full_url)
    res_body = res.json()
    res_code = res.status_code

    print(res_code)
    print(res_body)
    assert res_code == 200
