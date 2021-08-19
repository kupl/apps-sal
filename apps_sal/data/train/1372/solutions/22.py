# cook your dish here
# cook your code here

t = int(input())

while(t):

    l1 = list(map(int, input().split(" ")))
    res = 0
    a = l1[0] * l1[0] + l1[1] * l1[1]
    b = l1[2] * l1[2] + l1[3] * l1[3]
    if(a > b):
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")

    t -= 1
