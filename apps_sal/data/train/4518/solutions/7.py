from re import search
def wheres_wally(s): return (lambda r: -1 if r == None else r.start(0))(search("(^|(?<= ))Wally(\W|$)", s))
