# import the requests module to make HTTP requests
import requests
# import the argparse module to get the city name from the command line
import argparse
# import the json module to handle JSON data
import json

# create a variable to store the API key
#

API_KEY = 'cc8bf2b2b089cf2e8669737ba08135b6'

# create a logo for the app
logo = """
___    __    ____  _______     ___   .___________. __    __   _______ .______      
\   \  /  \  /   / |   ____|   /   \  |           ||  |  |  | |   ____||   _  \     
 \   \/    \/   /  |  |__     /  ^  \ `---|  |----`|  |__|  | |  |__   |  |_)  |    
  \            /   |   __|   /  /_\  \    |  |     |   __   | |   __|  |      /     
   \    /\    /    |  |____ /  _____  \   |  |     |  |  |  | |  |____ |  |\  \----.
    \__/  \__/     |_______/__/     \__\  |__|     |__|  |__| |_______|| _| `._____|  """
rain_logo = """      __   _
    _(  )_( )_
   (_   _    _)
  / /(_) (__)
 / / / / / /
/ / / / / /
"""

# create a class to add color to the output
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#create a function to get the weather data

def get_weather(city):
    print(color.YELLOW + logo)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    #create a try block to handle errors
    try:
        #get the weather data from the API
        response = requests.get(url)
        #convert the JSON data to a python dictionary
        weather_data = response.json()
        #get the weather data from the dictionary
        description = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        temp_min = weather_data["main"]["temp_min"]
        temp_max = weather_data["main"]["temp_max"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]

        # create a dictionary to store the weather data with the fields
        fields = {'Weather': f"{description}  ☁️",
                  'Temperature': f"{temp} °C  🌡️",
                  'Feels_like': f"{feels_like} °C  🌡️",
                  'Min_Temperature': f"{temp_min} °C  🌡️",
                  'Max_Temperature': f"{temp_max} °C  🌡️",
                  'Humidity': f"{humidity} %",
                  'Pressure': f"{pressure} mb",
                  'Wind_speed': f"{wind_speed} m/sec  💨"
                  }

                
        print(color.BLUE + rain_logo)
        for field, val in fields.items():

            #print the weather data
            print(color.BOLD + color.GREEN + f"   {color.PURPLE + field}:   {color.DARKCYAN + val}" + color.END)

            #create exception handling for errors
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    except KeyError as err:
        print(color.RED + f"City not Found: {err}")
    except json.JSONDecodeError as err:
        print(f"JSON Decode Error: {err}")

    #create a main function to run the program
if __name__ == 'main':
    #create a parser to get the city name from the command line
    parser = argparse.ArgumentParser(description='Get the current weather forecast for a city.')
    parser.add_argument('city', type=str, help='Enter name of the city')

    args = parser.parse_args()
    city = args.city

    #call the get_weather function
    get_weather(city)

#dependencies
#requests
#argparse
#json

#run the program
#python weather_app.py city_name

#example
#python weather_app.py london

#output
#Weather:       overcast clouds  ☁️
#Temperature:   10.01 °C  🌡️