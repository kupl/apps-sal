def solve(files):
    hashMap = {}
    mostCommon = []
    maxCount = 1
    for file in files:
        ext = file[file.rfind('.'):]
        count = hashMap[ext] = hashMap.get(ext, 0) + 1
        if maxCount < count:
            maxCount = count
            mostCommon = [ext]
        elif maxCount == count:
            mostCommon.append(ext)
    mostCommon.sort()
    return mostCommon
