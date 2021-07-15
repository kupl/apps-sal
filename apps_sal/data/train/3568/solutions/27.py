def bumps(road):
    n = 0
    for i in road:
       if i=="n":
          n = n+1
    return ("Woohoo!" if n<=15 else "Car Dead" )

