def encode(message, key):
    ans = [] ;key = list(str(key)); counter = 0
    for i in message:
        if counter == len(key):
            counter = 0
        ans.append(ord(i)-96 + int(key[counter]))
        counter +=1
    return ans

