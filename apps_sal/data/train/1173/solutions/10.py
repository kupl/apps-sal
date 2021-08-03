# cook your dish here
# import atexit
# import io
# import sys
#
#
# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER
#
#
# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
#
# # Brute force approach
# R = lambda :map(int,input().split())
# t = int(input())
# for i in range(t):
#     n = int(input())
#     lst = list(R())
#     cnt = 0
#     for i in range(n):
#         temp = 0
#         for j in range(i,n):
#             temp^=lst[j]
#             if temp==0:
#                 cnt+=j-i
#
#     print(cnt)
def sumPairs(arr, n):
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i * arr[i] - (n - 1 - i) * arr[i]
    return sum - ((n * (n - 1)) // 2)


def R(): return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n = int(input())
    xs = list(map(int, input().split()))
    xor = 0
    dict = {0: [0]}
    count = 0
    i = 0
    # for i in range(1,len(xs)):
    #     xs[i]=xs[i-1]^xs[i]
    # print(xs)
    for x in xs:
        xor = xor ^ x
        if xor not in dict:
            dict[xor] = [i + 1]
        else:
            # for j in dict[xor]:
            #     count += (i + 1) - j - 1
            dict[xor].append(i + 1)
        i += 1
    ans = 0
    for i in list(dict.values()):
        if len(i) == 1:
            continue
        else:
            ans += (sumPairs(i, len(i)))

    # print(dict)
    print(ans)
