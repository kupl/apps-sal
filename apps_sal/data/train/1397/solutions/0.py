def mForMaxSeq(arr, n):
    eim = dict()
    for i in range(n):
        if arr[i] in eim:
            eim[arr[i]].append(i)
        else:
            eim[arr[i]] = [i]
    
    keys = sorted(eim.keys())
    
    # print(eim, keys)

    connected = False
    count = 0
    pI = -1

    nKeys = len(keys)
    for i in range(nKeys-1):
        
        if not connected:
            pI = eim[keys[i]][0]
            
            for idx in eim[keys[i+1]]:
                if idx >pI:
                    connected = True
                    count += 1
                    pI = idx
                    break
        else:
            connected = False

            for idx in eim[keys[i+1]]:
                if idx > pI:
                    connected = True
                    count += 1
                    pI = idx
                    break

    
    return (nKeys - count)


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        
        print(mForMaxSeq(arr, n))
        
        

__starting_point()
