from player import Player


class Club:
    def __init__(self, name, budget=500):
        self.name = name
        self.budget = budget

        self.players = []

        # Season Statistics
        self.played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

        # Club Records
        self.trophies = 0

    # -----------------------
    # Squad Management
    # -----------------------

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_id):

        for player in self.players:

            if player.id == player_id:
                self.players.remove(player)
                return True

        return False

    def find_player(self, player_id):

        for player in self.players:

            if player.id == player_id:
                return player

        return None

    # -----------------------
    # Transfers
    # -----------------------

    def buy_player(self, player):

        if self.budget >= player.value:

            self.players.append(player)

            self.budget -= player.value

            return True

        return False


    def sell_player(self, player_id):

        player = self.find_player(player_id)

        if player:

            self.players.remove(player)

            self.budget += player.value

            return True

        return False

    # -----------------------
    # Statistics
    # -----------------------

    def squad_size(self):
        return len(self.players)

    def average_rating(self):

        if len(self.players) == 0:
            return 0

        total = sum(player.rating for player in self.players)

        return round(total / len(self.players), 1)

    # -----------------------
    # Matches
    # -----------------------

    def record_match(self, goals_for, goals_against):

        self.played += 1

        self.goals_for += goals_for
        self.goals_against += goals_against

        if goals_for > goals_against:

            self.wins += 1
            self.points += 3

        elif goals_for == goals_against:

            self.draws += 1
            self.points += 1

        else:

            self.losses += 1

    # -----------------------
    # Dashboard
    # -----------------------

    def summary(self):

        return {
            "club": self.name,
            "budget": self.budget,
            "players": self.squad_size(),
            "average_rating": self.average_rating(),
            "points": self.points
        }
