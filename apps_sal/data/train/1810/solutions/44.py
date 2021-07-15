class Solution:
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        result = list()
        dictionary = dict()

        for name in names:
            if (name not in dictionary.keys()):                
                dictionary.setdefault(name, 1)
                result.append(name)
            else:
                unique_name = name
                suffix_number = dictionary[name]

                while (unique_name in dictionary.keys()):
                    unique_name = name + \"(\" + str(suffix_number) + \")\"
                    suffix_number = suffix_number + 1
                    dictionary.update({name: suffix_number})
            
                dictionary.setdefault(unique_name, 1)
                result.append(unique_name)
                
        return result
        
