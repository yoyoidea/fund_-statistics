import requests

url = "https://api.doctorxiong.club/v1/fund/position"
code = "001714"
params = {"code": code}
res = requests.get(url=url, params=params)
print(res.json())
