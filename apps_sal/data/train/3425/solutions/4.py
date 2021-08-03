def word_square(s): return len(s)**.5 % 1 == 0 and sum(s.count(c) % 2for c in set(s)) <= len(s)**.5
