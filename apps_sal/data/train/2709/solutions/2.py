def take_umbrella(weather, rain_chance):
    # Your code here.
    a = (weather == 'sunny' and rain_chance > 0.5)
    b = (weather == 'rainy')
    c = (weather == 'cloudy' and rain_chance > 0.2)
    return bool(a or b or c)
