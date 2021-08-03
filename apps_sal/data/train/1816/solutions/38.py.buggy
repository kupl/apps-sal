class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        data = {user:[] for user in set(keyName)}
        result = set()
        for user, time in zip(keyName, keyTime):
            hour, minute = tuple(map(int, time.split(\":\")))
            time = 60*hour+minute
            data[user].append(time)
        
        data = {user: sorted(data[user]) for user in data}
    
        for user in data:
            for i in range(2, len(data[user])):
                if data[user][i]-data[user][i-2] <= 60:
                    result.add(user)
                    break;
                    
        
        return sorted(result)
            
            
        
