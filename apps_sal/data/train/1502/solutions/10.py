# cook your dish here
t = int(input())

for _ in range(t):
    s = set(str(input()).strip())
    n = int(input())
    arr = set(str(input()).split())
    
    if len(s.difference(arr)) == 0:
        print(1)
    else:
        print(0)
