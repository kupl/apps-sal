def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res
