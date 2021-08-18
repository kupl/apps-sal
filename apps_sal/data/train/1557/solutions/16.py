def rii(): return map(int, input().strip().split(" "))
def ril(): return list(map(int, input().strip().split(" ")))
def ri(): return int(input().strip())
def rs(): return input()


T = ri()
for _ in range(T):
    N = ri()
    l1 = rs()
    l2 = rs()
    nb1_1 = len(list(filter(lambda x: x == '1', l1)))
    nb2_1 = len(list(filter(lambda x: x == '1', l2)))
    if nb1_1 == nb2_1:
        print("YES")
    else:
        print("NO")
