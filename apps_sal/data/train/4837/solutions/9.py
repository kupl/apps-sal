isodays=['SUN','MON','TUE','WED','THU','FRI','SAT']
isomonths=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
def checkIso(start,end):
    if start in isodays:
        return str(isodays.index(start)),str(isodays.index(end))
    if start in isomonths:
        return str(isomonths.index(start)+1),str(isomonths.index(end)+1)
    return start,end

def parseitem(itempart):
    itemnums=list()
    period,item,minmax = itempart
    for i in item.split(','):
    
        if i.isnumeric():
            itemnums.append(int(i))
            continue

        if i.find('-')>-1:
            rangsplit=i.split('-') 
            step=1
            start=rangsplit[0]
            end=rangsplit[1]
            if rangsplit[1].find('/')>-1:
                step=int(rangsplit[1].split('/')[1])         
                end=rangsplit[1].split('/')[0]
            start,end=checkIso(start,end)
            itemnums.extend(range(int(start),int(end)+1,step))
            continue
        if i.find('*')>-1:
            step=1
            if i.find('/')>-1:
                step=int(i.split('/')[1])
            itemnums.extend(range(minmax[0],minmax[1]+1,step))
            continue

    itemnums.sort()    
    return period.ljust(15)+' '.join([ str(x) for x in itemnums ])



def parse(crontab):
    periods=['minute','hour','day of month','month','day of week']
    periodminmax=[[0,59],[0,23],[1,31],[1,12],[0,6]]
    zipped=list(zip(periods,crontab.split(' '),periodminmax))
    return '\n'.join([ parseitem(x) for x in zipped ])
