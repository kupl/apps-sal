T = int(input())

for _ in range(T):

    _dummy = int(input())
    s = list(input())
    n = int(input())
    days = list(map(int, input().split()))

    def seperate(s, d):
        s.insert(d - 1, '
        return s

    def infect(s):
        index_list=set()

        if s[0] == '1' and s[1] != '
            s[1]='1'
        if s[-1] == '1' and s[-2] != '
            s[-2]='1'

        for i in range(1, len(s) - 1):
            present=s[i]
            prev=s[i - 1]
            next=s[i + 1]

            if present == '1':
                if prev != '
                    index_list.add(i - 1)
                if next != '
                    index_list.add(i + 1)

        for i in index_list:
            s[i]='1'
        return s

    for i in range(n):
        s=seperate(s, i + days[i])
        s=infect(s)
    total_infected=sum(1 for x in s if x == '1')
    print(total_infected)
