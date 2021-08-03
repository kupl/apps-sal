class Solution:
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        result = list()
        dictionary = dict()

        # Iterate over names
        for name in names:
            
            # If name is not in the dictionary, then add it to the dictionary and append it to the results
            if (name not in dictionary.keys()):
                dictionary.setdefault(name, 1)
                result.append(name)

            # Otherwise, build a unique name, add the unique name to the dictionary, and update the suffix of the name.
            else:
                unique_name = name
                suffix_number = dictionary[name]

                while (unique_name in dictionary.keys()):
                    unique_name = name + \"(\" + str(suffix_number) + \")\"
                    suffix_number = suffix_number + 1
            
                dictionary.setdefault(unique_name, 1)
                dictionary.update({name: suffix_number})

                result.append(unique_name)
                
        return result
        
