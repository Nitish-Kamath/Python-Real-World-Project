# pip install requests->we can request data from website
# pip install win10toast->allow us to see notification in notification area

import requests
from win10toast import ToastNotifier
import json                                                       #->api that store data in json format
import time
def update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json() #convert data in json format
    text=f'Confirmed cases:{data["cases"]} \nDeaths:{data["deaths"]} \nRecovered:{data["recovered"]}'

    while True:
        toast=ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=20)   #Covid-19 Updates ->Title of  notification ;duration=20->duration of update notification in seconds
        time.sleep(60)                                          #notification interval 60 seconds(1 minute)
update()

