class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        def check_equal(sub_string):
            
            for c1, c2 in zip(list(sub_string), list(stamp)):
                if c1 != \"?\" and c1 != c2:
                    return False
            return True
                
        stamp_length = len(stamp)
        end_result = \"?\" * len(target)
        no_check_string = \"?\" * stamp_length

        res = []
        for _ in range(10 * len(target)):
            found = False
            for ti in range(len(target) - stamp_length + 1):
                sub_string = target[ti:ti+stamp_length]
                # print(sub_string)
                if sub_string == no_check_string:
                    continue
                if check_equal(sub_string):
                    target = target[:ti] + no_check_string + target[ti + stamp_length:]
                    found = True
                    res += [ti]
                    break
            
            if found:
                if target == end_result:
                    return res[::-1]
            
            else:
                return []
            
        return []
                
            
            
            
            
            
        
