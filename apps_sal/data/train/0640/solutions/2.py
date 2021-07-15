# def find(x,y):
#     if x==y:
#         return 0
    
#     if x > y:
#       greater = x
#     else:
#       greater = y

#     while(True):
#       if((greater % x == 0) and (greater % y == 0)):
#           lcm = greater
#           break
#       greater += 1
#     return lcm
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
# cook your dish here
t = int(input())


for i in range(t):
    x_y = input().split()
    x = int(x_y[0])
    y = int(x_y[1])
    if x == y:
        print(0)
    else:
        sweetness = compute_lcm(x,y)
        x = (sweetness/x)-1
        y = (sweetness/y)-1
        print(int(x+y))
