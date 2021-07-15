add=lambda l:"Invalid input"if any(type(e)!=int for e in l)or type(l)!=list else[sum(l[:i+1])for i in range(len(l))]
