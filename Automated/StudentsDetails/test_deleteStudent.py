import requests, jsonpath

url = "https://thetestingworldapi.com/api/studentsDetails"


def test_005_deleteStudentById():
    id = 9373726
    urlPathParam = "/" + str(id)
    full_url = url + urlPathParam

    res = requests.delete(full_url)
    res_code = res.status_code
    res_body = res.json()

    print(res_code)
    print(res_body)

    res_msg = jsonpath.jsonpath(res_body, "msg")[0]
    assert res_msg == "Delete  data success"

    res2 = requests.get(full_url)
    res2_code = res2.status_code
    res2_body = res2.json()

    res2_msg = jsonpath.jsonpath(res2_body, "msg")[0]
    assert res2_msg == "No data Found"
