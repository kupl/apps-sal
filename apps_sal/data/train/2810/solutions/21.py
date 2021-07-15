def solve(arr):
    abc = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for word in arr:
        count = 0
        word = word.lower()
        for i, letter in enumerate(word):
            if i == abc.index(letter):
                count += 1
        res.append(count)
    return res
    

