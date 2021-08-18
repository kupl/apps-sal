try:
    t = int(input())
    for i in range(t):
        ar = list(map(int, input().split()))
        if (ar[0]**2 + ar[1]**2 > ar[2]**2 + ar[3]**2):
            print("B IS CLOSER")
        else:
            print("A IS CLOSER")


except:
    pass
