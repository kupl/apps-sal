'''
  Problem : Id and Ship
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
'''


def solve():
    for _ in range(int(input())):
        s = str(input())
        r = 'yes'
        for i in range(0, len(s), 2):
            if s[i] == s[i + 1]:
                r = 'no'
                break
        print(r)


def __starting_point():
    solve()


__starting_point()
