class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Invalid username")        

    def results(self):
        return self._results

    def games_played(self):
        return list(set(self._games))

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        count = 0
        for result in self._results:
            if result.game == game:
                count += 1
        return count
    
    @classmethod
    def highest_scored(cls, game):
        best_player = None
        highest_average = 0

        for player in cls.all:
            if player.played_game(game):
                average = sum(result.score for result in player.results() if result.game == game) / player.num_times_played(game)
                if average > highest_average:
                    highest_average = average
                    best_player = player

        return best_player