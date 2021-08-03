#[] DP
#O(N * 2^R) N: number of people, R: number of skills
#f(i, S): the minimum people count to use first i people to fulfill state S
#state S is a binary set which is a combinations of skills
#f(N, all 1) = 0,  f(N, not all 1) = inf
#return f(-1, 0)
#f(i, S) = min( f(i+1, S) , 1+f(i+1, S + req_skill[i])
def memorized(f):
    memo = {}
    def helper(*arg):
        if arg not in memo:
            memo[arg] = f(*arg)
        return memo[arg]
    return helper
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N, MASK = len(people), (1 << len(req_skills))-1
        skill2id, child = {skill: i for i, skill in enumerate(req_skills)}, {}
        people = [sum(1 << skill2id[skill] for skill in skills) for skills in people]
        @memorized
        def dp(i: int, status: int) -> int:
            \"\"\"return the path to get into (i, status) node\"\"\"
            if i >= N:
                return [] if status == MASK else None
            not_choose, choose = dp(i+1, status), dp(i+1, status | people[i])
            if not_choose is not None and (choose is None or len(not_choose) <= len(choose) + 1):
                return not_choose
            else: #NOTE: handle the case that choose is None, too
                return choose + [i] if choose is not None else None
        return dp(-1, 0)
