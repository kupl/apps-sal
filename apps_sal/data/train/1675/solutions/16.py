# cook your dish here
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_distance(self, p):
        return math.sqrt((p.x-self.x)*(p.x-self.x) + (p.y-self.y)*(p.y-self.y));

T=int(input())
for t in range(T):
    input()
    n=int(input())
    arr=[]
    for i in range(n):
        x,y=map(int,input().split())
        arr.append(Point(x,y))
    arr.sort(key=lambda p:(p.x,(-1)*p.y))
    s=0.0
    for i in range(1,n):
        s+=arr[i].get_distance(arr[i-1])
    print("{0:.2f}".format(s))
