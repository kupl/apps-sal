class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        rec = []
        # res = collections.defaultdict(int)
        res = {}
        
        for file in names :
            # for j in range(len(rec)) :
            #     if file == rec[j] :
            #         n = 1
            #         while file+'('+str(n)+')' in rec :
            #             n += 1
            #         file += '('+str(n)+')'        
            # rec.append(file)
            if file in res.keys() :
                n = res[file]
                tmp = file+'('+ str(n) +')'
                while tmp in res.keys() :
                    n += 1
                    tmp = file+'('+ str(n) +')'
                rec.append(tmp)
                res[tmp] = 1
                res[file] += 1
            else :
                res[file] = 1
                rec.append(file)
                    
        return rec
