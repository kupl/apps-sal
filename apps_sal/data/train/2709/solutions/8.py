def take_umbrella(weather, rain_chance):
        return((weather == "rainy")
        or ((rain_chance > 0.2) and (weather == "cloudy"))
        or ((rain_chance > 0.5) and (weather == "sunny")))

