def main():
    N, Q = map(int, input().split())
    tl = [] # イベントタイムライン
    for _ in range(N):
        S, T, X = map(int, input().split())
        tl.append((S-X, 1, X)) # insert
        tl.append((T-X, 0, X)) # erase
    for _ in range(Q):
        D = int(input())
        tl.append((D, 2, 0)) # min
    tl.sort()
    working = set() # 工事中
    wcur = 0 # 工事中の区域の数
    curmin = -1
    flag = False
    for t, c, x in tl:
        if c == 0: # erase
            wcur -= 1
            working.remove(x)
            if x <= curmin:
                curmin = x
                flag = True
        elif c == 1: # insert
            wcur += 1
            working.add(x)
            if curmin < 0 or curmin >= x:
                curmin = x
                flag = False
        else: # min
            if wcur == 0:
                curmin = -1
                flag = False
            elif flag:
                curmin = min(working)
                flag = False
            print(curmin)
    return
    
def __starting_point():
    main()
__starting_point()
