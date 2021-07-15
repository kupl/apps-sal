def feast(beast, dish):
    animalbegin=beast[0]
    animalend=beast[len(beast)-1]
    dishbegin=dish[0]
    dishend=dish[len(dish)-1]
    if animalbegin==dishbegin and animalend==dishend:
        return True
    return False
