def jumping_number(number):
    number = str(number)
    return ("Jumping!!"if all(abs(int(number[i+1]) - int(number[i])) == 1 for i in range(len(number)-1)) else "Not!!")
