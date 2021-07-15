def subsetsum(array,num):

    if num == 0 or num < 1:
        return False
    elif len(array) == 0:
        return False
    else:
        if array[0] == num:
            return True
        else:
            return subsetsum(array[1:],(num - array[0])) or subsetsum(array[1:],num)
        
n, q = list(map(int, input().split()))
w = list(map(int, input().split()))
for i in range(q):
    s = list(map(int, input().split()))
    if s[0]==1:
        w[s[1]-1]=s[2]
    elif s[0]==2:
        w=w[:s[1]-1]+w[s[1]-1:s[2]][::-1]+w[s[2]:]
    else:
        if(subsetsum(w[s[1]-1:s[2]], s[3])):
            print("Yes")
        else:
            print("No")
