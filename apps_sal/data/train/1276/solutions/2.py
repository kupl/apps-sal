'''input
1
7 3
3 7 5 4 6 2 1
'''

#~ @author = dwij28 (Abhinav Jha) ~#


def pow2(n): return n and (not(n & (n - 1)))


for T in range(eval(input())):
    n, k = list(map(int, input().strip().split()))
    data = list(map(int, input().strip().split()))
    ans = set()
    for i in data:
        if pow2(i):
            ans.add(i)
    print(k - len(set(ans)))
