def f(N, M):
    setn = set()
    setrn = set()
    for ele in N+M:
        if ele in setrn:
            continue
        elif ele in setn:
            setn.remove(ele)
            setrn.add(ele)
        else:
            setn.add(ele)
    
    return list(setn)
    

t = int(input())
answers = list()
for _ in range(t):
    some_inp = input()
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    answers.append(f(N, M))

for answer in answers:
    print(*answer, sep=" ")
