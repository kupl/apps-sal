class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        if len(favoriteCompanies) == 0:
            return []
        answer = []
        listOfSets = [[set(favoriteCompanies[index]), index] for index in range(len(favoriteCompanies))]
        listOfSets.sort(key=lambda pair: len(pair[0]))
        print(listOfSets)
        for i in range(len(listOfSets)):
            subset = False
            for j in range(i + 1, len(listOfSets)):
                # print(f\"current {listOfSets[i][0]} subset of {listOfSets[j][0]}\")
                if listOfSets[i][0].issubset(listOfSets[j][0]):
                    subset = True
                    # print(\"Found subset\")
                    break
            if subset == False:
                answer.append(listOfSets[i][1])
        answer.sort()
        return answer
