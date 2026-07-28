class Player:
    next_id = 1

    def __init__(self, name, position, rating,
                 age=18, nationality="Unknown",
                 value=1000000):

        self.id = Player.next_id
        Player.next_id += 1

        self.name = name
        self.position = position
        self.rating = rating
        self.age = age
        self.nationality = nationality
        self.value = value

        self.goals = 0
        self.assists = 0
        self.matches = 0
        self.yellow_cards = 0
        self.red_cards = 0

    def score_goal(self):
        self.goals += 1

    def make_assist(self):
        self.assists += 1

    def play_match(self):
        self.matches += 1

    def receive_yellow(self):
        self.yellow_cards += 1

    def receive_red(self):
        self.red_cards += 1

    def display(self):
        return (
            f"{self.name} | "
            f"{self.position} | "
            f"Rating: {self.rating}"
        )

    def full_profile(self):
        return (
            f"""
Player ID: {self.id}

Name: {self.name}

Position: {self.position}

Rating: {self.rating}

Age: {self.age}

Nationality: {self.nationality}

Value: £{self.value:,}

Matches: {self.matches}

Goals: {self.goals}

Assists: {self.assists}

Yellow Cards: {self.yellow_cards}

Red Cards: {self.red_cards}
"""
        )
