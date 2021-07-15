from datetime import date, timedelta    

def calc(y):

    st  = date(y, 1, 1)
    fin = date(y, 12, 31)
    numday = timedelta(days=1)
    while st < fin:
        if st.weekday() == 4 and st.day == 13:
             yield st
        st = st + numday
        
    
def unlucky_days(year):
    count = 0
    res = [str(i) for y in range(year - 1,year + 1) for i in calc(y)]
    for x in range(len(res)):
        if str(year) in res[x]:
            count = count + 1
    return count

