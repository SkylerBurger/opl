from random import randint

from player import Player
from seed import get_seed_rooms


rooms = get_seed_rooms()


def enter_room(player):
    room = rooms[randint(0, 2)]
    print("*********************")
    print(f"You find yourself in {room.name}.")
    print(room.description)
    room.play(player)
    print("*********************")


def play():
    print("Hello and welcome to this haunted home.")
    player_name = input("What is your name?: ")
    player = Player(player_name, 100, 100)
    print(f"Nice to meet you, {player.name}.")
    print("Let's enter the house.")

    while True:
        enter_room(player)
        choice = input(
            "Would you like to proceed to the next room (r), check your inventory first (i), or quit (q)?: "
        )
        if choice.lower() == "i":
            player.check_inventory()
        elif choice.lower() == "q":
            break

    print("Thank you for visiting our home!")


if __name__ == "__main__":
    play()
