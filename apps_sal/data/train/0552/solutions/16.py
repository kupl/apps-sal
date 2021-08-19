answers = []


def solve(weights, limit):
    weights.sort()
    diff1 = abs(sum(weights[limit:]) - sum(weights[0:limit]))
    diff2 = abs(sum(weights[-limit:]) - sum(weights[:-limit]))
    answers.append(max(diff1, diff2))


T = int(input())
while T:
    (N, K) = [int(x) for x in input().split()]
    weights = [int(x) for x in input().split()]
    solve(weights, K)
    T -= 1
for ans in answers:
    print(ans)
