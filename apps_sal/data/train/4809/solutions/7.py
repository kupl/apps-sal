key   = 'GADERYPOLUKI'
key  += key.lower()
dekey = ''.join(key[i:i+2][::-1] for i in range(0,len(key),2))

def encode(message):
    return message.translate(str.maketrans(key,dekey))
    
def decode(message):
    return message.translate(str.maketrans(dekey,key))
