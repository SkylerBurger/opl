from random import randint

from room import Room
from mechanic import (
    InstantOutcome,
    Mechanic,
    Outcome,
    RollEvent,
)


seed_rooms_details = [
    ("The Library", "A large and musty collection of ancient tomes."),
    (
        "The Kitchen",
        "A large wooden island dominates the center of this large cooking space.",
    ),
    ("The Arboretum", "A tall droopy willow tree stands under a glass dome."),
    ("The Closet", "A small, cramped space containing coats and boxes."),
    ("The Guest Room", "A quaint bedroom just waiting for someone to stay... forever."),
    ("The Parlor", "A large room that would be more jovial if it weren't so dark."),
]

seed_instant_outcomes_details = [
    (
        "Friendly Ghost",
        "You sense the presence of someone that has passed on. They grant you 10 health.",
        "health",
        10,
    ),
    (
        "Curious Cat",
        "You see a black cat pace across the room. You reach out to pet it and the cat vanishes in to thin air. Lose 10 sanity",
        "sanity",
        -10,
    ),
]

seed_roll_events = [
    RollEvent(
        "Careful Steps",
        "The floor is creaky, walk softly. Roll above a 3 to cross safely and gain 10 sanity, otherwise lose 10 health.",
        1,
        [
            ([1, 2, 3], Outcome("stat", "health", increment=-10)),
            ([4, 5, 6], Outcome("stat", "sanity", increment=10)),
        ],
    ),
    RollEvent(
        "Possessive Vibes",
        "You feel an otherworldly force trying to take control of your body. Roll an even number to stabilize or lose 10 sanity.",
        1,
        [([1, 3, 5], Outcome("stat", "health", increment=-10))],
    ),
    RollEvent(
        "Flurry of Consciousness",
        "Diary pages covered in scrawling handwriting fly out from a notebook, forming a tornado around. Roll 2 dice, if your total is 8 or higher you successfully stay in the eye of the storm, otherwise you lose 10 health.",
        2,
        [([1, 2, 3, 4, 5, 6, 7], Outcome("stat", "health", increment=-10))],
    ),
]


def get_seed_rooms():

    instant_outcomes: list[Mechanic] = [
        InstantOutcome(name, description, stat, increment)
        for name, description, stat, increment in seed_instant_outcomes_details
    ]

    mechanics = instant_outcomes + seed_roll_events

    rooms = list()

    for name, description in seed_rooms_details:
        this_mechanic = mechanics[randint(0, len(mechanics) - 1)]
        rooms.append(Room(name, description, this_mechanic))

    return rooms
