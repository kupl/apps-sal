n = int(input())
x = list(map(int,input().split( )))
t = int(input())
def function(x,y):
    p = x[y-1]
    x.remove(x[y-1])
    return p
for i in range(t):
    y = int(input())
    print(function(x,y))

