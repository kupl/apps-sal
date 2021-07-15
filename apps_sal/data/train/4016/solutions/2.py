def game(a, b):
    n = int(a**0.5)
    return "Non-drinkers can't play" if a * b == 0 else "Mike" if n*(n+1) > b  else "Joe"
