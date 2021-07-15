class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        my_list = [[time,name]for name,time in zip(keyName,keyTime)]
        def my_func(str1):
            total = 0
            l1 = str1[0].split(\":\")
            min1 = int(l1[0])
            min2 = int(l1[1])
            total = min1*60
            total += min2
            return total
        
        my_list.sort(key = my_func)
        #print(my_list)
        out = set()
        def find_minutes(str1,str2):
            l1 = str1.split(\":\")
            l2 = str2.split(\":\")
            total = 0
            if int(l1[0])>int(l2[0]):
                return 100
            total += (int(l2[0])-int(l1[0]))*60
            min1 = int(l1[1])
            min2 = int(l2[1])
            if min2 < min1:
                total -= min1-min2
            else:
                total += min2-min1
            return total
        #hashed = {}
        card_use = collections.defaultdict(list)
        
        for time,name in my_list:
            if name not in card_use:
                card_use[name].append(time)
            else:
                while card_use[name] and find_minutes(card_use[name][0],time) > 60:
                    card_use[name].pop(0)
                card_use[name].append(time)
                if len(card_use[name]) >= 3:
                    out.add(name)
            #print(card_use)
            #print(out)
        out =  list(out)
        out.sort()
        return out
            # print(f\"{name} {time}\")
            # if name in hashed:
            #     print(f\"hashed[name] {hashed[name]}\")
            #     if find_minutes(hashed[name],time) <= 60:
            #         card_use[name] += 1
            #         if alert[name] >= 3:
            #             out.append(name)
            # print(alert)
            # hashed[name] = time
                
            
        #print(find_minutes(\"09:10\",\"10:30\"))
        return out
        
