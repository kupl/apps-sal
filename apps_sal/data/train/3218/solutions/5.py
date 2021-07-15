def SJF(jobs, index):
    return sum(list(filter(lambda x: x<jobs[index],jobs)))+sum(list(filter(lambda x: x==jobs[index], jobs[0:index+1])))
