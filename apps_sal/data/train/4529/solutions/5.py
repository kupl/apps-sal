truncate_string=lambda s,n:s[:n-3*(3<n<len(s))]+'...'*(n<len(s))
