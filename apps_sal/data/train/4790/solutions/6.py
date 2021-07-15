import math
def clean_mean(sample, cutoff):
    print(sample, cutoff)
    while True:
        a=len(sample)
        total=sum(sample)
        mean=total/len(sample)
        new_list=[(i-mean)**2 for i in sample]
        total_new_list=sum(new_list)
        sd=math.sqrt(total_new_list/len(sample))
        sample=[i for i in sample if i<cutoff*sd+mean and i>mean-cutoff*sd]
        if a==len(sample):
            break
    print (round(mean,2))
    return round(mean,2)
