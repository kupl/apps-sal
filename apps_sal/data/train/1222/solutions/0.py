def sort_str(s):
    o = []
    for c in s:
        o.append(c)
    o.sort()
    return "".join(o)
def find_ana(s):
    if len(s) <= 1:
        return 0
    h = {}
    c = 0
    for i in range(len(s)):
       for j in range(i+1, len(s)+1):
          t = sort_str(s[i:j])
          if t in h:
            c += h[t]
            h[t] += 1
          else:
            h[t] = 1
    return c
t = int(input())
for _ in range(t):
    print(find_ana(input()))
