from config import *
import os

class Creature:
    def __init__(self, name: str, health: int, attack: int) -> None:
        self.name = name
        self.health = health
        self.current_health = health
        self.attack = attack

class Room:
    def __init__(self, name: str, description: str, search_results: str, exits: dict, enemies: dict, treasure: dict) -> None:
        self.name = name
        self.description = description
        self.search_results = search_results
        self.exits = exits
        self.enemies = enemies
        self.treasure = treasure

class Dungeon:
    def __init__(self, name: str, description: str, rooms: dict) -> None:
        self.name = name
        self.description = description
        self.rooms = rooms

class Game():
    def __init__(self, dungeon: dict) -> None:
        self.dungeon = dungeon

    def start(self) -> None:
        print(f"Welcome to {self.dungeon.name}!")
        print(self.dungeon.description)
        self.enter_room(self.dungeon.rooms["room_6"])

    def enter_room(self, room: dict) -> None:
        current_room: Room = Room(room["name"], room["description"], room["search_results"], room["exits"], room["enemies"], room["treasure"])
        print(current_room.description)


# dungeon: Dungeon = Dungeon(dungeon_name, dungeon_description, dungeon_rooms)
# game: Game = Game(dungeon)
# game.start()



class Unit_Tests:
    def __init__(self, unit_tests: dict) -> None:
        self.unit_tests = unit_tests
    
    def process_results(self, test_output: dict) -> tuple:
        test_results = {}
        failure_count = 0
        for key, value in test_output.items():
            if value == True:
                result = "PASSED"
            else:
                result = "FAILED"
            if value != True:
                error = value
                failure_count += 1
            else:
                error = ""
            test_results[key] = (result, error)
        return test_results, failure_count

    def run_unit_tests(self):
        results, totals = self.process_results(self.unit_tests)
        for key, value in results.items():
            if value[1] != "":
                print(f"{key}: {value[0]}, Error: {value[1]}")
            else:
                print(f"{key}: {value[0]}")
        if totals == 0:
            print("All tests PASSED!")
        elif totals == 1:
            print(f"{totals} Test FAILED!")
        else:
            print(f"{totals} Tests FAILED!")

# Unit tests
def creature_test() -> bool:
    try:
        test_goblin: Creature = Creature("goblin peasant", 10, 2)
        if test_goblin.name == "goblin peasant":
            return True
    except Exception as e:
        return e

def room_test() -> bool:
    try:
        test_room: Room = Room("Throne Room", "This is a large room with four pillars in the middle and a raised dais on the South side. The only entrance is the double doors you entered through. On the dais sits a rickety throne decorated with bones, an ugly statue of a goblin, and a large wodden chest. A fat goblin sits on the throne, a garishly decorated crown on his head. His clothing is of finer material than the others but tattered, poorly sewn rips in several places. Three other goblins stand near the throne. Standing to the king's right is a large, muscular goblin wearing leather armor and carrying a spiked club. To his left stands a slim, older-looking goblin with an ornate staff and wearing robes. Several other goblins stand around, chittering to one another in their strange tongue.", "The chest contains 61 gold.", {"North": "room_5"}, {"goblin": 3, "goblin king": 1, "goblin champion": 1, "goblin shaman": 1}, {"gold": 61})
        if test_room.name == "Throne Room":
            return True
    except Exception as e:
        return e

def dungeon_test() -> bool:
    try:
        test_dungeon: Dungeon = Dungeon(dungeon_name, dungeon_description, dungeon_rooms)
        if test_dungeon.name == "Goblin Stronghold":
            return True
    except Exception as e:
        return e


unit_testing: Unit_Tests = Unit_Tests({"Creature Test": creature_test(), "Room Test": room_test(), "Dungeon Test": dungeon_test()})
unit_testing.run_unit_tests()