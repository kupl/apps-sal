# cook your dish here
        
def hill(lst):
    maxm = lst.index(max(lst))

    if maxm == 0 or maxm == len(lst) -1:
        return 1
    else:
        return 1 + min(hill(lst[:maxm]), hill(lst[maxm + 1:]))

    

t = int(input())

for _ in range(t):
    n = int(input())
    
    lst = list(map(int, input().split(' ')))

    print(hill(lst))

