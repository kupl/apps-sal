deep_count=d=lambda a:sum(type(e)is not list or d(e)+1for e in a)
