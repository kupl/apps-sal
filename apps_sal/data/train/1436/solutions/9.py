# cook your dish here
t=int(input())
for _ in range(t):
    h=input()
    if h == h[::-1]:
        print(1)
    else: print(2)
