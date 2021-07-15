from collections import defaultdict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_dic = defaultdict(int)
        out = []
        for name in names:
            if name not in name_dic:
                #print(name)
                name_dic[name] += 1
                out.append(name)
            else:
                #print(name)
                postfix = \"(\"+ str(name_dic[name]) + \")\"
                while name + postfix in name_dic:
                    postfix = \"(\" + str(int(postfix[1:-1]) + 1) + \")\"
                name_dic[name] = int(postfix[1:-1]) + 1
                name_dic[name + postfix] += 1
                out.append(name + postfix)
        #print(name_dic)
        return out
                
            
