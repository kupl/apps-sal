T = int(input())

line_flag = 0
out = ""
for t in range(2 * T):
    if line_flag == 0:
        N = int(input())
        line_flag = 1
    elif line_flag == 1:
        S = input().split()
        for i in range(len(S)):
            S[i] = int(S[i])
        S.sort()
        min_array = []
        for i in range(len(S) - 1):
            min_array.append(abs(S[i + 1] - S[i]))
        out += str(min(min_array)) + "\n"
        line_flag = 0

print(out[:-1])
