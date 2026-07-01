import requests
from tkinter import * 

def get_weather():
    city = city_entry.get()
    API_KEY= "your_api_key"
    Base_Url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")

    try:
        response = requests.get(Base_Url)
        data = response.json()
        if response.status_code==200:
            weather_text = (
            f"📍 {data['name']}, {data['sys']['country']}\n\n"
                f"🌡 Temperature : {data['main']['temp']}°C\n"
                f"🤗 Feels Like : {data['main']['feels_like']}°C\n"
                f"💧 Humidity : {data['main']['humidity']}%\n"
                f"🌥 Weather : {data['weather'][0]['description'].title()}\n"
                f"💨 Wind Speed : {data['wind']['speed']} m/s"
            )
            result_label.config(text=weather_text)
        
        else:
           result_label.config(text = f" City {city} not found. Please check the name and Try again.")    
    except Exception as e:
        result_label.config(text=f"Something went wrong :\n {e}")



#-----------------------------------------------------------------------------------------------

root = Tk()
root.title("Weather App")
root.geometry("400x300")

city_entry = Entry(root,font=("Arial", 14),justify="center")
city_entry.pack(padx=10, pady=10, fill="x")


button1 = Button(root,text="Get Weather",command=get_weather,font=("Arial", 12))
button1.pack(pady=5)


result_label = Label(root,font=("Arial", 14),justify="center")
result_label.pack(pady=20, padx=10)

root.mainloop()
