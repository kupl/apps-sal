date_checker=lambda s:bool(__import__('re').match('\d\d-\d\d-\d{4} \d\d:\d\d',s))
