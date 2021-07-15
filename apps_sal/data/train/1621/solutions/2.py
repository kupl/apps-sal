def count_change(money, coins):
    A = [1] + [0]*money
    for c in coins:
        A = [sum(A[:k+1][::-c]) for k in range(money+1)]
    return A[-1]
