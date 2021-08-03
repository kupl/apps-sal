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

        if s[0] == '1' and s[1] == '0':
            s[1] = '1'
            total_infected += 1

        i = 1
        while i < (N + k):
            if s[i] == '1':
                if s[i - 1] == '0':
                    s[i - 1] = '1'
                    total_infected += 1
                if s[i + 1] == '0':
                    s[i + 1] = '1'
                    total_infected += 1
                    i += 1
            i += 1

        return (s, total_infected)

    for i in range(n):
        s = seperate(s, i + days[i])
        s, total_infected = infect(s, i, total_infected)

    print(total_infected)
