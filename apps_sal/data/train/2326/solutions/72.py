N = int(input())
As = list(map(int, input().split()))

sorted_iAs = sorted(map(tuple, enumerate(As)), key=lambda t: (t[1], t[0]), reverse=True)


ans = [0] * N
youngest_index = 10 ** 9
for index, (original_index, A) in enumerate(sorted_iAs):
    youngest_index = min(original_index, youngest_index)
    if index == N - 1:
        ans[youngest_index] += A * (index + 1)
    elif sorted_iAs[index + 1][1] < A:
        next_A = sorted_iAs[index + 1][1]
        ans[youngest_index] += (A - next_A) * (index + 1)

print(*ans, sep='\n')
