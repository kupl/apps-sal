for i in range(int(input())):
    s = input().strip()
    n = int(input().strip())
    li = input().strip().split()
    
    ans = 1
    
    for el in set(s):
        if el not in li:
            ans = 0
            break
    
    print(ans)
