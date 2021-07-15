def how_many_dalmatians(n):
    dogs = {
        n <= 10: "Hardly any", 
        10 < n <= 50: "More than a handful!", 
        n == 101: "101 DALMATIONS!!!"
    }
    return dogs.get(True, "Woah that's a lot of dogs!")

