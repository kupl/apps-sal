def get_planet_name(id):
    id_dict = {1: "Mercury",
               2: "Venus",
               3: "Earth",
               4: "Mars",
               5: "Jupiter",
               6: "Saturn",
               7: "Uranus",
               8: "Neptune"}
    for key in id_dict.keys():
        if key == id:
            return id_dict[key]
