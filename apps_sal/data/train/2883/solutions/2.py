CONFIG = [
    ('',"week",3600*24*7),
    ('',"day",3600*24),
    ('n',"hour",3600),
    ('',"minute",60),
    ('',"second",1)
]

def to_pretty(s):
    return next((out(one,t,s//n) for one,t,n in CONFIG if s//n), "just now")

def out(one,t,n):
    return f'{n==1 and "a"+one or n} {t}{n>1 and "s" or ""} ago'
