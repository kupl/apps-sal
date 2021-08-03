def pair_of_shoes(s): return all([s.count([i[0] ^ 1, i[1]]) == s.count(i)for i in s])
