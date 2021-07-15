class Solution:
    
    def generateUniqueFolderName(self, name: str, dictionary: dict) -> str:

        result = name
        
        if (name not in dictionary.keys()):
            dictionary.setdefault(result, 1)
            
        else:
            suffix_number = dictionary[name]

            while (result in dictionary.keys()):
                result = name + \"(\" + str(suffix_number) + \")\"
                suffix_number = suffix_number + 1
            
            dictionary.update({result: 1})
            dictionary.update({name: suffix_number})
            
        return result
    
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        result = list()
        dictionary = dict()

        # Iterate over names
        for name in names:
            
            unique_name = self.generateUniqueFolderName(name, dictionary)
            
            result.append(unique_name)

                
        return result
        
