class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.nums = [i for i in range(combinationLength)]
        self.characters = characters
        self.s = len(characters)
        self.len = combinationLength
        self.is_next = True

    def __next__(self) -> str:
        ret = ''
        for n in self.nums:
            ret += self.characters[n]
        self.nums[-1] += 1
        if self.nums[-1] == self.s:
            carry = True
            cnt = -2
            while carry and cnt >= -self.len:
                self.nums[cnt] += 1
                if self.nums[cnt] > self.s + cnt:
                    carry = True
                    cnt -= 1
                else:
                    carry = False
            if cnt < -self.len:
                self.is_next = False
            else:
                for i in range(cnt + 1, 0, 1):
                    self.nums[i] = self.nums[i - 1] + 1
        return ret

    def hasNext(self) -> bool:
        return self.is_next
