class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = dict()
        for word in words:
            cur_d = self.d
            for ch in word[::-1]:
                if ch in cur_d:
                    cur_d = cur_d[ch]
                else:
                    cur_d[ch] = {}
                    cur_d = cur_d[ch]
            cur_d['end'] = True
        self.query_cache = ''

    def query(self, letter: str) -> bool:
        self.query_cache += letter
        cur_d = self.d
        for ch in self.query_cache[::-1]:
            if ch in cur_d:
                if cur_d[ch].get('end'):
                    return True
                cur_d = cur_d[ch]
            else:
                break
        return False
