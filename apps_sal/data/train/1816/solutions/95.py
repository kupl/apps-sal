class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        arr = sorted(zip(keyTime, keyName))
        rcd = defaultdict(deque)
        alert = set()
        # print(arr)
        for i in range(len(arr)):
            name = arr[i][1]
            hr, mi = arr[i][0].split(\":\")
            time = int(hr) * 60 + int(mi)
            
            rcd[name].append(time)
            while time - rcd[name][0] > 60 or time - rcd[name][0] < 0 or len(rcd[name]) > 3:
                    rcd[name].popleft()

            if len(rcd[name]) == 3:
                alert.add(name)
        
        return sorted(alert)
        
