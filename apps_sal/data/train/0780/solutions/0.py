import sys
user_input = sys.stdin.readline().split()
T = int(user_input[0])
for j in range(T):
    var = sys.stdin.readline().split()
    N = int(var[0])
    M = int(var[1])
    if N % M % 2:
        print('ODD')
    else:
        print('EVEN')
