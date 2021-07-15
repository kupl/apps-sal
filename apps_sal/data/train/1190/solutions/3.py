for _ in range (int(input())):
    cash = int(input())
    menu = 11
    count = 0
    while(cash>0):
        if(cash>=pow(2,menu)):
            cash -= pow(2,menu)
            count += 1
        else:
            menu -= 1 
    print(count)
