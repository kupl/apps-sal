def position(ch):
    for i in range(26):
        if ch.lower() == "abcdefghijklmnopqrstuvwxyz"[i]: return f"Position of alphabet: {i+1}"
    return False        
