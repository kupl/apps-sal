word_square=lambda s:len(s)**.5%1==0and sum(s.count(c)%2for c in set(s))<=len(s)**.5
