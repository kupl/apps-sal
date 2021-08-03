from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.data_set,self.end_chars, self.start_chars, self.min_len, self.max_len = self._get_set_min_max_len(words)
        self.queue = list()
        
    
    @staticmethod
    def _get_set_min_max_len(words):
        data_set = set(words)
        min_len = 10000
        max_len = 0
        end_chrs = set()
        start_chrs = set()
        for w in words:
            min_len = min(min_len, len(w))
            max_len = max(max_len, len(w))
            end_chrs.add(w[-1])
            start_chrs.add(w[0])
        return data_set, end_chrs,start_chrs, min_len, max_len
    
    def check_if_word_exists(self):
        c_l = len(self.queue)
        start_idx = c_l - self.min_len
        if start_idx >= 0:
            c_w = \"\".join(self.queue[k] for k in range(start_idx+1, c_l))
            for i in range(start_idx, max(-1, c_l - self.max_len-1), -1):
                c_w = f\"{self.queue[i]}{c_w}\"
                if self.queue[i] not in self.start_chars:
                    continue
                if c_w in self.data_set:
                    return True
        else:
            return False
        

    def query(self, letter: str) -> bool:
        # if len(self.queue) >= self.max_len:
        #     self.queue.popleft()
        self.queue.append(letter)
        if letter in self.end_chars:
            return self.check_if_word_exists()
        else:
            return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
