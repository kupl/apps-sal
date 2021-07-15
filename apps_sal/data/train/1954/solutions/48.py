# 5.05
class Solution:
        
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dp={0:[]}
        reqSkills={v:k for k,v in enumerate(req_skills)}
        for i,curSkills in enumerate(people):
            curMask=0
            for skill in curSkills:
                curMask|=1<<reqSkills[skill]
            for mask,team in list(dp.items()):
                m=mask|curMask
                if m==mask:
                    continue
                if m not in dp or 1+len(team)<len(dp[m]):
                    dp[m]=team+[i]
        return dp[(1<<len(req_skills))-1]
                
# class Solution:
#     def __init__(self):
#         self.minCnt=math.inf
#         self.minTeam=[]
        
#     def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
#         skills,team,skillsets,pids=set(req_skills),set(),set(),[]
#         people
#         for i,p in enumerate(people):
#             p=frozenset(p)
#             if not p or p in skillsets:
#                 continue
#             skillsets.add(p)
#             pids.append(i)
            
#         def dfs(skills, team):
#             if len(team)>self.minCnt:
#                 return
#             if not skills and len(team)<self.minCnt:
#                 self.minCnt=len(team)
#                 self.minTeam=list(team)
#             ps=sorted(((p,skills.intersection(people[p])) for p in pids if p not in team),\\
#                       key=lambda x:len(x[1]),reverse=True)
#             for p,curSkills in ps:
#                 if not curSkills:
#                     break
#                 team.add(p)
#                 skills-=curSkills
#                 dfs(skills,team)
#                 team.remove(p)
#                 skills.update(curSkills)
#         dfs(skills,team)
#         return self.minTeam

