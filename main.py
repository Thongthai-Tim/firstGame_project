import random
import copy

# Player class
class Player:
    def __init__(self, hp: int, name: str, atk: int, charge: int = 0):
        self.hpBackup = hp
        self.atkBackup = atk
        self.chargeBackup = charge
        self.hp = hp
        self.name = name
        self.atk = atk
        self.charge = charge
        self.weapon = "fists"
        self.weaponBackup = self.weapon

    def hitted(self, dmg: int):
        self.hp -= dmg

    def charged(self):
        self.charge += 1

    def equipment(self, weapon: str, wpatk_stat: int):
        self.weapon = weapon
        self.atk += wpatk_stat

    def restore(self):
        self.hp = self.hpBackup
        self.atk = self.atkBackup
        self.charge = self.chargeBackup
        self.weapon = self.weaponBackup

    def __str__(self):
        return f"{self.name} HP: {self.hp} ATK: {self.atk} CHARGE: {self.charge} WEAPON: {self.weapon}"

# Fight class
class Fight:
    def __init__(self, pattern: list, enemy: Player):
        self.pattern = pattern
        self.enemy = enemy
        self.index = 0

    def show_pattern(self):
        print("Enemy pattern:", self.pattern)

    def execute_turn(self, player: Player):
        current_pattern = self.pattern[self.index]
        self.index = (self.index + 1) % len(self.pattern)  # Looping through the pattern

        if current_pattern == 'A':  # Enemy attacks
            my_line()
            choose = int(input("1. ATK 2. DEF 3. CHR\nChoice :  "))
            if choose == 1:
                if player.charge > 0:
                    player.hitted(self.enemy.atk)
                    player.charge -= 1
                    print("You got Damages!!!")
                else :
                    player.hitted(self.enemy.atk)
                    print("You got Damages!!!")
            elif choose == 2:
                print("You blocked the attack!")
                my_line()
            elif choose == 3:
                player.hitted(self.enemy.atk)
                print("You got Damages!!!")
            else:
                print("ATK DEF CHR only bro!!!")
                my_line()

        elif current_pattern == 'D':  # Enemy defends
            my_line()
            choose = int(input("1. ATK 2. DEF 3. CHR\nChoice : "))
            if choose == 1:
                if player.charge == 0:
                    print(f"{self.enemy.name} blocked the attack!")
                    my_line()
                else:
                    self.enemy.hitted(player.atk)
                    player.charge -= 1
            elif choose == 2:
                print("Nothing happened.")
                my_line()
            elif choose == 3:
                player.charged()
                print("Charged +1.")
            else:
                print("ATK DEF CHR only bro!!!")
                my_line()


# Weapon class
class Weapon:
    def __init__(self, weapon: str = 'fists', atk: int = 0):
        self.type = weapon
        self.atk = atk

    def __str__(self):
        return f"Weapon is {self.type} DMG Power Up + {self.atk}"

def my_line():
    print("______________________________________________________________\n")


#Characters
player_info = Player(20, "Player", 2)
slime_info  = Player(5, "Slime", 3)
goblin_info = Player(20,"Goblin",5)


#Weapons
great_sword = Weapon('Great Sword', 5)
long_sword = Weapon('Long Sword', 2)
lance = Weapon('Lance', 3)

#Pattern for enemies
goblin = Fight(['A', 'A', 'D', 'A'], goblin_info)
slime = Fight(['A', 'D'], slime_info)

#Player chooses a weapon
print(f"\n{player_info}\n")
while True:
    print("Welcome the  Arena")
    print(f"{player_info}\n")
    while True:
        choice = int(input("Choose your weapon:\n1. Great Sword\n2. Long Sword\n3. Lance\n4. No equip\nChoice : "))
        if choice == 1:
            print(f"{great_sword}\n")
            player_info.equipment(great_sword.type, great_sword.atk)
            break
        elif choice == 2:
            print(f"{long_sword}\n")
            player_info.equipment(long_sword.type, long_sword.atk)
            break
        elif choice == 3:
            print(f"{lance}\n")
            player_info.equipment(lance.type, lance.atk)
            break
        elif choice == 4:
            print("No equip")
            break
        else:
            print("Choose again")

    #Start fighting
    weapon_list = ['Great Sword', 'Lance', 'Long Sword']

    fight_choice = int(input("You want to fight?\n1. Goblin\n2. Slime\n3.Exit\nChoice : "))
    if fight_choice == 1:
        print("Oh shit that is Goblin !!!")
        print("""
            ,      ,
            /(.-""-.)\\
        |\\  \\/      \\/  /|
        | \\ / =.  .= \\ / |
        \\( \\   o\\/o   / )/
        \\_, '-/  \\-' ,_/
            /   \\__/   \\
            \\ \\__/\\__/ /
        ___\\ \\|--|/ /___
        /`    \\      /    `\\
        /       '----'       \\
        """)
        goblin.show_pattern()

        while goblin_info.hp > 0:
            goblin.execute_turn(player_info)
            print(f"{player_info}\n{goblin_info}")
            if goblin_info.hp <= 0:
                print("You defeated the Goblin!")
                goblin_info.restore()
                player_info.restore()
                break
            elif player_info.hp <= 0:
                print("YOU DIED!")
                slime_info.restore()
                player_info.restore()
                break

    elif fight_choice == 2:
        print("OMG I meet Slime !!!")
        print("""
                ░░░░░░░░░░              
            ░░░░        ░░░░░░         
            ░░                  ░░         
        ░░                    ░░░░      
        ░░                      ░░░░░░   
        ░░                        ░░░░       
    ░░                ░░    ░░  ░░░░░░    
    ░░                ██░░  ██    ░░░░   
    ░░                ██░░  ██    ░░░░  
    ░░            ░░            ░░░░░░ 
    ░░░░░░                      ░░░░░░  
        ░░░░░░                  ░░░░░░   
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
            ░░░░░░░░░░░░░░░░░░░░░░ 
            """)
        slime.show_pattern()

        while slime_info.hp > 0:
            slime.execute_turn(player_info)
            print(f"{player_info}\n{slime_info}")
            
            if slime_info.hp <= 0:
                print("You defeated the Slime!")
                slime_info.restore()
                player_info.restore()
                break
            elif player_info.hp <= 0:
                print("YOU DIED!")
                slime_info.restore()
                player_info.restore()
                break
    
    elif fight_choice == 3: #exit game
        print("Exit")
        break    
    



