def power_of_two(x):
    if x % 2 and x != 1 : return 0
    while x > 2 :
        x = x//2
        if x % 2 and x != 1 : return 0
  
    return ( x == 2 or x == 1)
