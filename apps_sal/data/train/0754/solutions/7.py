import sys
def input(): return sys.stdin.readline()


for _ in range(int(input())):
    k = int(input())
    for i in str(k):
        if int(i) % 2 == 0:
            print("1")
            break
    else:
        print("0")
