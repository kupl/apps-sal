(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
cost = 0
x_prev = X[0]
for x_next in X[1:]:
    walk_cost = A * (x_next - x_prev)
    tele_cost = B
    cost += min(walk_cost, tele_cost)
    x_prev = x_next
print(cost)
