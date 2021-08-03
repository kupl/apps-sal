class Solution:
    def smallestSufficientTeam(self,
                               req_skills: List[str],
                               people: List[List[str]]) -> List[int]:

        N = len(req_skills)
        P = len(people)

        skill_id_map = {skill: idx for idx, skill in enumerate(req_skills)}

        def get_ssid(skills):
            ssid = 0
            for skill in skills:
                idx = skill_id_map[skill]
                ssid |= (1 << idx)
            return ssid

        people_ssid_map = {
            idx: get_ssid(skills) for idx, skills in enumerate(people)
        }

        dpv = [sys.maxsize] * (2**N)
        dpv[0] = 0
        dps = [[] for _ in range(2**N)]

        for ssid in range(2**N):
            if dpv[ssid] == sys.maxsize:
                continue
            for peepsid in range(P):
                skillset_id = people_ssid_map[peepsid]

                new_ssid = (ssid | skillset_id)
                if new_ssid != ssid:
                    if 1 + dpv[ssid] < dpv[new_ssid]:
                        dpv[new_ssid] = 1 + dpv[ssid]
                        dps[new_ssid] = dps[ssid] + [peepsid]

        # print(dpv)

        return dps[(2**N) - 1]
