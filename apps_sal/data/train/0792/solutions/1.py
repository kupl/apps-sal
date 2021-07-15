# cook your dish here
t = int(input())

for _ in range(t):

    n,s = input().split()

    N = int(n) 
    r = N - len(s)

    count = 0

    if N>len(s):

     count = pow(26, r-1,(10**9+7))
     count*= (26+25*len(s))

     count = count%(10**9 + 7)
    print(count)


