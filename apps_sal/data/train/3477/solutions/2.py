sort_string=lambda s,o:''.join(sorted(s,key=lambda x,d={c:i for i,c in reversed(list(enumerate(o)))}:d.get(x,len(o))))
