# cook your dish here
import math
def find():
    x,y = map(int,input().split())
    a = math.gcd(x,y)
    lcm = (x*y)//a
    print(a,lcm)
 

for i in range(int(input())):
    find()
