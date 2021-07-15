import math
#r,g,b=map(int,input().split())
#list1 = input().split()
#for i in range(len(list1)):
#    list1[i] = int(list1[i])
#print(list1)
#print(r, g, b)
# arr = [[0 for x in range(columns)] for y in range(rows)]

lookup = "abcdefghijklmnopqrstuvwxyz"
t=int(input())

def helper(string, k):
    n = len(string)
    m = n//2
    if(n == 1 and string  == lookup[k]):
        return 0
    elif(n == 1):
        return 1
    else:
        front1 = helper(string[0:m], k+1)
        back1 = helper(string[m:n], k+1)
        for i in range(m):
            if(string[i] != lookup[k]):
                back1 += 1
        for i in range(m):
            if(string[m + i] != lookup[k]):
                front1 += 1
        return min(front1, back1)

for i in range(t):
    n = int(input())
    string = input()
    print(helper(string, 0))



    
        

