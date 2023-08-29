# cs361_microservice
A simple microservice used to connect to external APIs. There are two ways to use this: 1) Using the GUI made with Tkinter, or 2) Programmatically via text files.

------------------------------------------------------
### To use this microservice programmatically:
1. REQUEST data by writing to a "request.txt" file.<br>
  Use new lines for each parameter: API, zipcode, y/n air quality information.<br>
  Example:<br>
    Weather API<br>
    92122<br>
    no
2. RECEIVE data by reading from "response.txt" file.
  Currently contains a lot of information - recommend keys to access are:
    current, forecast, temp_c, temp_f.

------------------------------------------------------
### To use this microservice with the provided GUI (see apiLinkGUI.py)
1. Select an API from dropdown.
<img width="498" alt="image" src="https://github.com/wleejess/cs361_microservice/assets/29618012/20d2ae7a-da01-4fc3-8750-dc5dfd8ec0cc">

2. Based on API, additional fields will be displayed. User must fill out these fields 
as they are necessary query parameters.
<img width="493" alt="image" src="https://github.com/wleejess/cs361_microservice/assets/29618012/12a459d7-6194-4251-a013-1601725a8c85">

<img width="498" alt="image" src="https://github.com/wleejess/cs361_microservice/assets/29618012/392853cb-bb80-4521-aa17-9f1fdecd0810">

------------------------------------------------------
<img width="573" alt="Screenshot 2023-07-31 at 12 24 58 PM" src="https://github.com/wleejess/cs361_microservice/assets/29618012/8d93d704-3a1e-4ecc-b518-80339be00c08">

## General Notes

### Currently available APIs:
- Weather app <br>
parameters = location, days, air quality index.

- Dictionary api <br>
parameters = word
-----------------------------------------------------
### Responses:
Weather App response will be formatted as JSON.<br>
Keys to access: "current" > "temp_c" or "temp_f"
  "precip_mm", "precip_in", "feelslike_c", "feelslike_f", etc.

Dictionary App response will be formatted as JSON.<br>
Keys to access: "definition", "word"

