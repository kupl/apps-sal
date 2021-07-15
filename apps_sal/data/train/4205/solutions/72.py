cannons_ready = lambda gunners: 'Fire!' if all(i == 'aye' for i in gunners.values()) else 'Shiver me timbers!'
