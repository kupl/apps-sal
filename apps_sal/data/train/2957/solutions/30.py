def get_drink_by_profession(param):
    client_drink = {
        "jabroni":"Patron Tequila",
        "school counselor":"Anything with Alcohol",
        "programmer":"Hipster Craft Beer",
        "bike gang member":"Moonshine",
        "politician":"Your tax dollars",
        "rapper":"Cristal",
    }
    return client_drink[param.lower()] if param.lower() in client_drink else "Beer"
