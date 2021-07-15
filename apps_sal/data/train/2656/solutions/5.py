REGEX = __import__("re").compile(r"[ -]").split
letters = ((4,), (2,2), (1,1,2), (1,1,1,1))

def code(L):
    return ''.join(L[i][:j] for i,j in enumerate(letters[len(L)-1])).upper()

def bird_code(arr):
    return [code(REGEX(name)) for name in arr]
