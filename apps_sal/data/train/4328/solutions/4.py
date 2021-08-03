def friend_find(L): return sum(p == 'red' and any(L[x:x + 3].count('blue') == 2 for x in range(max(0, i - 2), i + 1))for i, p in enumerate(L))
