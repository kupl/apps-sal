def get_the_largest_contiguous_subarray_sum(A, N):
    max_sum_so_far = 0
    max_sum_ending_here = 0
    for i in range(N):
        max_sum_ending_here += A[i]
        if max_sum_ending_here < 0:
            max_sum_ending_here = 0
        else:
            max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)
    return max_sum_so_far


(N, x) = list(map(int, input().split()))
A = list(map(int, input().split()))
array_sum = sum(A)
max_subarray_sum = get_the_largest_contiguous_subarray_sum(A, N)
profit = max_subarray_sum - max_subarray_sum / x
min_sum_possible = array_sum - profit
print(min_sum_possible)
