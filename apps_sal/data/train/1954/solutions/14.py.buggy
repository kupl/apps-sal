class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = dict(zip(req_skills,list(range(len(req_skills)))))
        target = (1<<len(req_skills))-1
        for p in range(len(people)):
            temp = 0
            for s in people[p]:
                temp |= (1<<skills[s])
            people[p] = temp
            
        \"\"\"
        dp[i][j]: min people to have skills of j using first i people
        dp[0][0] = 0
        dp[i][j][k] = min(dp[i-1][j][k],dp[i-1][j]+1)
        
        \"\"\"
        
        dp = [[float(\"inf\"),[]] for _ in range(1+target)]
        dp[0] = (0,[])
        
        for r in range(len(people)):
            for c in range(target,-1,-1):
                #print(dp)
                if dp[c][0] != float(\"inf\"):
                    if dp[c][0]+1<dp[c|people[r]][0]:
                        dp[c|people[r]][0] = dp[c][0]+1
                        dp[c|people[r]][1] = dp[c][1]+[r]
        return dp[-1][1]
        
        
        
            
            
