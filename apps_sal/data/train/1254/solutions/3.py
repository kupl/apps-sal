def ishard(participants, studentswhosolved):
    if studentswhosolved <= int(participants / 10):
        return True
    else:
        return False


def iscakewalk(participants, studentswhosolved):
    if studentswhosolved >= int(participants / 2):
        return True
    else:
        return False


for t in range(int(input())):
    (n, p) = list(map(int, input().split()))
    cakwalkproblems = 0
    hardproblems = 0
    numberlist = list(map(int, input().split()))
    for _ in range(n):
        if ishard(p, numberlist[_]):
            hardproblems += 1
        elif iscakewalk(p, numberlist[_]):
            cakwalkproblems += 1
    if cakwalkproblems == 1 and hardproblems == 2:
        print('yes')
    else:
        print('no')
