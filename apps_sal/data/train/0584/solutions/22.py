T = int(input())
for _ in range(T):
    S = input()
    t = -1
    if S[0] == '0':
        print(0)
        continue
    else:
        i = 1
        count = 0
        while i < len(S):
            if i == len(S) - 1 and S[i] == '0':
                print(count + 1)
                break
            if t == -1 and i == len(S) - 1:
                print(0)
                break
            if t == 0 and S[i] == '1':
                print(count)
                break
            if S[i] == '0':
                t = 0
            if S[i] == '0' and t == 0:
                count += 1
            i = i + 1
