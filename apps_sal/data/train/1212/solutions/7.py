n = int(input())


def find(arr, num):
    auxarr = [0] * (len(arr) - sum(arr) // num) + [num] * (sum(arr) // num)
    ans = sum([abs(auxarr[i] - arr[i]) for i in range(len(arr))]) / 2
    return ans


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for _ in range(n):
    string = list(input())
    length = len(string)
    dic = {letter: 0 for letter in letters}
    for letter in string:
        dic[letter] += 1
    arr = [dic[letter] for letter in letters]
    arr.sort()
    currentmin = float('inf')
    for i in range(length // 26, length + 1):
        if i == 0:
            continue
        if length % i == 0 and i != 0:
            currentmin = min(currentmin, find(arr, i))
    print(int(currentmin))
