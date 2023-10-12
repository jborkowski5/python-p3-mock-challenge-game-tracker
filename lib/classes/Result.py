class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.game._results.append(self)
        self.game._players.append(self.player)

        self.player._results.append(self)
        self.player._games.append(self.game)

        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not hasattr(self, "_score"):
            if isinstance(score, int) and 1 <= score <= 5000:
                self._score = score
            else:
                print("Score cannot be changed after it is set")
        else:
            print("Score cannot be changed after it is set")

    @property 
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        from classes.Player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Invalid player")

    @property 
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        from classes.Game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Invalid game")              