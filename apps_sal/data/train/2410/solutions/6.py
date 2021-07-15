class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if (len(typed) < len(name)):
            return False
        
        typed_index = 0
        
        
        for i in range(len(name)):
            if (typed_index >= len(typed)):
                return False
            elif (name[i] != typed[typed_index]):
                if (typed_index == 0 or typed[typed_index - 1] != typed[typed_index]):
                    return False
                else:
                    letter = typed[typed_index]
                    
                    
                    while (typed_index < len(typed) and typed[typed_index] == letter):
                        typed_index += 1
                        
                        
                    if (typed_index == len(typed) or typed[typed_index] != name[i]):
                        return False
            else:
                pass
            
            typed_index += 1
            
        
        if (typed_index < len(typed) and (typed[typed_index - 1] != typed[typed_index] or typed[typed_index:].count(typed[typed_index]) != len(typed) - typed_index)):
            return False
        
        return True
