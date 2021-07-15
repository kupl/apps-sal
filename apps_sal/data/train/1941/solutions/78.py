from collections import defaultdict
from typing import List


def get_encode(word, letters):
    encode = ['0'] * 26
    for c in word:
        idx = letters.index(c)
        encode[idx] = '1'
    return ''.join(encode)


def dfs(encode, cur, sub_encodes):
    if cur == len(encode):
        sub_encodes.add(encode)
        return
    elif encode[cur] == '1':
        sub_zero = encode[:cur] + '0' + encode[cur+1:]
        sub_one = encode[:cur] + '1' + encode[cur+1:]
        sub_encodes.add(sub_zero)
        sub_encodes.add(sub_one)
        dfs(sub_zero, cur+1, sub_encodes)
        dfs(sub_one, cur+1, sub_encodes)
    else:
        dfs(encode, cur+1, sub_encodes)


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        records = defaultdict(int)
        for word in words:
            encode = get_encode(word, letters)
            records[encode] += 1

        results = []
        for puzzle in puzzles:
            encode, cur, idx_first = get_encode(puzzle, letters), 0, letters.index(puzzle[0])
            sub_encodes = {encode}
            dfs(encode, cur, sub_encodes)
            result = sum([records[sub_encode] for sub_encode in list(sub_encodes) if sub_encode[idx_first] == '1'])
            results.append(result)
        return results

