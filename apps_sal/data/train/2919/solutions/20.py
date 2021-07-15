def encode(message, key):
    cypher = {chr(ord('a') + i) : i+1 for i in range(26)}
    return [ cypher[letter] + int(str(key)[i % len(str(key))]) for i, letter in enumerate(message) ]
     

