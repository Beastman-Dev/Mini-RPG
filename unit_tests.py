# Import necessary modules
from main import *
import config

## Unit Tests

def create_dungeon_unit_tests():
    try:
        dungeon: Dungeon = Dungeon("Tomb of Minor Inconvenience", "A dim and depressing underground goblin lair.", config.dungeon_rooms)
        if dungeon.name == "Tomb of Minor Inconvenience":
            return True
    except Exception as e:
        return e

def create_room_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", {"North": "room_0"}, {"goblin": 1}, ["health potion"])
        if room.name == "test_room":
            return True
    except Exception as e:
        return e

def spawn_enemies_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", {"North": "room_0"}, {"goblin": 1}, ["health potion"])
        room.spawn_enemies()
        return True
    except Exception as e:
        return e

def search_room_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", {"North": "room_0"}, {"goblin": 1}, ["health potion"])
        search_results = room.search_room()
        if search_results == "You find a health potion!":
            return True
    except Exception as e:
        return e
    
def exit_room_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", {"North": "room_0"}, {"goblin": 1}, ["health potion"])
        exit_room = room.exit_room("North")
        if exit_room == "room_0":
            return True
    except Exception as e:
        return e

def room_options_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", {"North": "room_0"}, {"goblin": 1}, ["health potion"])
        options = room.room_options()
        if options == ["1. Go North", "2. Search room"]:
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

def damage_target_unit_tests():
    try:
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        character: Character = Character("Beastman", 100, 10)
        sorcerer: Sorcerer = Sorcerer
        character.damage_target(enemy, character.attack)
        if enemy.current_health == 40:
            return True
    except Exception as e:
        return e

def equip_item_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        amulet: Treasure = Treasure("amulet", "a shiny amulet", 10)
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        character.equip(amulet)
        character.equip(weapon)
        character.equip(armor)
        if character.equipment["amulet"] == amulet and character.equipment["sword"] == weapon and character.equipment["shield"] == armor:
            return True
    except Exception as e:
        return e
    
def unequip_item_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        amulet: Treasure = Treasure("amulet", "a shiny amulet", 10)
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        character.equip(amulet)
        character.equip(weapon)
        character.equip(armor)
        character.unequip(amulet)
        character.unequip(weapon)
        character.unequip(armor)
        if character.equipment == {}:
            return True
    except Exception as e:
        return e
    
def add_to_inventory_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        amulet: Treasure = Treasure("amulet", "a shiny amulet", 10)
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        character.add_to_inventory(amulet)
        character.add_to_inventory(weapon)
        character.add_to_inventory(armor)
        if character.inventory["amulet"] == amulet and character.inventory["sword"] == weapon and character.inventory["shield"] == armor:
            return True
    except Exception as e:
        return e
    
def remove_from_inventory_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        amulet: Treasure = Treasure("amulet", "a shiny amulet", 10)
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        character.add_to_inventory(amulet)
        character.add_to_inventory(weapon)
        character.add_to_inventory(armor)
        character.remove_from_inventory(amulet)
        character.remove_from_inventory(weapon)
        character.remove_from_inventory(armor)
        if character.inventory == {}:
            return True
    except Exception as e:
        return e

def use_potion_unit_tests():
    try:
        fighter: Character = Character("Beastman", 100, 10)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        health_potion: Potion = Potion("health potion", "small vial of red liquid", 10, 10)
        mana_potion: Potion = Potion("mana potion", "small vial of blue liquid", 10, 10)
        fighter.use_item(health_potion)
        if fighter.current_health == 100:
            test_1 = True
        else:
            test_1 = False
        sorcerer.use_item(mana_potion)
        if sorcerer.current_mana == 100:
            test_2 = True
        else:
            test_2 = False
        fighter.current_health = 80
        sorcerer.current_mana = 80
        fighter.use_item(health_potion)
        if fighter.current_health == 90:
            test_3 = True
        else:
            test_3 = False
        sorcerer.use_item(mana_potion)
        if sorcerer.current_mana == 90:
            test_4 = True
        else:
            test_4 = False
        if test_1 == True and test_2 == True and test_3 == True and test_4 == True:
            return True
    except FullHealthError as e:
        return True
    except FullManaError as e:
        return True
    except NotSorcererError as e:
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

def create_treasure_unit_tests():
    try:
        amulet: Treasure = Treasure("amulet", "a shiny amulet", 10)
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        if amulet.name == "amulet" and weapon.name == "sword" and armor.name == "shield":
            return True
    except Exception as e:
        return e

def create_weapon_unit_tests():
    try:
        weapon: Weapon = Weapon("sword", "a sharp blade", 10, 5)
        if weapon.name == "sword":
            return True
    except Exception as e:
        return e

def create_armor_unit_tests():
    try:
        armor: Armor = Armor("shield", "a sturdy shield", 10, 5)
        if armor.name == "shield":
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

def start_combat_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        combat: Combat = Combat(character, enemy)
        if combat.player == character and combat.enemies == enemy:
            return True
    except Exception as e:
        return e

def player_combat_options_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        combat: Combat = Combat(character, enemy)
        options = combat.player_combat_options()
        if options == ["1. Use potion", "2. Attack"]:
            return True
    except Exception as e:
        return e

def combat_loop_unit_tests():
    pass

def attack_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        enemy: Monster = Monster("Goblin 1", 50, 5, 0)
        character.damage_target(enemy, character.attack)
        if enemy.current_health == 40:
            return True
    except Exception as e:
        return e

def create_game_unit_tests():
    pass
    
def start_game_unit_tests():
    pass
    
def enter_room_unit_tests():
    pass

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

## Search room tests
passed = search_room_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Search room unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Exit room tests
passed = exit_room_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Exit room unit test: {result}")
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

## Damage target tests
passed = damage_target_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Damage target unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Equip item tests
passed = equip_item_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Equip item unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Unequip item tests
passed = unequip_item_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Unequip item unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Add to inventory tests
passed = add_to_inventory_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Add to inventory unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Remove from inventory tests
passed = remove_from_inventory_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Remove from inventory unit test: {result}")
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

## Treasure creation tests
passed = create_treasure_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Treasure creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Weapon creation tests
passed = create_weapon_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Weapon creation unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Armor creation tests
passed = create_armor_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Armor creation unit test: {result}")
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

## Combat start tests
passed = start_combat_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Combat start unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Combat options tests
passed = player_combat_options_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Combat options unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## Combat loop tests
#passed = combat_loop_unit_tests()
#if passed == True:
#    result = "PASSED"
#else:
#    result = "FAILED"
#print(f"Combat loop unit test: {result}")
#if passed != True:
#    print(f"Error: {passed}")

## Attack tests
passed = attack_unit_tests()
if passed == True:
    result = "PASSED"
else:
    result = "FAILED"
print(f"Attack unit test: {result}")
if passed != True:
    print(f"Error: {passed}")

## 