def search_substr(s, sub, overlap=True):
    return 0 if not s or not sub else sum(s[i:].startswith(sub) for i in range(len(s))) if overlap else len(s.split(sub)) - 1
