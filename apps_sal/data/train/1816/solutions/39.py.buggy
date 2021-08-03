class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        people = []
        
        rec_tries = {}
        
        queue = deque()

        
        for user, time in sorted(zip(keyName, keyTime), key = lambda x:x[1]):
            time = time.split(\":\")
            mins = int(time[0]) * 60 + int(time[1])
            queue.append((user, mins))
                
            
            while queue[0][1] < mins - 60:
                to_rem = queue.popleft()
            
                rec_tries[to_rem[0]] -= 1
                    
            if user in rec_tries:
                rec_tries[user] += 1
            else:
                rec_tries[user] = 1
                
            if rec_tries[user] >= 3:
                people.append(user)
                rec_tries[user] = -inf
                    
        return sorted(people)
