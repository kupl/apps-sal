import base64

def adFly_decoder(sc):
    #your code here
    try:
        code1 = sc[::2]
        code2 = sc[1::2]
        code2 = code2[::-1]    # reverse
        decode_adfly = base64.b64decode(code1 + code2).decode("utf-8") 
        encoded_url = decode_adfly.split("https://adf.ly/go.php?u=")[-1]
        return base64.b64decode(encoded_url).decode("utf-8") 
    except:
        return "Invalid"
    
def adFly_encoder(url):
    #your code here
    code = base64.b64encode(url.encode()).decode("utf-8")
    ad_fly_code = "12https://adf.ly/go.php?u=" + code
    final_code = base64.b64encode(ad_fly_code.encode()).decode("utf-8")
    
    l = len(final_code)
    half = l // 2
    first_half = final_code[0:half] 
    second_half = final_code[half if l % 2 == 0 else half+1:] 
    
    second_half = second_half[::-1]
    result_string = ""
    
    for i in range(half):
        result_string += first_half[i]
        if i < half - 1 or l % 2 == 0:
            result_string += second_half[i]
            
    return result_string
    

