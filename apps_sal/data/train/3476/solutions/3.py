def unlucky_number(n):
    return len([i for i in range(1,n+1) if(i%13==0 and str(i).count("4")==0 and str(i).count("7")==0)])+1
