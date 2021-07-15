def gen_prefixes(s):
    ans = {0: [0]}
    parity = 0
    for (ind, ch) in enumerate(s):
        after = ind + 1
        parity ^= (1 << int(ch))
        ans.setdefault(parity, [])
        ans[parity].append(after)
    return ans

def get_awesomes(prefixes):
    ans = 1
    for A in prefixes:
        for xbit_ind in range(11):
            if xbit_ind == 10:
                B = A
            else:
                B = A ^ (1 << xbit_ind)
                if B not in prefixes:
                    continue
            pA, pB = prefixes[A], prefixes[B]
            ans = max(ans, max(pB) - min(pA))
            ans = max(ans, max(pA) - min(pB))
    return ans

class Solution:
    def longestAwesome(self, s: str) -> int:
        prefixes = gen_prefixes(s)
        return get_awesomes(prefixes)
