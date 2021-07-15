s1 = input()
s2 = input()
rs = list(map(int, input().split()))

def is_in(big, little):
    i, j = 0, 0
    matched = 0
    while i < len(big) and j < len(little):
        if big[i] == little[j]:
            matched += 1
            i +=1
            j += 1
        else:
            i += 1
    if matched < len(little):
        return False
    return True

def gen_st(mid):
    nonlocal s1, s2, rs
    cs = set(rs[:mid])
    n = []
    for i in range(len(s1)):
        if i+1 in cs:
            continue
        n.append(s1[i])
    #print(''.join(n), s2)
    return is_in(''.join(n), s2)

start = 0
end = len(rs)
weird = False
#print(gen_st(4))
while start < end:
    #print(start, end)
    mid = (start+end)//2
    if gen_st(mid):
        start = mid
        if start == end-1:
            weird = True
            if gen_st(end):
                print(end)
                break
            else:
                print(start)
                break
    else:
        end = mid - 1
    if not weird and start == end:
        print(start)


