def get_planet_name(id):
    planet_names = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }
    if (id > 8):
        print("Kelebihan Bos")
    elif (id < 0):
        print("Belajar Lagi Bos")
    else:
        return planet_names.get(id)


print(get_planet_name(3))
