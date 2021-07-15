def count_positives_sum_negatives(arr):
    count=0
    suma=0
    if arr==[]:
        return []
    else:
    
        for number in arr:
            if number>0:
                count=count+1
            elif number<=0:
                suma=suma+number
        return [count,suma]

