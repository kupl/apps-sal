def feast(beast, dish):
    a=len(dish)-1
    if beast[0]==dish[0] and beast[len(beast)-1]==dish[a]: 
         return True
    else:
        return False
