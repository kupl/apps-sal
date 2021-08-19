# cook your dish here
T = int(input())

for _ in range(T):

    N = int(input())
    s = list(input())
    n = int(input())
    days = list(map(int, input().split()))
    total_infected = sum(1 for x in s if x == '1')

    def seperate(s, d):
        s.insert(d - 1, '#')
        return s

    def infect(s, k, total_infected):
        index_list = set()

        if s[0] == '1' and s[1] == '0':
            s[1] = '1'
            total_infected += 1
        if s[-1] == '1' and s[-2] == '0':
            s[-2] = '1'
            total_infected += 1

        for i in range(1, (N + k)):
            present = s[i]
            prev = s[i - 1]
            next = s[i + 1]

            if present == '1':
                if prev == '0':
                    index_list.add(i - 1)
                if next == '0':
                    index_list.add(i + 1)

        for i in index_list:
            s[i] = '1'
            total_infected += 1
        return (s, total_infected)

    for i in range(n):
        s = seperate(s, i + days[i])
        s, total_infected = infect(s, i, total_infected)

    print(total_infected)
