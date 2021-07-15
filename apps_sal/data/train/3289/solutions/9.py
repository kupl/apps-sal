def motif_locator(s, m):
    return [i+1 for i in range(len(s)-len(m)+1) if s[i:i+len(m)]==m]
