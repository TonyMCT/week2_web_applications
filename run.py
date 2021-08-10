#!/usr/bin/env python3
import os
import requests

mypath = "data/feedback"
for file in os.listdir(mypath):
 try:
    feedbackInfo = {}
    with open(mypath+"/"+file, "r") as f:
        listContent = f.readlines()
        feedbackInfo['title'] = listContent[0].strip()
        feedbackInfo['name'] = listContent[1].strip()
        feedbackInfo['date'] = listContent[2].strip()
        feedbackInfo['feedback'] = listContent[3].strip()
    print(feedbackInfo)
    response = requests.post("http://<corpweb-external-IP>/feedback", data=feedbackInfo)
    print(response.request.url)
    print(response.status_code)
 except OSError:
    pass