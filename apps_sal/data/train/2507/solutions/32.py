import copy


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        tracker = dict()
        result = 0
        for s in chars:
            tracker.setdefault(s, 0)
            tracker[s] += 1
        for word in words:
            _temp = copy.deepcopy(tracker)
            for ch in word:
                if ch not in _temp:
                    break
                if _temp[ch] <= 0:
                    break
                _temp[ch] -= 1
            else:
                result += len(word)
        return result
