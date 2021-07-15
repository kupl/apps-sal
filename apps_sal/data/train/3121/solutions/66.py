def solve(ar):
    
    for item in ar:
        if -item not in ar:
            return item
