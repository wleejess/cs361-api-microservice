import time, requests

weatherURL = 'http://api.weatherapi.com/v1/forecast.json?key=d50dc7dd12384f2a80f173407232907'

while True:
    time.sleep(1)
    with open("request.txt", "r+") as f:
        data = [line.rstrip() for line in f]
        f.truncate(0)
    
    if data and data[0] == "Weather API":
        zipcode = data[1]
        aqi = data[2]

        keyString = "&q=" + zipcode + "&days=1" + "&aqi=" + aqi + "&alerts=no"
        fullString = weatherURL + keyString
        print(fullString)
        response = requests.get(fullString)

        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
        else:
            q = open("response.txt", "w")
            q.write(response.text)
            q.close()
        data = None