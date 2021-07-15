t = int(input())
for i in range(t):
    n = int(input())
    if n == 1 :
        print("B")
    elif n%2==0:
        print("B")
    elif  n==3:
        print("A")
    elif (n-3)%2==0:
        print("B")
    else:
        print("A")
