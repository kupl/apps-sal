# cook your dish here
t = int(input())
while(t):
    li = [int(i) for i in input().split()]
    d1 = pow((pow(li[0], 2) + pow(li[1], 2)), 0.5)
    d2 = pow((pow(li[2], 2) + pow(li[3], 2)), 0.5)
    if(d1 > d2):
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
    t -= 1
