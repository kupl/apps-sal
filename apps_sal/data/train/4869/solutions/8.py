import json


def isItAChainOfSons(listOfCildren):
    chainOfSons = True
    for i in range(0, 7):
        if listOfCildren[i]['gender'] == 'female':
            chainOfSons = False
    return chainOfSons


def rekursiveSonFinder(family, secondGeneration):
    if family['gender'] == 'female' or len(family['children']) < 7:
        return '/'
    elif isItAChainOfSons(family['children']):
        if secondGeneration:
            return '/' + family['children'][6]['name']
        else:
            return rekursiveSonFinder(family['children'][6], True)


def rekursiveIteration(family):
    if len(family['children']) == 0:
        return '/'
    else:
        ownSolution = rekursiveSonFinder(family, False)
        solutionOfChildren = ''
        for child in family['children']:
            if len(child['children']) > 0:
                solutionOfChildren = solutionOfChildren + rekursiveIteration(child)
        if ownSolution == None:
            return solutionOfChildren
        else:
            return ownSolution + solutionOfChildren


def find_seventh_sons_of_seventh_sons(jstring):
    familyTree = json.loads(jstring)
    listOfSons = rekursiveIteration(familyTree)
    listOfSons = listOfSons.split('/')
    solution = set()
    for name in listOfSons:
        if name != '':
            solution.add(name)
    return solution
