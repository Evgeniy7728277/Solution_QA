import requests
import json
import jsonpath
import response

# Link request
url = 'https://qfinterfaces.qnomy.com:10443/QfRougeQa/VLS_QVCP_63sp1_v3_1_0/api/Dynamic/BasicOperation'

# Read input Json file:
file = open("C:\\Users\\EvgeniyBelsky\\Desktop\\JSON\\baseOperation.json", "r")
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

headers = {
  'Content-Type': 'application/json',
  'Cookie': '_gcl_au=1.1.1517568310.1699302077; _ga=GA1.1.17692532.1699302077; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Nov+06+2023+22%3A21%3A17+GMT%2B0200+(Eastern+European+Standard+Time)&version=202310.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.qnomy.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; _lfa=LF1.1.ae52778d9315f30c.1697015140149; _hjSessionUser_3373565=eyJpZCI6ImQ3Njg2MmQ2LTA0M2YtNTE0Ni1hNjQ4LWE3ODk4MmYwMTIxNCIsImNyZWF0ZWQiOjE2OTkzMDIwNzg1OTksImV4aXN0aW5nIjpmYWxzZX0=; _ga_6VY256SCC2=GS1.1.1699302077.1.0.1699302078.59.0.0; cookiesname=CfDJ8Js9xqr7p%2FNNm8KEAGlW0nXv%2BH32XAwNh5dg4xbmZwhWdsPVfb6D4nE4U5yF8fHlAFjn9rhJ4I78U7yJ4i3cMavhYgPAAhAza%2B45PkGdak1Cc%2FjFKZJ9FCIcxQjFos5T2O8KjltzfBlq8jpQZm5nigwJOsOT8%2BKV2Sshg6Ua2IBc; qflowhybridvideo=CfDJ8Pr%2BvXjHNXxGtl0JtmakdkBF%2FwO2XVgB%2B3OdfoVW7skeFVLFHsoycJjAobTGcQT4Tq%2BDYYq7N8pRFfEBXYWCZRejYHxTcY4TxOfg5xq9ire8mzr%2FFFugbDy%2FvctUocOgLAyOq0Gj8wdoi21ZJnmEODBMsxtykZ1C5qvX%2BfNyqh4s; _dd_s=logs=1&id=295a5398-f501-4e7c-8a88-70e163e2509b&created=1700130189321&expire=1700131581596',
  'Accept': '*/*'
}

response = requests.request("POST", url, headers=headers, data=url)
print(response.request.body)



