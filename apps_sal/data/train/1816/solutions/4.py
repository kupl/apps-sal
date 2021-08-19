class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        dictTime = collections.defaultdict(list)
        setName = set()
        for x, y in zip(keyName, keyTime):
            dictTime[x].append(y)
            setName.add(x)

        listName = list(setName)
        listName.sort()
        for key in dictTime:
            dictTime[key].sort()

        print(dictTime)

        out = []
        for name in listName:
            listT = dictTime[name]
            if len(listT) >= 3:
                start = 0
                end = 2
                condit = False
                while end < len(listT):
                    # print(listT[start][:2],listT[end][:2])
                    # print(listT[start][3:],listT[end][3:])
                    # print(int(listT[start][:2])+1 == int(listT[end][:2]) )
                    # print(int(listT[start][3:]) <= int(listT[end][3:]))

                    if int(listT[start][:2]) == int(listT[end][:2]):
                        condit = True
                        break

                    if (int(listT[start][:2]) + 1 == int(listT[end][:2]) and int(listT[start][3:]) >= int(listT[end][3:])):
                        # print('ciao')
                        condit = True
                        break

                    start += 1
                    end = start + 2
                if condit:
                    out.append(name)
        return out
