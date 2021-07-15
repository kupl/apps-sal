class Solution:
    def peopleIndexes(self, favorite_companies: List[List[str]]) -> List[int]:
        company_set_per_person = []
        for i, company_list in enumerate(favorite_companies):
            company_set = set(company_list)
            found = False
            for j, (other_company_set, k) in enumerate(company_set_per_person):
                if company_set >= other_company_set:
                    company_set_per_person[j] = (company_set, i)
                    found = True
                    break
                if company_set <= other_company_set:
                    found = True
                    break
            if not found:
                company_set_per_person.append((company_set, i))
        
        # print(company_set_per_person)
        
        ans = []
        for i, company_list in enumerate(favorite_companies):
            company_set = set(company_list)
            found = False
            for other_company_set, j in company_set_per_person:
                if company_set <= other_company_set and i != j:
                    found = True
                    break
            if not found:
                ans.append(i)
        return ans
