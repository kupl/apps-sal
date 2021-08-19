def solve(arr):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return_list = []
    for word in arr:
        print(word)
        counter = 0
        for i in range(len(word) if len(word) <= len(alphabet) else 25):
            if word.lower()[i] == alphabet[i]:
                counter += 1
        return_list.append(counter)
    return return_list
