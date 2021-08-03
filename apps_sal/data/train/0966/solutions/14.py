standard_input = '''3
7 3 2
2 5 1 2 3 4 1
5 2 3
4 4 4 4 4
5 2 7
1 4 3 2 1'''

for _ in range(int(input())):
    n, u, d = map(int, input().split())
    d = -1 * d
    hill = list(map(int, input().split()))
    jump = 1
    para = 1
    for i in range(n - 1):
        if hill[i + 1] - hill[i] < d:
            if para == 0:
                break
            jump += 1
            para = 0
            continue
        if hill[i + 1] - hill[i] <= u:
            jump += 1
        else:
            break
    print(jump)
