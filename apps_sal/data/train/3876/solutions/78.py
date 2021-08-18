def find(n):
    char = n + 1
    mystr = 0
    while char >= 4:
        char -= 1
        if(char % 3) == 0:
            mystr += (char)

        else:
            if(char) % 5 == 0:
                mystr += (char)
        if char == 3:
            return(int(mystr))
