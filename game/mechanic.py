from random import randint

from player import Player


class Mechanic:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def play(self, player):
        pass


class Outcome:
    def __init__(self, flavor: str, stat: str = None, increment: int = None, item=None):
        self.flavor = flavor
        self.stat = stat
        self.increment = increment
        self.item = item

    def apply(self, player: Player):
        if self.flavor == "stat":
            self._update_player_stat(player)
        elif self.flavor == "item":
            self._update_player_inventory(player)

    def _update_player_stat(self, player: Player):
        direction = "increased" if self.increment > 0 else "decreased"
        print(f"Your {self.stat} {direction} by {self.increment}.")
        player.update(self.stat, self.increment)

    def _update_player_inventory(self, player: Player):
        player.add_to_inventory(self.item)


class RollEvent(Mechanic):
    def __init__(self, name: str, description: str, dice: int, roll_outcomes: list):
        super().__init__(name, description)
        self.dice = dice
        self.roll_outcomes = self._generate_outcomes_dict(roll_outcomes)

    @staticmethod
    def _generate_outcomes_dict(roll_outcomes: list):
        outcomes_dict = dict()
        for roll_keys, outcome in roll_outcomes:
            for key in roll_keys:
                outcomes_dict[str(key)] = outcome
        return outcomes_dict

    def play(self, player: Player):
        print(f"~~ {self.name} ~~")
        print(f"--> {self.description}")

        rolls_sum = 0
        for i in range(self.dice):
            roll_result = randint(1, 6)
            print(f"Your rolled a {roll_result}.")
            rolls_sum += roll_result

        print(f"Your roll total is {rolls_sum}.")
        outcome = self.roll_outcomes.get(str(rolls_sum))
        if outcome:
            outcome.apply(player)
        else:
            print("You leave unchanged.")


class InstantOutcome(Mechanic):
    def __init__(self, name: str, description: str, stat: str, increment: int):
        super().__init__(name, description)
        self.stat = stat
        self.increment = increment

    def play(self, player: Player):
        print(f"~~ {self.name} ~~")
        print(f"--> {self.description}")
        player.update(self.stat, self.increment)
