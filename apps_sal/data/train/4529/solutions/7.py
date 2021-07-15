truncate_string=lambda str,n: str if n>=len(str) else str[:n-3 if n>3 else n]+'...'
