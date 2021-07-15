li = [1, 1]
while len(li) != 1000 : li.append(li[-li[-1]] + li[-li[-2]])
hofstadter_Q=lambda n:li[n-1]
