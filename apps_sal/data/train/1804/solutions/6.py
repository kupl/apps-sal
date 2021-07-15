def recoverSecret(triplets):
    ansList = list({triplet[i] for i in range(3) for triplet in triplets})
    indexDict = {letter:i for i,letter in enumerate(ansList)}
    
    isModified = True
    while isModified:
        isModified = False
        for triplet in triplets:
            for i in range(2):
                if indexDict[ triplet[i] ] > indexDict[ triplet[i+1] ]:
                    isModified = True
                    indexDict[ triplet[i] ], indexDict[ triplet[i+1] ] = indexDict[ triplet[i+1] ], indexDict[ triplet[i] ]
    
    for k in indexDict.keys(): ansList[ indexDict[k] ] = k
    return ''.join(ansList)
