# Import necessary modules
from main import *
import config

## Unit Tests

def create_dungeon_unit_tests():
    try:
        dungeon: Dungeon = Dungeon("Tomb of Minor Inconvenience", config.dungeon_rooms)
        if dungeon.name == "Tomb of Minor Inconvenience":
            return True
    except Exception as e:
        return e

def create_room_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", ["north"], {"goblin": 1}, ["health potion"])
        if room.name == "test_room":
            return True
    except Exception as e:
        return e

def spawn_enemies_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", ["north"], {"goblin": 1}, ["health potion"])
        room.spawn_enemies()
        return True
    except Exception as e:
        return e

def room_options_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", ["north"], {"goblin": 1}, ["health potion"])
        options = room.room_options()
        if options == ["1. Go north", "2. Search room"]:
            return True
    except Exception as e:
        return e

def create_creature_unit_tests():
    try:
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        character: Character = Character("Beastman", 100, 10)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        if enemy.name == "Goblin 1" and character.name == "Beastman" and sorcerer.name == "Gandalf":
            return True
    except Exception as e:
        return e

def create_treasure_unit_tests():
    try:
        amulet: Treasure = Treasure("amulet", "a shiny amulet", 10)
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        if amulet.name == "amulet" and weapon.name == "sword" and armor.name == "shield":
            return True
    except Exception as e:
        return e

def create_potion_unit_tests():
    try:
        health_potion: Potion = Potion("health potion", "small vial of red liquid", 10, 10)
        mana_potion: Potion = Potion("mana potion", "small vial of blue liquid", 10, 10)
        if health_potion.name == "health potion" and mana_potion.name == "mana potion":
            return True
    except Exception as e:
        return e

def use_potion_unit_tests():
    try:
        fighter: Character = Character("Beastman", 100, 10)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        health_potion: Potion = Potion("health potion", "small vial of red liquid", 10, 10)
        mana_potion: Potion = Potion("mana potion", "small vial of blue liquid", 10, 10)
        health_potion.use_potion(fighter)
        if fighter.current_health == 100:
            test_1 = True
        else:
            test_1 = False
        mana_potion.use_potion(sorcerer)
        if sorcerer.current_mana == 100:
            test_2 = True
        else:
            test_2 = False
        fighter.current_health = 80
        sorcerer.current_mana = 80
        health_potion.use_potion(fighter)
        if fighter.current_health == 90:
            test_3 = True
        else:
            test_3 = False
        mana_potion.use_potion(sorcerer)
        if sorcerer.current_mana == 90:
            test_4 = True
        else:
            test_4 = False
        if test_1 == True and test_2 == True and test_3 == True and test_4 == True:
            return True
    except Exception as e:
        return e

def attack_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        character.damage_target(enemy, character.attack)
        if enemy.current_health == 40:
            return True
    except Exception as e:
        return e

def cast_spell_unit_tests():
    try:
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        sorcerer.cast_spell(enemy, 20)
        if enemy.current_health == 30 and sorcerer.current_mana == 80:
            return True
    except ValueError as e:
        return True
    except Exception as e:
        return e

## Run tests

## Dungeon creation tests
passed = create_dungeon_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Dungeon creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Room creation tests
passed = create_room_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Room creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Enemy spawning tests
passed = spawn_enemies_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Enemy spawning unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Room options tests
passed = room_options_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Room options unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Creature creation tests
passed = create_creature_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Creature creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Treasure creation tests
passed = create_treasure_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Treasure creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Potion creation tests
passed = create_potion_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Potion creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Potion use tests
passed = use_potion_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Potion use unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Attack tests
passed = attack_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Attack unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Spell casting tests
passed = cast_spell_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Spell casting unit test: {result}")
if passed != True:
    print
    print(f"Error: {passed}")