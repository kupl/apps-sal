N = int(input())
As = list(map(int, input().split()))

sorted_iAs = sorted(map(tuple, enumerate(As)), key=lambda t: (t[1], t[0]), reverse=True)

# if As = 1 2 1 3 2 4 2 5 8 1
# then sorted_iAs is:
#   i | 8 7 5 3 6 4 1 9 2 0
#   A | 8 5 4 3 2 2 2 1 1 1
# I'll look at:
#       x x x x     x     x
# where the next A decreases (or doesn't exist).

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
