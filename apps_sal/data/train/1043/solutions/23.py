'''
  Problem : Mahasena
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 29/01/2021
'''


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        aitihasik_bhasa = list(map(str, input().split()))
        d = {}
        for b in aitihasik_bhasa:
            d[b] = False
        for _ in range(k):
            vakya = list(map(str, input().split()))
            vakya = vakya[1:]
            for v in vakya:
                if v in d:
                    d[v] = True
        for v in aitihasik_bhasa:
            if d[v]:
                print('YES', end=' ')
            else:
                print('NO', end=' ')
        print()


def __starting_point():
    solve()


__starting_point()
