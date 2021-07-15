def solve(arr):
    abc ='abcdefghijklmnopqrstuvwxyz'
    res = []
    for word in arr:
        word = word.lower()
        count = 0
        for i, letter in enumerate(word):
            if i == abc.index(letter):
                count +=1
        res.append(count)
    return res

