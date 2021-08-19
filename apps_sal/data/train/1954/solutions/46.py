class Solution:

    def smallestSufficientTeam(self, req_skills, people):
        (countReqSkills, memo) = (len(req_skills), {0: []})
        skillToIndex = {v: i for (i, v) in enumerate(req_skills)}
        for (i, ithSkills) in enumerate(people):
            ithSkillsBitmap = 0
            for skill in ithSkills:
                ithSkillsBitmap |= 1 << skillToIndex[skill]
            for (skillsBitmap, reqPpl) in list(memo.items()):
                skillsBitmapAddI = skillsBitmap | ithSkillsBitmap
                if skillsBitmapAddI == skillsBitmap:
                    continue
                if skillsBitmapAddI not in memo or len(reqPpl) + 1 < len(memo[skillsBitmapAddI]):
                    memo[skillsBitmapAddI] = reqPpl + [i]
        return memo[(1 << countReqSkills) - 1]
