# cook your dish here
t = int(input())
for b in range(t):
    n = int(input())
    tot = 0
    while(n>0):
        dig=n%10
        tot = tot+dig
        n= n//10
    print(tot)
