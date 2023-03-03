import pandas as pd
import requests
import pprint
import json
import csv
import glom


bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImlwYWFzLWNvbm5lY3RAdGR4LmNvbSIsInRkeF9lbnRpdHkiOiIyIiwidGR4X3BhcnRpdGlvbiI6IjUzIiwibmJmIjoxNjc3NzgwNzQ5LCJleHAiOjE2Nzc4NjcxNDksImlhdCI6MTY3Nzc4MDc0OSwiaXNzIjoiVEQiLCJhdWQiOiJodHRwczovL3d3dy50ZWFtZHluYW1peC5jb20vIn0.TvqMADaQwGpyW2d32N4GMDclm7suHbJl4v29hrChzFc'

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1136?withData=True&DataSortExpression=',
                        auth=BearerAuth(bearer))
with open('response1.json', 'wb') as outf:
    outf.write(response.content)


pprint.pprint(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1168?withData=True',
                        auth=BearerAuth(bearer))
with open('response2.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1116?withData=True',
                        auth=BearerAuth(bearer))
with open('response3.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1115?withData=True',
                        auth=BearerAuth(bearer))
with open('response4.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1137?withData=True',
                        auth=BearerAuth(bearer))
with open('response5.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1138?withData=True',
                        auth=BearerAuth(bearer))
with open('response6.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1167?withData=True',
                        auth=BearerAuth(bearer))
with open('response7.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1134?withData=True',
                        auth=BearerAuth(bearer))
with open('response8.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1162?withData=True',
                        auth=BearerAuth(bearer))
with open('response9.json', 'wb') as outf:
    outf.write(response.content)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1166?withData=True',
                        auth=BearerAuth(bearer))
with open('open14d.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1165?withData=True',
                        auth=BearerAuth(bearer))
with open('open7d.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1164?withData=True',
                        auth=BearerAuth(bearer))
with open('open3d.json', 'wb') as outf:
    outf.write(response.content)

print(response)

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1169?withData=True',
                        auth=BearerAuth(bearer))
with open('createtoclose.json', 'wb') as outf:
    outf.write(response.content)
print("done")

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1170?withData=True',
                        auth=BearerAuth(bearer))
with open('createtoclose2.json', 'wb') as outf:
    outf.write(response.content)
print("done")

response = requests.get('https://support.successacademies.org/TDWebApi/api/reports/1162?withData=True',
                        auth=BearerAuth(bearer))
with open('resolvedweek', 'wb') as outf:
    outf.write(response.content)