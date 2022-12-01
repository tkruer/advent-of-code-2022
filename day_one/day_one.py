import requests


def getdata():
    response = requests.get("https://adventofcode.com/2022/day/1/input")
    with open("input.txt", "w") as f:
        f.write(response.text)
    return f'{response.status_code} - File written to day_one/day_one_data.txt'


getdata()

