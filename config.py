# Dungeon details
dungeon_name = "Goblin Stronghold"
dungeon_description = "A stronghold of goblins, ruled by a fat goblin king. The stronghold is a series of rooms connected by hallways. The rooms are sparsely furnished and decorated with bones and other grisly trophies. The goblins are primitive and hostile, but not particularly intelligent. The stronghold is dimly lit by torches and the occasional shaft of light from a crack in the ceiling. The air is thick with the smell of unwashed bodies and stale food."
dungeon_rooms = {
    "room_1": {
    "name": "Entrance Hall",
    "description": "You're in a hallway. To the North is the dungeon entrance. There are doors to the East and West. The hall is otherwise empty.",
    "search_results": "You hear gutteral voices coming from the West and faint snoring from the East.",
    "exits": {"North": "exit", "East": "room_3", "West": "room_2"},
    "enemies": None,
    "treasure": None
    },
    "room_2": {
    "name": "West Dormitory",
    "description": "This appears to be a primitive dormitory, with sleeping pallets lining the walls and various articles of clothing hung from spikes in the walls. Two goblins are laying down but awake and talking with a third, who appears to be undressing for bed. All three turn toward the door as you enter and immediately scramble for weapons.",
    "search_results": "The articles of clothing are tattered and worthless. You find five gold coins stashed in the sleeping pallets.",
    "exits": {"East": "room_1", "South": "room_4"},
    "enemies": {"goblin": 3},
    "treasure": {"gold": 5}
    },
    "room_3": {
    "name": "East Dormitory",
    "description": "This appears to be a primitive dormitory, with sleeping pallets lining the walls and various articles of clothing hung from spikes in the walls. Three goblins lay sleeping on their pallets, one snoring loudly.",
    "search_results": "The articles of clothing are tattered and worthless. You find five gold coins stashed in the sleeping pallets.",
    "exits": {"West": "room_1", "South": "room_4"},
    "enemies": {"goblin": 3},
    "treasure": {"gold": 5}
    },
    "room_4": {
    "name": "Common Room",
    "description": "This large room is littered with primitive furniture, decorations, and a number of goblins. Several goblins are eating some foul-smelling meal at a table on one side of the room while another handful sit on makeshift stools in a corner, a pile of bones and coins on the floor between them.",
    "search_results": "The furnishing and food in this room are worthless and unappetizing, but you find a dozen gold on the floor next to the bones and on the various goblins.",
    "exits": {"Northeast": "room_3", "Northwest": "room_2", "South": "room_5"},
    "enemies": {"goblin": 7, "goblin warrior": 2},
    "treasure": {"gold": 12}
    },
    "room_5": {
    "name": "Throne Room Foyer",
    "description": "Hall with double doors at both ends and two tough-looking goblins standing guard in front of the doors to the South.",
    "search_results": "You hear faint sounds of voices coming from the other side of the Southern double-doors.",
    "exits": {"North": "room_4", "South": "room_6"},
    "enemies": {"goblin warrior": 2},
    "treasure": {"gold": 4}
    },
    "room_6": {
    "name": "Throne Room",
    "description": "This is a large room with four pillars in the middle and a raised dais on the South side. The only entrance is the double doors you entered through. On the dais sits a rickety throne decorated with bones, an ugly statue of a goblin, and a large wodden chest. A fat goblin sits on the throne, a garishly decorated crown on his head. His clothing is of finer material than the others but tattered, poorly sewn rips in several places. Three other goblins stand near the throne. Standing to the king's right is a large, muscular goblin wearing leather armor and carrying a spiked club. To his left stands a slim, older-looking goblin with an ornate staff and wearing robes. Kneeling at the base of the steps to the dais is a female goblin wearing a dress.",
    "search_results": "The chest contains 61 gold.",
    "exits": {"North": "room_5"},
    "enemies": {"goblin": 1, "goblin king": 1, "goblin champion": 1, "goblin shaman": 1},
    "treasure": {"gold": 61}
    }
}
enemies = {
    "goblin": {
        "name": "goblin",
        "health": 10,
        "attack": 2
    },
    "goblin warrior": {
        "name": "goblin warrior",
        "health": 20,
        "attack": 4
    },
    "goblin king": {
        "name": "goblin king",
        "health": 50,
        "attack": 6
    },
    "goblin champion": {
        "name": "goblin champion",
        "health": 30,
        "attack": 6
    },
    "goblin shaman": {
        "name": "goblin shaman",
        "health": 30,
        "attack": 8
    }
}