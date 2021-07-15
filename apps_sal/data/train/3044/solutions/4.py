is_pal = lambda s: all(s[i] == s[len(s)-i-1] for i in range(len(s)//2))
solve  = lambda s: any(is_pal(s[i:]+s[:i]) for i in range(len(s)))
