import json, jsonpath
import requests
import test_getStudentDetails

url = "https://thetestingworldapi.com/api/studentsDetails"


def test_003_createStudent():
    file = open(
        "E:\\Testing\\Learning\\API\\pytest1\\Automated\\StudentsDetails\\studentDataNew.json",
        "r",
    )
    file_content = file.read()
    req_body = json.loads(file_content)

    res = requests.post(url, data=req_body)
    res_code = res.status_code
    res_body = res.json()

    print(res_code)
    print(res_body)
    assert res_code == 201

    id = jsonpath.jsonpath(res_body, "id")[0]

    res2 = requests.get(url + "/" + str(id))
    res2_code = res2.status_code
    res2_body = res2.json()

    res2_id = jsonpath.jsonpath(res2_body, "data.id")[0]

    print(res2_code)
    print(res2_body)

    assert res2_id == id
