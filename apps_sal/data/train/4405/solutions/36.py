def is_palindrome(st):
    st=str(st)
    if len(st)%2==0:
        if st[:(len(st)//2)][::-1]==st[(len(st)//2):]:
            return True
        return False
    else:
        if st[:(len(st)//2)][::-1]==st[(len(st)//2)+1:]:
            return True
        return False
