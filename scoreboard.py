import requests


class ScoreBoard:
    def __init__(self):
        self.scoreboard = {}

    def get_leader_board(self):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        sorted_players = sorted(data[''])
        pass

    def get_players(self, game):
        data = requests.get("https://store.ncss.cloud/group2/jamescurrancyapi").json()
        for player in data:
            if game in data[player]['score']:
                self.scoreboard[player] = data[player]['score'][game]
            else:
                self.scoreboard[player] = 0

        sorted_players = dict(sorted(self.scoreboard.items(), key=lambda item: item[1], reverse=True))
        
        return sorted_players
