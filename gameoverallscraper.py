import premierleague
import fifaoverallscraper


def replace_names_to_overalls(team_vector):
    for i in range(len(team_vector)):
        if team_vector[i] != "0":
            try:
                overall = fifaoverallscraper.scrap_player_overall(team_vector[i], 13)
                print(team_vector[i] + " [Overall: " + str(overall) + "]")
                team_vector[i] = overall
            except fifaoverallscraper.NotSinglePlayerFoundException as err:
                print("Player not found: " + str(team_vector[i]) + "\nOverall? ")
                team_vector[i] = int(input())
        else:
            team_vector[i] = 0


def scrap_game_vector(game_url):
    premierleague.start()
    game = premierleague.scrap_match_page(game_url)

    print("=== Home Team: " + game["Home Team"] + " ===")
    replace_names_to_overalls(game["Home Vector"])
    print()

    print("=== Away Team: " + game["Away Team"] + " ===")
    replace_names_to_overalls(game["Away Vector"])
    print()

    return game["Home Vector"] + game["Away Vector"]
