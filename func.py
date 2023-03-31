from pyowm import OWM

def weather(city):
    owm = OWM('7a22c510c5659189e790f0257a1bcff3')
    mgr = owm.weather_manager()
    davlat = 'Uzbekistan'
    shvd = city + ", " + davlat
    observation = mgr.weather_at_place(shvd)
    w = observation.weather
    answers = "🌡Havo harorati: " + str(w.temperature('celsius')['temp']) + 'º' + "\n💨Shamol tezligi: " + str(w.wind()['speed']) + ' m/s' + "\n💧Havo namligi: " + str(w.humidity) + ' g/m³'
    return answers


regions = ["Andijan","Bukhara","Fergana","Jizzakh","Karakalpakstan","Khorezm","Namangan","Navoiy","Qashqadaryo","Samarqand","Sirdaryo","Surxondaryo","Tashkent","Xorazm",]


