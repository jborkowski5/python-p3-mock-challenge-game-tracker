class Game:

    all = []

    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception("must be str over 0 characters")


    def results(self):
        return self._results

    def players(self):
        return list(set(self._players))

    def average_score(self, player):
        player_results = [result for result in self._results if result.player == player]
        if not player_results:
            return 0
        return sum(result.score for result in player_results) / len(player_results)