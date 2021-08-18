for i in range(int(input())):
    a = input()
    cnt = 0
    for i in a:
        if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            cnt = cnt + 0
        elif(i == "b" or i == "f" or i == "j" or i == "d" or i == "h" or i == "n" or i == "p" or i == "t" or i == "v"):
            cnt = cnt + 1
        elif(i == "c" or i == "g" or i == "k" or i == "m" or i == "q" or i == "s" or i == "w"):
            cnt = cnt + 2
        elif(i == "l" or i == "r" or i == "x"):
            cnt = cnt + 3
        elif(i == "y"):
            cnt = cnt + 4
        else:
            cnt = cnt + 5
    print(cnt)
