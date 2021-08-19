try:
    for _ in range(int(input())):
        number = int(input())
        list_hai_bhai = list(map(int, input().split(' ')))
        dic = {}
        verma = 0
        for cv in range(number - 1):
            if list_hai_bhai[cv] == list_hai_bhai[cv + 1]:
                list_hai_bhai[cv + 1] = -1
                verma = 1
        list_hai_bhai.sort()
        for cv in range(number):
            if list_hai_bhai[cv] in dic:
                dic[list_hai_bhai[cv]] += 1
            else:
                dic[list_hai_bhai[cv]] = 1
        if verma == 1:
            dic.pop(-1)
        print(max(dic, key=dic.get))
except:
    pass
