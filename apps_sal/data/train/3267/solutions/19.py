def well(x): return ('Fail!', 'Publish!', 'I smell a series!')[min(int(x.count('good') / 2 + 0.5), 2)]
