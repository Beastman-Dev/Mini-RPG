# Room properties = name, description, search_results, exits, enemies, treasure
dungeon_rooms = {
    "room_1": {
    "name": "Entrance Hall",
    "description": "You're in a hallway. To the North is the dungeon entrance. There are doors to the East and West. The hall is otherwise empty.",
    "search_results": "You hear gutteral voices coming from the West and faint snoring from the East.",
    "exits": ("North", "East", "West"),
    "enemies": None,
    "treasure": None
    },
    "room_2": {
    "name": "West Dormitory",
    "description": "This appears to be a primitive dormitory, with sleeping pallets lining the walls and various articles of clothing hung from spikes in the walls. Two goblins are laying down but awake and talking with a third, who appears to be undressing for bed. All three turn toward the door as you enter and immediately scramble for weapons.",
    "search_results": "The articles of clothing are tattered and worthless. You find five copper coins stashed in the sleeping pallets.",
    "exits": ("East", "South"),
    "enemies": {"goblins": 3},
    "treasure": {"copper": 5}
    },
    "room_3": {
    "name": "East Dormitory",
    "description": "This appears to be a primitive dormitory, with sleeping pallets lining the walls and various articles of clothing hung from spikes in the walls. Three goblins lay sleeping on their pallets, one snoring loudly.",
    "search_results": "The articles of clothing are tattered and worthless. You find five copper coins stashed in the sleeping pallets.",
    "exits": ("West", "South"),
    "enemies": {"goblins": 3},
    "treasure": {"copper": 5}
    },
    "room_4": {
    "name": "Common Room",
    "description": "This large room is littered with primitive furniture, decorations, and a number of goblins. Several goblins are eating some foul-smelling meal at a table on one side of the room while another handful sit on makeshift stools in a corner, a pile of bones and coins on the floor between them.",
    "search_results": "The furnishing and food in this room are worthless and unappetizing, but you find a dozen copper on the floor next to the bones and on the various goblins.",
    "exits": ("North-East", "North-West", "South"),
    "enemies": {"goblins": 7, "goblin warriors": 2},
    "treasure": {"copper": 12}
    },
    "room_5": {
    "name": "Throne Room Foyer",
    "description": "Hall with double doors at both ends and two tough-looking goblins standing guard in front of the doors to the South.",
    "search_results": "You hear faint sounds of voices coming from the other side of the Southern double-doors.",
    "exits": ("North", "South"),
    "enemies": {"goblin warriors": 2},
    "treasure": {"silver": 4}
    },
    "room_6": {
    "name": "Throne Room",
    "description": "This is a large room with four pillars in the middle and a raised dais on the South side. The only entrance is the double doors you entered through. On the dais sits a rickety throne decorated with bones, an ugly statue of a goblin, and a large wodden chest. A fat goblin sits on the throne, a garishly decorated crown on his head. His clothing is of finer material than the others but tattered, poorly sewn rips in several places. Three other goblins stand near the throne. Standing to the king's right is a large, muscular goblin wearing leather armor and carrying a spiked club. To his left stands a slim, older-looking goblin with an ornate staff and wearing robes. Kneeling at the base of the steps to the dias is a female goblin wearing a dress.",
    "search_results": "The chest contains 11 gold, 27 silver, and 59 copper.",
    "exits": ("North"),
    "enemies": {"goblin king": 1, "goblin champion": 1, "goblin shaman": 1, "goblin female": 1},
    "treasure": {"gold": 11, "silver": 27, "copper": 59}
    }
}

