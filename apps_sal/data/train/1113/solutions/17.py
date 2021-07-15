def maxcount(lst):
    op = [0]*max(lst)
    for i in lst:
        op[i-1]+=1
        
    return op.index(max(op))+1, max(op)

t= int(input())

while (t>0):
    input()
    lst = list(map(int, input().split(' ')))
    counts = maxcount(lst)
    for i in counts:
        print(i, end=' ')    
    print("")    
    t-=1   
