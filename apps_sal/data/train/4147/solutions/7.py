from string import ascii_lowercase as s

def play_pass(message,key):
    m = message.lower().translate(str.maketrans(s+"0123456789",s[key%26:]+s[:key%26]+"9876543210"))
    return "".join([j if i%2==1 else j.upper() for i,j in enumerate(m)][::-1])
