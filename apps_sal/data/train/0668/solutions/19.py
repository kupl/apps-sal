def maximum_subarray_sum(a):
    N = len(a)
    max_so_far = -float('inf')
    max_ending_here = 0

    start = 0
    end = 0
    s = 0
    for i in range(N):
        max_ending_here += a[i]
        if(max_ending_here > max_so_far):
            max_so_far = max_ending_here
            start = s
            end = i
        if(max_ending_here < 0):
            max_ending_here = 0
            s = i + 1
    return start, end

# a = [-1,-2,-3,-4,-5]
# print(maximum_subarray_sum(a))


T = int(input())
ans = []

for _ in range(T):
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    if(K == 1):
        s, e = maximum_subarray_sum(A)
        ans.append(sum(A[s:e + 1]))
    else:
        s, e = maximum_subarray_sum(A + A)
        # print('$',s,e,sum(A[2:3]))
        if(e < N):
            ans.append(sum(A[s:e + 1]))
        else:
            e -= N
            ans.append(sum(A[s:]) + sum(A) * (K - 2) + sum(A[:e + 1]))

for i in ans:
    print(i)
