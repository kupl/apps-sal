permutation_position=lambda p:sum(26**i*(ord(c)-97)for i,c in enumerate(p[::-1]))+1
