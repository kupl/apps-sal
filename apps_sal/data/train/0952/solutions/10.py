for i in range(int(input())):
    a = input()
    g = 0
    for i in a:
        p = ord(i) % 96
        if(p <= 3):
            g += abs(p - 1)
        elif(4 <= p <= 6):
            g += abs(p - 5)
        elif(7 <= p <= 12):
            g += abs(p - 9)
        elif(13 <= p <= 18):
            g += abs(p - 15)
        else:
            g += abs(p - 21)
    print(g)
