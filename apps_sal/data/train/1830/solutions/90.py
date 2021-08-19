class Solution:

    def backtrack(self, rains, full, position, seq):
        if position >= len(rains):
            return True
        if rains[position] > 0:
            if rains[position] in full:
                return False
            seq.append(-1)
            full.add(rains[position])
            if self.backtrack(rains, full, position + 1, seq):
                return True
            full.remove(rains[position])
            seq.pop()
        elif rains[position] == 0:
            # must choose one lake that is full to dry
            for lake in full:
                seq.append(lake)
                full.remove(lake)
                if self.backtrack(rains, full, position + 1, seq):
                    return True
                full.add(lake)
                seq.pop()
            if len(full) < 1:
                seq.append(1)  # random lake
                if self.backtrack(rains, full, position + 1, seq):
                    return True
                seq.pop()

    def avoidFloodBacktrack(self, rains: List[int]) -> List[int]:
        seq = []
        full = set()
        if not self.backtrack(rains, full, 0, seq):
            return []
        return seq

    def avoidFlood(self, rains: List[int]) -> List[int]:
        spares = []
        recent = dict()
        full = set()
        ans = []
        for i in range(len(rains)):
            if rains[i] > 0:
                ans.append(-1)
                if rains[i] in full:
                    # we need to have dried this lake for sure
                    valid = False
                    for d in range(len(spares)):
                        dry = spares[d]
                        if dry > recent[rains[i]]:
                            ans[dry] = rains[i]
                            full.remove(rains[i])
                            del spares[d]
                            valid = True
                            break
                    if not valid:
                        return []
                elif rains[i] in recent and recent[rains[i]] == i - 1:
                    # no chance to dry this one
                    return []
                else:
                    full.add(rains[i])
                recent[rains[i]] = i
            else:
                # we can dry one lake
                # greedy chooses some random lake
                # that will be replaced if needed
                ans.append(1)
                spares.append(i)
        return ans


if False:
    assert Solution().avoidFlood([69, 0, 0, 0, 69]) == [-1, 69, 1, 1, -1]
    assert Solution().avoidFlood([1, 2, 0, 0, 2, 1]) == [-1, -1, 2, 1, -1, -1]
    assert Solution().avoidFlood([1, 2, 0, 1, 2]) == []
    assert Solution().avoidFlood([10, 20, 20]) == []
