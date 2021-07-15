class Solution:            
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        l = len(req_skills)
        index_dict = {item : i for i, item in enumerate(req_skills)}
        mydict = {0 : []}
        for i, person in enumerate(people):
            skill_list = ['0']*l
            for skill in person:
                index = index_dict[skill]
                skill_list[index] = '1'
            num = int(''.join(skill_list), 2)
            new_dict = {key: list(item) for key, item in list(mydict.items())}
            for key in list(mydict.keys()):
                new_num = key | num
                if new_num in new_dict:
                    if len(new_dict[new_num]) > 1 + len(mydict[key]):
                        new_dict[new_num] = mydict[key] + [i,]
                else:
                    new_dict[new_num] = mydict[key] + [i,]
            mydict = new_dict
        return mydict[2**l-1]
                                    
            
                

