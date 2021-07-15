search = lambda budget, prices: ",".join(map(str, sorted([x for x in prices if x <= budget])))
