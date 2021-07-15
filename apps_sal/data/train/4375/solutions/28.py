def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""

    for idx, planete in [(1, "Mercury"), (2, "Venus"), (3, "Earth"), (4, "Mars"), (5, "Jupiter"), (6, "Saturn"), (7, "Uranus"), (8, "Neptune")]:
        if idx == id:
            return planete
    return 'ID not fund'    
    
    
    
    
    

