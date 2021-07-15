def to_freud(sentence):
    arr=sentence.split(" ")
    for i in range(0,len(arr)):
        arr[i]="sex"
    return " ".join(arr)
