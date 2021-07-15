def my_languages(d):
    return [key for key,value in sorted(d.items(),key=lambda item:item[1],reverse=True) if value>=60]
