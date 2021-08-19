# Md. Khairullah Gaurab
# SUST, CSE, 20th Batch
#  gaurab.cse.sust@gmail.com


test = int(input())

for i in range(test):
    N, S, K = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    ans = [i + 1 for i in range(N)]
    ans.sort(reverse=True)
    for j in range(N):
        print(ans[j], end=' ')
    print('')
