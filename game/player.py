class Player:
    def __init__(self, name: str, sanity: int, health: int):
        self.name = name
        self.inventory = list()
        self.sanity = sanity
        self.health = health

    def report_stats(self):
        print(f"Your stats: Health - {self.health}, Sanity - {self.sanity}")

    def check_inventory(self):
        if self.inventory:
            print("Your inventory has the following items:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("Your inventory is currently empty.")

    def update(self, stat: str, increment: int):
        if stat == "sanity":
            self.sanity += increment
        if stat == "health":
            self.health += increment

    def add_to_inventory(self, item):
        self.inventory.append(item)
