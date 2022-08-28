from mechanic import Mechanic


class Room:
    def __init__(
        self,
        name: str,
        description: str,
        mechanic: Mechanic | None = None,
    ):
        self.name = name
        self.description = description
        self.mechanic = mechanic
        self.neighbors = {"north": None, "east": None, "south": None, "west": None}

    def play(self, player):
        self.mechanic.play(player)
        player.report_stats()
