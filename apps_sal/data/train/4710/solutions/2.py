luck_check = lambda s: sum(map(int,s[:len(s)//2])) == sum(map(int, s[len(s)//2 + len(s)%2:]))
