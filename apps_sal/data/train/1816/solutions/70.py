class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        data = defaultdict(list)
        for t, n in zip(keyTime, keyName):
            data[n].append(t)
        ans = set()
        for name, time in data.items():
            count = 0
            left = 0
            time = sorted(time)
            #print(f\"name {name}\")
            for i, t in enumerate(time):
                #print(f\"t {t}\")
                hour = int(t.split(':')[0])
                minute = int(t.split(':')[1])
                prev_t = time[left]
                prev_h = int(prev_t.split(':')[0])
                prev_m = int(prev_t.split(':')[1])
                while (h_diff := hour - prev_h) > 1 or (h_diff == 1 and prev_m < minute):
                    left += 1
                    prev_t = time[left]
                    prev_h = int(prev_t.split(':')[0])
                    prev_m = int(prev_t.split(':')[1])
                if i - left >= 2:
                    print(f\"i {i}, left {left}\")
                    ans.add(name)
                    break
        return sorted(ans)
