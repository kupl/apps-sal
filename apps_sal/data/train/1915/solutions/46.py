class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        tl,sl = len(target),len(stamp)
        t,s = list(target),list(stamp)
        res = []
        def check(i):
            signal = False
            for j in range(sl):
                if t[i+j] == '?':continue
                if t[i+j] != s[j]:return False
                signal = True
            if signal:
                t[i:i+sl] = ['?']*sl
                res.append(i)
            return signal
        signal = True
        while signal:
            signal = False
            for i in range(tl-sl+1):
                signal = signal | check(i)
        return res[::-1] if t == ['?']*tl else []

