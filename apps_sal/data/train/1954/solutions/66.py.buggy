class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        ##dp[i][state]: state: 0 ---- 2^n,  n = len(req_skills)
        ##dp[i][state] if state all included in people[i] --> dp[i-1][state]
        ##dp[i][state - subset] if subset in people[i] --> dp[i-1][state-subset] + 1
        \"\"\"
        m = len(req_skills)
        n = len(people)
        states = 1<<(m)
        skill_index = {}
        for i,skill in enumerate(req_skills):
            skill_index[skill] = i
        mypeople = []
        for p in people:
            myp = 0
            for skill in p:
                myp ^= (1 << skill_index[skill])
            mypeople.append(myp)
        
        dp = [float(\"inf\") for _ in range(states)]
        parent = [(-1, -1) for _ in range(states)]
        dp[0] = 0
        
        for i in range(n):
            skill = mypeople[i]
            if skill == 0:
                continue
            #for j in range(states)：
            #    if dp[i-1][j] != float(\"inf\"):
            #        dp[i][j] = dp[i-1][j]

            for j in range(states-1, -1, -1):
                if  dp[j] + 1 < dp[j|skill]:
                    dp[j | skill] = dp[j] + 1
                    parent[j | skill] = (j, i)
                    print(\"parent\", parent)
                if dp[i-1][j] + 1 < dp[i-1][j|skill] and dp[i-1][j] + 1 < dp[i][j|skill]:
                    parent[j|skill] = (j, i-1)
                dp[i][j|skill] = min(dp[i][j|skill], dp[i-1][j|skill], dp[i-1][j] + 1)
            print(i, dp)
                
        #print(\"dp\", dp)
        #print(\"parents\", parent)
        ans = []
        t = states - 1
        while t > 0:
            ans.append(parent[t][1])
            t = parent[t][0]
        print(\"ans\", ans)
        ans.reverse()
        return ans
        \"\"\"
        m, n = len(req_skills), len(people)
        key = {v:i for i,v in enumerate(req_skills)}
        #print(m, n, key)
        paths = {0: []} 
        for i, who in enumerate(people):
            his_skill = 0
            for skill in people[i]:
                if skill in key:
                    his_skill |= (1 << key[skill])
            
            for skills, path in list(paths.items()):
                new_skill = skills | his_skill
                if new_skill == skills: continue
                if new_skill not in paths or len(paths[new_skill]) > len(path) + 1:
                    paths[new_skill] = path + [i]
            #print(i, \"paths\", paths)
        return paths[(1 << m) - 1]
            
        
            
                
