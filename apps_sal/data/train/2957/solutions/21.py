KNOWN_DRINK_PREFERENCES = { "zaphod beeblebrox" : "Intergalactic Gargle-Blaster",
                            "school counselor"  :        "Anything with Alcohol",
                            "programmer"        :           "Hipster Craft Beer",
                            "politician"        :             "Your tax dollars",             
                            "jabroni"           :               "Patron Tequila",
                            "bike gang member"  :                    "Moonshine",
                            "rapper"            :                      "Cristal",
                            "nero"              :                         "Wine" }

get_drink_by_profession = lambda p: KNOWN_DRINK_PREFERENCES.get(p.lower(), "Beer")
