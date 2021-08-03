import sys
N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

A_max_right = [A[-1]]
A_min_left = [A[0]]
for a in A[-2::-1]:
    A_max_right.append(max(a, A_max_right[-1]))
A_max_right.reverse()
for a in A[1:]:
    A_min_left.append(min(a, A_min_left[-1]))

A_dig = 0
for i in range(N):
    A_dig = max(A_dig, A_max_right[i] - A_min_left[i])

#print(A_max_right, A_min_left, A_dig)


def ct_edges(ma, mi, start):
    counting_max = 1  # 0:counting max, 1:counting min
    i = start
    ct_max = [0]
    ct_min = []
    while i >= 0 and A_max_right[i] == ma and A_min_left[i] == mi:
        if counting_max:
            if A[i] == ma:
                ct_max[-1] += 1
            elif A[i] == mi:
                ct_min.append(1)
                counting_max = 0
        else:  # counting min
            if A[i] == mi:
                ct_min[-1] += 1
            elif A[i] == ma:
                ct_max.append(1)
                counting_max = 1
        #print(i, A[i], ma, mi, ct_max, ct_min)
        i -= 1

    if len(ct_max) != len(ct_min):
        print("Error! Type:1")
        return

    tmp_max = 0
    tmp_min = sum(ct_min)
    tmp = tmp_max + tmp_min
    for j in range(len(ct_max)):
        tmp_max += ct_max[j]
        tmp_min -= ct_min[j]
        tmp = min(tmp, tmp_max + tmp_min)

    ct = tmp
    end = i
    return ct, end


i = N - 1
ans = 0
while i >= 0:
    if A_max_right[i] - A_min_left[i] != A_dig:
        i -= 1
    else:
        # print(i)
        ct, i = ct_edges(A_max_right[i], A_min_left[i], start=i)
        ans += ct
print(ans)
