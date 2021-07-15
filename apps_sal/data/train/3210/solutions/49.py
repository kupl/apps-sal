def get_strings(city):
    city=city.lower().strip()
    letters_count={}
    
    def star_print(int):
        star_string=""
        for i in range(int):
            star_string=star_string+"*"
        return star_string
    
    for letter in city:
        if letter.isalpha():  
            if letter in letters_count:
                letters_count[letter]=letters_count[letter]+1
            else:
                letters_count[letter]=1
                
    ans_string=""
    for items in letters_count:
        temp_string=str(items)+":"+star_print(letters_count[items])+","
        ans_string=ans_string+temp_string
    ans_string=ans_string[0:-1]
    return ans_string
