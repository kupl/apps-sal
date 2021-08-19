for _ in range(int(input())):
    (N, d) = [int(x) for x in input().split()]
    S = str(N)
    New = str()
    List = []
    List1 = []
    for i in S:
        List.append(int(i))
    for i in range(len(List)):
        if List[i] == min(List[i:len(List)]):
            New += str(List[i])
    for i in New:
        List1.append(int(i))
    for i in range(len(List1) - 1, -1, -1):
        if List1[i] >= d:
            List1[i] = d
        else:
            break
    BadNew = str()
    for i in List1:
        BadNew += str(i)
    X = len(S) - len(BadNew)
    for i in range(X):
        BadNew += str(d)
    print(BadNew)
