# cook your dish here
def get_input():
    s = []
    a, b, c = list(map(int, input().split()))
    s.append(a)
    s.append(b)
    s.append(c)
    s.sort()
    print(s[1])


n = int(input())
for i in range(n):
    get_input()
