def watch_pyramid_from_the_side(s):
    return '\n'.join(f"{' '*(len(s)-i)}{(i*2-1)*c}{' '*(len(s)-i)}" for i,c in enumerate(reversed(s), 1)) if s else s

def watch_pyramid_from_above(s):
    if not s:
        return s
    n = len(s) - 1
    a = []
    for i in range(n + 1):
        a.append(s)
        n -= 1
        s = s[:n] + s[n] * (i + 2) 
    a = [s + s[::-1][1:] for s in a]
    a =  a[1:][::-1] + a
    return '\n'.join(a)

def count_visible_characters_of_the_pyramid(s):
    return (len(s) * 2 - 1) ** 2 if s else -1

def count_all_characters_of_the_pyramid(s):
    return sum(((n+1)*2-1)**2 for n in range(len(s))) if s else -1



