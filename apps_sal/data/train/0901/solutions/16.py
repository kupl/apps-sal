import random
t = int(input())
while t>0:
    t -= 1
    
    n, k, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    #temp = range(n, 0, -1)
    #random.shuffle(temp)
    #random.shuffle(temp)
    temp = sorted(list(range(n)),key=lambda x:arr[x],reverse=True)
    ans = [str(i+1) for i in temp]
    print(' '.join(ans[::-1]))
