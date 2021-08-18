from sys import stdin, stdout
from itertools import combinations
input = stdin.readline
print2 = stdout.write


def sub_lists(my_list, le):
    for x in combinations(my_list, 2):
        if sum(x) == 2000:
            return "Accepted"
    return "Rejected"


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        input()
        print("Rejected")
        continue
    elif n == 2:
        if sum(map(int, stdin.readline().split())) != 2000:
            print("Rejected")
        else:
            print("Accepted")
        continue
    a = sorted(list(map(int, stdin.readline().split())))
    i = n - 1
    while i >= 0 and a[i] > 2000:
        i -= 1
    if i <= 0:
        print("Rejected")
        continue
    i += 1
    if sum(a[:i]) < 2000:
        print("Rejected")
        continue
    print(sub_lists(a[:i], i))
