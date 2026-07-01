import requests
 

def get_weather(city):
    API_KEY= "your_api_key"
    Base_Url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")

    try:
        response = requests.get(Base_Url)
        data = response.json()
        if response.status_code==200:
            print(f"Weather in {data['name']}, {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']}°C")
            #print(f"Feels Like  : {data['main']['feels_like']}°C")
            print(f"Humidity    : {data['main']['humidity']}%")
            #print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather'][0]['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
        else:
            print(f" City {city} not found. Please check the name and Try again.")    
    except Exception as e:
        print(f"Something went wrong : {e}")

if __name__ =="__main__":
    city = input("Enter the city name:")
    get_weather(city)
    
           