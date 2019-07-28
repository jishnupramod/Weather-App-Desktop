import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

WIDTH = 600
HEIGHT = 500

def format_weather(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: {}\nDescription: {}\nTemperature: {}°F\n'.format(name, desc, temp)
    except:
        final_str = 'There occured \na problem retrieving \nthe information'

    return final_str

def get_weather(city):
    weather_key = '2efc8a1d3bf99830e816a0b2527d166f'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)

    current_weather = response.json()

    label['text'] = format_weather(current_weather)

    icon_name = current_weather['weather'][0]['icon']
    open_icon(icon_name)

def open_icon(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize(size, size))
    weather_icon.delete('all')
    weather_icon.image = img



root = tk.Tk()
root.title('WEATHER APP')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#035afc', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 30))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 18), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#035afc', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 30), anchor='nw', justify='left', bd=5)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
