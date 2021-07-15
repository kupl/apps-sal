def truncate_string(s,n):
    return s if len(s)<=n else s[:n if n<=3 else n-3]+'...'
