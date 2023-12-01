import requests, jsonpath
from DataDriven.Utilities import ReadXL


def test_createStudents():
    url = "https://thetestingworldapi.com/api/studentsDetails"

    xlObj = ReadXL.ReadXLClass(
        "E:\\Testing\\Learning\\API\\pytest1\\Automated\\DataDriven\\Resources\\test_data.xlsx",
        "Sheet1",
    )
    rows = xlObj.row_count

    # capturing excel data row by row, converting it to json_req_body and sending to POST
    for i in range(2, rows + 1):
        req_body = xlObj.fetch_record_json(i)

        print(req_body)

        res = requests.post(url, data=req_body)
        print(res.status_code)
        print(res.json())

        assert res.status_code == 201
