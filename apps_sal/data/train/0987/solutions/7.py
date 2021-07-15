for _ in range(int(input())):
    f,dtb,ta,bs=list(map(int,input().split()))
    btime=f/bs
    ttime=((f+dtb)*2)/ta
    ttime=(ttime)**(1/2)
    if(btime<ttime):
     print("Bolt")
    else:
     print("Tiger")

