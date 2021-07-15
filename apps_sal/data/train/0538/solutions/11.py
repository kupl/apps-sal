# cook your dish here
t = int(input())

for _ in range(t):
    s,sg,fg,d,t = map(int , input().split(" "))
    
    # t = t/3600
    # d = (d*50)/1000
    
    car_speed = s + (d*50*3.6)/t
    #print(car_speed)
    sebi = abs(car_speed-sg)
    fat = abs(car_speed-fg)
    #print(sebi,fat)
    if sebi<fat:
        print("SEBI")
    elif fat==sebi:
        print("DRAW")
    else:
        print("FATHER")
