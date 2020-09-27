import premierleague

premierleague.start()
next_matches = premierleague.scrap_upcoming_fixures()
print(premierleague.scrap_match_page(next_matches[1]))

