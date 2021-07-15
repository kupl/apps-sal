two_highest = lambda a, b=exec("import heapq"): heapq.nlargest(2, set(a)) if type(a) is list else False
