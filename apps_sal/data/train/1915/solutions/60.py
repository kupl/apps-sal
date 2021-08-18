'''
\"aabcaca\"
 0123456
  x
 
matched = [set() for _ in range(M-N)]

que = [1]
for window_start in range(i - n + 1, i + n):
    for j in range(i, i+n):
        todo[window_start].discard(j)
        if canMatch(todo[window_start]):
            que.append(window_start)
'''


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        '''greedy. everytime put the totally matched window to the que
            then update the windows that are affected
            then if updated window is totally matched, append to que.
            keep doing it.
        '''

        M = len(stamp)
        N = len(target)
        nwin = N - M + 1
        matched = [set() for _ in range(nwin)]
        done = set()

        for win_start in range(nwin):
            for i, (c1, c2) in enumerate(zip(target[win_start: win_start + M], stamp)):
                if c1 == c2:
                    matched[win_start].add(i + win_start)

        res = []
        que = deque()
        for win_start in range(nwin):
            if len(matched[win_start]) == M:
                que.append(win_start)
                res.append(win_start)
                done.add(win_start)

        while que:
            win_start = que.popleft()

            for nws in range(max(0, win_start - M + 1), min(nwin, win_start + M)):
                if nws in done:
                    continue
                for pos in range(win_start, win_start + M):
                    if nws <= pos < nws + M:
                        matched[nws].add(pos)

                if len(matched[nws]) == M:
                    que.append(nws)
                    done.add(nws)
                    res.append(nws)

        return res[::-1] if all([d in done for d in range(nwin)]) else []
