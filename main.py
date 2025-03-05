import config

class Dungeon:
    def __init__(self, name, description, rooms):
        self.name = name
        self.description = description
        self.rooms = rooms

class Room:
    def __init__(self, name, description, search_results, exits, enemies, treasure):
        self.name = name
        self.description = description
        self.search_results = search_results
        self.exits = exits
        self.enemies = enemies
        self.treasure = treasure

    def spawn_enemies(self):
        instances = []
        for enemy in self.enemies:
            for i in range(self.enemies[enemy]):
                instance = Monster(enemy, config.enemies[enemy]["health"], config.enemies[enemy]["attack"], i)
                instances.append(instance)
        return instances

    def search_room(self):
        print(self.search_results)

    def exit_room(self):
        pass

    def room_options(self):
        options = []
        for i, exit in enumerate(self.exits):
            options.append(f"{i+1}. Go {exit}")
        options.append(f"{len(self.exits)+1}. Search room")
        return options

class Creature:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.current_health = health
        self.attack = attack

    def damage_target(self, target, attack_power):
        self.target = target
        target.current_health -= attack_power
        return target.current_health

class Monster(Creature):
    def __init__(self, name, health, attack, instance_id):
        super().__init__(name, health, attack)
        self.id = instance_id

class Character(Creature):
    pass

class Sorcerer(Creature):
    def __init__(self, name, health, attack, mana):
        super().__init__(name, health, attack)
        self.mana = mana
        self.current_mana = mana

    def cast_spell(self, target, spell_power):
        self.target = target
        if spell_power > self.current_mana:
            raise ValueError("You don't have enough mana!")
        self.current_mana -= spell_power
        self.damage_target(target, spell_power)
        return spell_power

class Treasure:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Weapon(Treasure):
    def __init__(self, name, description, value, damage):
        super().__init__(name, description, value)
        self.damage = damage

class Armor(Treasure):
    def __init__(self, name, description, value, protection):
        super().__init__(name, description, value)
        self.protection = protection

class Potion(Treasure):
    def __init__(self, name, description, value, potency):
        super().__init__(name, description, value)
        self.potency = potency

    def add_to_inventory(self):
        pass

    def use_potion(self, imbiber):
        self.imbiber = imbiber
        if self.name == "health potion":
            if imbiber.current_health == imbiber.health:
                print(f"{imbiber.name} is already at full health!")
                return
            print(f"{imbiber.name} drinks a health potion and restores {self.potency} health.")
            imbiber.current_health += self.potency
            if imbiber.current_health > imbiber.health:
                imbiber.current_health = imbiber.health
        elif self.name == "mana potion":
            if not isinstance(imbiber, Sorcerer):
                print("Only sorcerers can use mana potions!")
                return
            if imbiber.current_mana == imbiber.mana:
                print(f"{imbiber.name} is already at full mana!")
                return
            print(f"{imbiber.name} drinks a mana potion and restore {self.potency} mana.")
            imbiber.current_mana += self.potency
            if imbiber.current_mana > imbiber.mana:
                imbiber.current_mana = imbiber.mana
        else:
            print("Invalid potion type!")

class Game():
    def __init__(self, dungeon):
        self.dungeon = dungeon

    def start(self):
        print(f"Welcome to {self.dungeon.name}!")
        print(self.dungeon.description)
        self.enter_room(self.dungeon.rooms["room_1"])

    def enter_room(self, room):
        current_room: Room = Room(room["name"], room["description"], room["search_results"], room["exits"], room["enemies"], room["treasure"])
        print(current_room.description)
        if current_room.enemies:
            print("You found enemies!")
            enemy_number = 1
            for enemy in current_room.spawn_enemies():
                print(f"{enemy_number}. {enemy.name}")
                enemy_number += 1
        else:
            options = current_room.room_options()
            for option in options:
                print(option)
            choice = input(f"What do you do? ")
            return choice    
        
dungeon = Dungeon(config.dungeon_name, config.dungeon_description, config.dungeon_rooms)
game = Game(dungeon)
game.start()

## Functional Testing
# room: Room = Room("test_room", "This is a test room.", "You find a shiny coin.", ("North", "East", "South"), {"goblin": 5, "goblin king": 1, "goblin champion": 1, "goblin shaman": 1}, {"gold": 1})
# enemies = room.spawn_enemies()
# for enemy in enemies:
#     print(f"Instance ID: {enemy.id}, Name: {enemy.name}, Health: {enemy.health}, Attack: {enemy.attack}")
# options = room.room_options()
# for option in options:
#     print(option)
# choice = input(f"What do you do? ")
# if choice == "1":
#     print("You go North.")
# elif choice == "2":
#     print("You go East.")
# elif choice == "3":
#     print("You go South.")
# elif choice == "4":
#     room.search_room()
# else:
#     print("Invalid choice.")
#     exit()