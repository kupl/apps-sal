for _t in range(int(input())):
    J = set(list(input().strip()))
    print(sum(1 for x in input() if x in J))
