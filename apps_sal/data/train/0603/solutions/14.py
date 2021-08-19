T = int(input())
ans = []

# S = 'zyxwvutsrqponmlkjihgfedcba'
S = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(T):
    K = int(input())

    if(K % 25 == 0):
        a = S[::-1] * (K // 25)
    else:
        a = S[:1 + K % 25][::-1] + S[::-1] * (K // 25)
    ans.append(a)

for i in ans:
    print(i)
