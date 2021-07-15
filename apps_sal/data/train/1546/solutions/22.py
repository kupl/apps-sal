# cook your dish here
t = int(input())
for _ in range (t):
    l = [int(x) for x in input().strip().split(" ")]
    l.sort()
    (a,b,c) = l 
    if(a>0 and b>0 and c>0 and a*a + b*b == c*c):
        print("YES")
    else:
        print("NO")
