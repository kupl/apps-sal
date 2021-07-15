class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        created_fld = set()
        result_set = []
        for i,name in enumerate(names):
            if name not in created_fld:
                created_fld.add(name)
                result_set.append(name)
            else:
                j = 1
                new_name = f'{name}({j})'
                while new_name in created_fld:
                    j+=1
                    new_name = f'{name}({j})'
                created_fld.add(new_name)
                result_set.append(new_name)
        return result_set

