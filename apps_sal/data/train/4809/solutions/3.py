def encode(message):
    s1 = "GADERYPOLUKI"
    s2 = "AGEDYROPULIK"
    return message.translate(str.maketrans(s1,s2)).translate(str.maketrans(s1.lower(),s2.lower()))
    
def decode(message):
    return encode(message)
