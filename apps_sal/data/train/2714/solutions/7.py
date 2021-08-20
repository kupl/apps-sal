def bucket_of(said):
    (water_list, slime_list) = (['water', 'wet', 'wash'], ["i don't know", 'slime'])
    s = said.lower()
    water = any((w in s for w in water_list))
    slime = any((sl in s for sl in slime_list))
    return 'sludge' if water and slime else 'water' if water else 'slime' if slime else 'air'
