def truncate_string(s, n):
    return s if n>=len(s) else s[:n]+'...' if n<=3 else s[:n-3]+'...'
