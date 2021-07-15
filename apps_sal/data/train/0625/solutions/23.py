for s in[*open(0)][2::2]:
 d = {0: 1}
 t = 0
 for x in s.split():
  t = (t + int(x[0])) % 10
  d[t] = d.get(t, 0) + 1
 print(sum(k * (k - 1) // 2 for k in list(d.values())))

