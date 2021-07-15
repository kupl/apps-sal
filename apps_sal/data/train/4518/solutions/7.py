from re import search
wheres_wally=lambda s: (lambda r: -1 if r==None else r.start(0))(search("(^|(?<= ))Wally(\W|$)",s))
