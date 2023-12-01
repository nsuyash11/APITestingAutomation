import json, jsonpath
import requests

url = "https://thetestingworldapi.com/api/studentsDetails"


def test_004_updateStudentDetailsById():
    file = open(
        "E:\\Testing\\Learning\\API\\pytest1\\Automated\\StudentsDetails\\studentDataUpdate.json"
    )
    file_content = file.read()
    req_body = json.loads(file_content)

    id = 9373729
    urlPathParam = "/" + str(id)
    full_url = url + urlPathParam

    res = requests.put(full_url, req_body)
    res_code = res.status_code
    res_body = res.json()

    res_msg = jsonpath.jsonpath(res_body, "msg")[0]

    print(res_code)
    print(res_body)

    assert res_code == 200
    assert res_msg == "update  data success"

    res2 = requests.get(full_url)
    res2_code = res2.status_code
    res2_body = res2.json()
    res2_first_name = jsonpath.jsonpath(res2_body, "data.first_name")[0]

    assert res2_first_name == "TochuNew"
