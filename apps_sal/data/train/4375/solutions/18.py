def get_planet_name(id):

    # switch-case statement doesn't work on python unlike java so convert it in dictionary
    switch = {1: "Mercury",
              2: "Venus",
              3: "Earth",
              4: "Mars",
              5: "Jupiter",
              6: "Saturn",
              7: "Uranus",
              8: "Neptune"}
    # use .get() function to get the value of the input from user
    return switch.get(id)
