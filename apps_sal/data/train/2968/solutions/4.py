def get_middle(s):
    x = int(len(s)/2)
    return s[x] if len(s)%2!=0 else s[x-1:x+1]
