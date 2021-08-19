import sys


class Directions:
    ReversedDirections = []
    ReversedDirLines = []

    def __init__(self, dirLines, directions):
        self.DirLines = dirLines
        self.Directions = directions


def FormReversedDirLines(d):
    i = -1
    j = 0
    ReversedDirLines = []
    while i >= -1 * len(d.DirLines):
        direction = d.ReversedDirections[j]
        t = ' '.join(d.DirLines[i].split()[1:])
        ReversedDirLines.append(direction + ' ' + t)
        i = i - 1
        j = j + 1
    return ReversedDirLines


def CorrectDirections(directions):
    correctedDirs = [directions[0]]
    for d in directions[1:]:
        if d == 'Right':
            correctedDirs.append('Left')
        else:
            correctedDirs.append('Right')
    return correctedDirs


def Reverse(l):
    newL = []
    i = -1
    while i >= -1 * len(l):
        newL.append(l[i])
        i = i - 1
    return newL


def RightCircularShift(l):
    newL = l[1:]
    newL.append(l[0])
    return newL


def ReverseDirections(Directions):
    rShiftDirs = RightCircularShift(Directions)
    reverse = Reverse(rShiftDirs)
    reverse = CorrectDirections(reverse)
    return reverse


def WriteOutput(fPath, output):
    f = open(fPath, 'w')
    for d in output:
        f.writelines(d.ReversedDirLines)
        f.write('\n')
    f.close()


def WriteOutputToConsole(output):
    for d in output:
        for l in d.ReversedDirLines:
            print(l)
        print('')


def GetDirectionsFromLines(lines):
    directions = []
    for l in lines:
        directions.append(l.split()[0])
    return directions


def ReadInputFromConsole():
    lines = []
    k = input()
    while k != '':
        lines.append(k)
        k = input()
    return ParseInput(lines)


def ParseInput(lines):
    nCases = int(lines[0])
    parsedLines = []
    prev = 0
    i = 0
    while i < nCases:
        numLineIndex = prev + 1
        nDirLines = int(lines[numLineIndex])
        parsedLines.append(lines[numLineIndex + 1:numLineIndex + 1 + nDirLines])
        i = i + 1
        prev = prev + 1 + nDirLines
    inputDirs = []
    for p in parsedLines:
        dirLines = p
        directions = GetDirectionsFromLines(p)
        inputDirs.append(Directions(dirLines, directions))
    return inputDirs


def ReadInput(fPath):
    f = open(fPath, 'r')
    lines = f.readlines()
    f.close()
    return ParseInput(lines)


def __starting_point():
    directions = ParseInput(sys.stdin.readlines())
    for d in directions:
        d.ReversedDirections = ReverseDirections(d.Directions)
        d.ReversedDirLines = FormReversedDirLines(d)
    WriteOutputToConsole(directions)


__starting_point()
