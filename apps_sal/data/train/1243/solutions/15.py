import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = input()
    for i in range(len(n)):
        if(n[i] == '0' or n[i] == '5'):
            print("1")
            break
    else:
        print("0")
