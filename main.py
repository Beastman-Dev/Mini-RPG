import config

class Dungeon:
    def __init__(self, name: str, description: str, rooms: dict) -> None:
        self.name = name
        self.description = description
        self.rooms = rooms

class Room:
    def __init__(self, name: str, description: str, search_results: str, exits: dict, enemies: dict, treasure: dict) -> None:
        self.name = name
        self.description = description
        self.search_results = search_results
        self.exits = exits
        self.enemies = enemies
        self.treasure = treasure

    def spawn_enemies(self) -> list:
        instances = []
        for enemy in self.enemies:
            for i in range(self.enemies[enemy]):
                instance = Monster(enemy, config.enemies[enemy]["health"], config.enemies[enemy]["attack"], i)
                instances.append(instance)
        return instances

    def search_room(self) -> str:
        return self.search_results

    def exit_room(self, exit: str) -> str:
        if exit not in self.exits:
            raise ValueError("Invalid exit!")
        self.exit = exit
        new_room = self.exits[exit]
        return new_room

    def room_options(self) -> list:
        options = []
        for i, (direction, _) in enumerate(self.exits.items()):
            options.append(f"{i+1}. Go {direction}")
        options.append(f"{len(self.exits) + 1}. Search room")
        return options

class FullHealthError(Exception):
    pass

class FullManaError(Exception):
    pass

class NotSorcererError(Exception):
    pass

class Creature:
    def __init__(self, name: str, health: int, attack: int) -> None:
        self.name = name
        self.health = health
        self.current_health = health
        self.attack = attack

    def damage_target(self, target: dict, attack_power: int) -> int:
        self.target = target
        target.current_health -= attack_power
        return target.current_health

class Monster(Creature):
    def __init__(self, name: str, health: int, attack: int, instance_id: int) -> None:
        super().__init__(name, health, attack)
        self.id = instance_id

class Character(Creature):
    def __init__(self, name: str, health: int, attack: int) -> None:
        super().__init__(name, health, attack)
        self.equipment = {}
        self.inventory = {}

    def equip(self, item: dict) -> None:
        self.item = item
        self.equipment[item.name] = item

    def unequip(self, item: dict) -> None:
        self.item = item
        del self.equipment[item.name]

    def add_to_inventory(self, item: dict) -> None:
        self.item = item
        self.inventory[item.name] = item

    def remove_from_inventory(self, item: dict) -> None:
        self.item = item
        del self.inventory[item.name]
        if item.name in self.equipment:
            del self.equipment[item.name]

    def use_item(self, item: dict) -> None:
        self.item = item
        if item.name == "health potion":
            if self.current_health == self.health:
                raise FullHealthError(f"{self.name} is already at full health!")
            self.current_health += item.potency
            if self.current_health > self.health:
                self.current_health = self.health
        elif item.name == "mana potion":
            if not isinstance(self, Sorcerer):
                raise NotSorcererError("Only sorcerers can use mana potions!")
            if self.current_mana == self.mana:
                raise FullManaError(f"{self.name} is already at full mana!")
            self.current_mana += item.potency
            if self.current_mana > self.mana:
                self.current_mana = self.mana
        else:
            raise Exception("Invalid item!")

class Sorcerer(Character):
    def __init__(self, name: str, health: int, attack: int, mana: int) -> None:
        super().__init__(name, health, attack)
        self.mana = mana
        self.current_mana = mana

    def cast_spell(self, target: dict, spell_power: int) -> int:
        self.target = target
        if spell_power > self.current_mana:
            raise ValueError("You don't have enough mana!")
        self.current_mana -= spell_power
        self.damage_target(target, spell_power)
        return spell_power

class Treasure:
    def __init__(self, name: str, description: str, value: int) -> None:
        self.name = name
        self.description = description
        self.value = value

class Weapon(Treasure):
    def __init__(self, name: str, description: str, value: int, damage: int) -> None:
        super().__init__(name, description, value)
        self.damage = damage

class Armor(Treasure):
    def __init__(self, name: str, description: str, value: int, protection: int) -> None:
        super().__init__(name, description, value)
        self.protection = protection

class Potion(Treasure):
    def __init__(self, name: str, description: str, value: int, potency: int) -> None:
        super().__init__(name, description, value)
        self.potency = potency

class Combat:
    def __init__(self, player: dict, enemies: dict) -> None:
        self.player = player
        self.enemies = enemies

    def player_combat_options(self) -> list:
        options = []
        options.append("1. Use potion")
        options.append("2. Attack")
        if isinstance(self.player, Sorcerer):
            options.append("3. Cast spell")
        return options

    def combat_loop(self) -> None:
        while True:
            options_menu = self.player_combat_options()
            for option in options_menu:
                print(option)
            choice = input("What do you do? ")
            if choice == "1":
                potion_choice = input("Which potion do you use? ")
                if potion_choice == "1":
                    self.player.use_potion(self.player)
                elif potion_choice == "2":
                    self.player.use_potion(self.player)
                else:
                    print("Invalid potion choice.")
            elif choice == "2":
                target_choice = input("Which enemy do you attack? ")
                self.attack(self.player, self.enemies[int(target_choice) - 1])
            elif choice == "3":
                spell_power = input("How much power do you put into the spell? ")
                self.cast_spell(int(spell_power))
            else:
                print("Invalid choice)")

            if self.player.current_health <= 0:
                print("You have died!")
                break
            if all(enemy.current_health <= 0 for enemy in self.enemies):
                print("You have defeated all enemies!")
                break
            for enemy in self.enemies:
                if enemy.current_health > 0:
                    self.attack(self.player, enemy)
            for enemy in self.enemies:
                if enemy.current_health > 0:
                    self.attack(enemy, self.player)

    def attack(self, attacker, defender) -> None:
        attacker.damage_target(defender, attacker.attack)

    def cast_spell(self, spell_power: int) -> None:
        self.attacker.cast_spell(self.defender, spell_power)


class Game():
    def __init__(self, dungeon: dict) -> None:
        self.dungeon = dungeon

    def start(self) -> None:
        print(f"Welcome to {self.dungeon.name}!")
        print(self.dungeon.description)
        self.enter_room(self.dungeon.rooms["room_4"])

    def enter_room(self, room: dict) -> None:
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
        
# dungeon = Dungeon(config.dungeon_name, config.dungeon_description, config.dungeon_rooms)
# game = Game(dungeon)
# game.start()

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