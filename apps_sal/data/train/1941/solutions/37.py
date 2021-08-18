
def gist(word):
    ans = 0
    for ch in word:
        ans |= (1 << (ord(ch) - ord('a')))
    return ans


def subsets(arr, start=0, progress=0):
    if start == len(arr):
        yield progress
    else:
        yield from subsets(arr, start + 1, progress | arr[start])
        yield from subsets(arr, start + 1, progress)


def head_subsets(puzzle):
    bits = [gist(ch) for ch in puzzle]
    for mask in subsets(bits[1:]):
        yield mask | bits[0]


def count_solutions(words, puzzles):
    gist_count = {}
    for word in words:
        g = gist(word)
        gist_count.setdefault(g, 0)
        gist_count[g] += 1

    ans = []
    for puzzle in puzzles:
        count = sum(gist_count.get(g, 0) for g in head_subsets(puzzle))
        ans.append(count)

    return ans


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        return count_solutions(words, puzzles)
