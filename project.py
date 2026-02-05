import random
from pyfiglet import Figlet
from termcolor import colored
p = Figlet(font='slant')

class Warrior():
    def __init__(self, strength=13, defend=7, craft=0, life=7, initiative=5, speed=4, vim=10, mana=0, special='warrior', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Warrior 🫚 🌿'
        else:
            return 'Warrior'

class Wizard():
    def __init__(self, strength=3, defend=6, craft=10, life=7, initiative=2, speed=2, vim=2, mana=6, special='wizard', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Wizard 🫚 🌿'
        else:
            return 'Wizard'

class Witch_hunter():
    def __init__(self, strength=7, defend=7, craft=5, life=7, initiative=4, speed=4, vim=4, mana=1, special='witch hunter', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Witch Hunter 🫚 🌿'
        else:
            return 'Witch Hunter'


class Fairy():
    def __init__(self, strength=2, defend=4, craft=8, life=5, initiative=6, speed=10, vim=1, mana=15, special='fairy', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Fairy 🫚 🌿'
        else:
            return 'Fairy'


class Ogre():
    def __init__(self, strength=14, defend=8, craft=0, life=10, initiative=2, speed=3, vim=3, mana=0, special='ogre', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Ogre 🫚 🌿'
        else:
            return 'Ogre'


class Dark_elf():
    def __init__(self, strength=10, defend=4, craft=5, life=8, initiative=3, speed=3, vim=4, mana=4, special='dark elf', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Dark Elf 🫚 🌿'
        else:
            return 'Dark Elf'

class Bard():
    def __init__(self, strength=4, defend=5, craft=7, life=7, initiative=5, speed=3, vim=3, mana=2, special='bard', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Bard 🫚 🌿'
        else:
            return 'Bard'

class Rogue():
    def __init__(self, strength=7, defend=7, craft=5, life=7, initiative=7, speed=7, vim=4, mana=1, special='rogue', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Rogue 🫚 🌿'
        else:
            return 'Rogue'

class Paladin():
    def __init__(self, strength=9, defend=8, craft=7, life=7, initiative=3, speed=3, vim=4, mana=3, special='paladin', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Paladin 🫚 🌿'
        else:
            return 'Paladin'

class Archer():
    def __init__(self, strength=4, defend=6, craft=0, life=7, initiative=5, speed=3, vim=7, mana=0, special='archer', shots=12, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Archer 🫚 🌿'
        else:
            return 'Archer'

class Troll():
    def __init__(self, strength=15, defend=10, craft=0, life=10, initiative=1, speed=2, vim=2, mana=0, special='troll', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Troll 🫚 🌿'
        else:
            return 'Troll'

class Vampire():
    def __init__(self, strength=11, defend=8, craft=0, life=8, initiative=4, speed=6, vim=7, mana=0, special='vampire', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Vampire 🫚 🌿'
        else:
            return 'Vampire'

class Ghost_knight():
    def __init__(self, strength=9, defend=8, craft=7, life=8, initiative=3, speed=5, vim=4, mana=3, special='ghost knight', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Ghost Knight 🫚 🌿'
        else:
            return 'Ghost Knight'


class Sorceress():
    def __init__(self, strength=4, defend=6, craft=9, life=7, initiative=4, speed=3, vim=3, mana=7, special='sorceress', shots=0, freeze=3, thunder=3, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        if self.creepers == 1:
            return '🌿🫚  Sorceress 🫚 🌿'
        else:
            return 'Sorceress'

class Ent():
    def __init__(self, strength=15, defend=15, craft=0, life=10, initiative=1, speed=1, vim=10, mana=0, special='ent', shots=0, freeze=0, thunder=0, creepers=0, fear=0):
        self.strength = strength
        self.defend = defend
        self.craft = craft
        self.life = life
        self.initiative = initiative
        self.speed = speed
        self.vim = vim
        self.mana = mana
        self.died = None
        self.special = special
        self.shots = shots
        self.freeze = freeze
        self.thunder = thunder
        self.creepers = creepers
        self.fear = fear
    def __repr__(self):
        return 'Ent'


warrior = Warrior()
wizard = Wizard()
bounty_hunter = Witch_hunter()
ogre = Ogre()
fairy = Fairy()
dark_elf = Dark_elf()
bard = Bard()
rogue = Rogue()
paladin = Paladin()
archer = Archer()
troll = Troll()
vampire = Vampire()
ghost_k = Ghost_knight()
sorceress = Sorceress()
ent = Ent()
sorceress_vim_max = sorceress.vim
sorceress_mana_max = sorceress.mana
sorceress_speed_max = sorceress.speed
ghost_k_vim_max = ghost_k.vim
ghost_k_mana_max = ghost_k.mana
ghost_k_speed_max = ghost_k.speed
vampire_vim_max = vampire.vim
vampire_life_max = vampire.life
vampire_speed_max = vampire.speed
troll_vim_max = troll.vim
troll_speed_max = troll.speed
warrior_vim_max = warrior.vim
warrior_speed_max = warrior.speed
wizard_mana_max = wizard.mana
wizard_vim_max = wizard.vim
wizard_speed_max = wizard.speed
bounty_hunter_vim_max = bounty_hunter.vim
bounty_hunter_mana_max = bounty_hunter.mana
bounty_hunter_speed_max = bounty_hunter.speed
ogre_vim_max = ogre.vim
ogre_speed_max = ogre.speed
fairy_vim_max = fairy.vim
fairy_mana_max = fairy.mana
fairy_speed_max = fairy.speed
dark_elf_vim_max = dark_elf.vim
dark_elf_mana_max = dark_elf.mana
dark_elf_speed_max = dark_elf.speed
bard_vim_max = bard.vim
bard_mana_max = bard.mana
bard_speed_max = bard.speed
rogue_vim_max = rogue.vim
rogue_mana_max = rogue.mana
rogue_speed_max = rogue.speed
fairy_vim_max = fairy.vim
fairy_mana_max = fairy.mana
fairy_speed_max = fairy.speed
paladin_vim_max = paladin.vim
paladin_mana_max = paladin.mana
paladin_speed_max = paladin.speed
paladin_life_max = paladin.life
archer_vim_max = archer.vim
archer_speed_max = archer.speed
ent_vim_max = ent.vim

def main():
    the_round = 0
    p1 = 0
    p2 = 0
    warrior_only_once = 0
    wizard_only_once = 0
    bounty_hunter_only_once = 0
    ogre_only_once = 0
    fairy_only_once = 0
    dark_elf_only_once = 0
    bard_only_once = 0
    rogue_only_once = 0
    paladin_only_once = 0
    archer_only_once = 0
    troll_only_once = 0
    vampire_only_once = 0
    ghost_k_only_once = 0
    sorceress_only_once = 0
    ent_only_once = 0
    box1, box2 = get_your_fighter()
    freezer = []
    fear = []
    he_returned = []
    he_was = 'no'
    temp_box_2 = []
    while True:
        if p1 == 5:
            print(f'\nPlayer1 won!\nPlayer1 score: {p1}\nPlayer2 score: {p2}')
            break
        elif p2 == 5:
            print(f'\nPlayer2 won!\nPlayer1 score: {p1}\nPlayer2 score: {p2}')
            break
        elif the_round == 10:
            if p1 > p2:
                print(f'\nPlayer1 won!\nPlayer1 score: {p1}\nPlayer2 score: {p2}')
                break
            elif p2 > p1:
                print(f'\nPlayer2 won!\nPlayer1 score: {p1}\nPlayer2 score: {p2}')
                break
            else:
                print(f'\nIt is a draw!\nPlayer1 score: {p1}\nPlayer2 score: {p2}')
        initiative, box, the_round, player1, player2= get_initiative(box1, box2, the_round)
        print(p.renderText(f'Round    {the_round}'))
        while True:
            box, freezer, temp_box_2 = get_freezer(box, freezer, temp_box_2)
            box, fear = get_fear(box, fear)
            box, pleya1 = get_prepare(initiative, box, freezer, fear, he_returned)
            if len(box) == 0:
                break
            attacker_vim, attacker_mana, attacker_life, defending_life, attacker, defending = get_attack_and_defence(box, player1, player2)
            won, vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was = get_player_attack(attacker_vim, attacker_mana, attacker_life, defending_life, attacker, defending, pleya1, initiative, freezer, fear, box, he_was, temp_box_2)
            box, p1, p2, fear, warrior_only_once, wizard_only_once, bounty_hunter_only_once, ogre_only_once, fairy_only_once, dark_elf_only_once, bard_only_once, rogue_only_once, paladin_only_once, archer_only_once, troll_only_once, vampire_only_once, ghost_k_only_once, sorceress_only_once, ent_only_once = face_off(box, pleya1, attacker, defending, won, vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, p1, p2, warrior_only_once, wizard_only_once, bounty_hunter_only_once, ogre_only_once, fairy_only_once, dark_elf_only_once, bard_only_once, rogue_only_once, paladin_only_once, archer_only_once, troll_only_once, vampire_only_once, ghost_k_only_once, sorceress_only_once, ent_only_once, fear)
            if len(box) == 0:
                break
            elif p1 == 5:
                break
            elif p2 == 5:
                break

def get_your_fighter():
    player1_box = []
    player2_box = []
    box = ['Wizard', 'Warrior', 'Witch Hunter', 'Ogre', 'Fairy', 'Dark Elf', 'Archer', 'Bard', 'Paladin', 'Rogue', 'Troll', 'Vampire', 'Ghost Knight', 'Sorceress', 'Ent']
    while True:
        while True:
            player1 = input(colored(f'\nPlayer1\nChoose your fighter: {', '.join(box)}.\nYour fighter: ', 'magenta')).title().strip()
            if player1 not in player1_box and player1 not in player2_box:
                if player1 in ['Wizard', 'Warrior', 'Witch Hunter', 'Ogre', 'Fairy', 'Dark Elf', 'Archer', 'Bard', 'Paladin', 'Rogue', 'Troll', 'Vampire', 'Ghost Knight', 'Sorceress', 'Ent']:
                    player1_box.append(player1)
                    box.remove(player1)
                    break

        while True:
            player2 = input(colored(f'\nPlayer2\nChoose your fighter: {', '.join(box)}.\nYour fighter: ', 'cyan')).title().strip()
            if player2 not in player1_box and player2 not in player2_box:
                if player2 in ['Wizard', 'Warrior', 'Witch Hunter', 'Ogre', 'Fairy', 'Dark Elf', 'Archer', 'Bard', 'Paladin', 'Rogue', 'Troll', 'Vampire', 'Ghost Knight', 'Sorceress', 'Ent']:
                    player2_box.append(player2)
                    box.remove(player2)
                    break


        if len(player1_box) == 5 and len(player2_box) == 5:
            return player1_box, player2_box

def get_initiative(player1_box, player2_box, the_round):
    box = player1_box + player2_box
    my_box = []
    if archer.life <= 0:
        archer.died = 'yes'
    if warrior.life <= 0:
        warrior.died = 'yes'
    if wizard.life <= 0:
        wizard.died = 'yes'
    if bounty_hunter.life <= 0:
        bounty_hunter.died = 'yes'
    if ogre.life <= 0:
        ogre.died = 'yes'
    if fairy.life <= 0:
        fairy.died = 'yes'
    if dark_elf.life <= 0:
        dark_elf.died = 'yes'
    if bard.life <= 0:
        bard.died = 'yes'
    if paladin.life <= 0:
        paladin.died = 'yes'
    if rogue.life <= 0:
        rogue.died = 'yes'
    if troll.life <= 0:
        troll.died = 'yes'
    if vampire.life <= 0:
        vampire.died = 'yes'
    if ghost_k.life <= 0:
        ghost_k.died = 'yes'
    if sorceress.life <= 0:
        sorceress.died = 'yes'
    if ent.life <= 0:
        ent.died = 'yes'
    while True:
        for i in box:
            if i == 'Warrior' and warrior.died != 'yes':
                my_box.append({'Class': warrior, 'Name': 'Warrior', 'Warrior': 'Player1' if i in player1_box else 'Player2', 'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Wizard' and wizard.died != 'yes':
                my_box.append({'Class': wizard, 'Name': 'Wizard', 'Wizard': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6)])})
            if i == 'Witch Hunter' and bounty_hunter.died != 'yes':
                my_box.append({'Class': bounty_hunter, 'Name': 'Witch Hunter', 'Witch Hunter': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Ogre' and ogre.died != 'yes':
                my_box.append({'Class': ogre, 'Name': 'Ogre', 'Ogre': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6)])})
            if i == 'Fairy' and fairy.died != 'yes':
                my_box.append({'Class': fairy, 'Name': 'Fairy', 'Fairy': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Dark Elf' and dark_elf.died != 'yes':
                my_box.append({'Class': dark_elf, 'Name': 'Dark Elf', 'Dark Elf': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Bard' and bard.died != 'yes':
                my_box.append({'Class': bard, 'Name': 'Bard', 'Bard': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Rogue' and rogue.died != 'yes':
                my_box.append({'Class': rogue, 'Name': 'Rogue', 'Rogue': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6),random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Paladin' and paladin.died != 'yes':
                my_box.append({'Class': paladin, 'Name': 'Paladin', 'Paladin': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Archer' and archer.died != 'yes':
                my_box.append({'Class': archer, 'Name': 'Archer', 'Archer': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Troll' and troll.died != 'yes':
                my_box.append({'Class': troll, 'Name': 'Troll', 'Troll': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6)])})
            if i == 'Vampire' and vampire.died != 'yes':
                my_box.append({'Class': vampire, 'Name': 'Vampire', 'Vampire': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Ghost Knight' and ghost_k.died != 'yes':
                my_box.append({'Class': ghost_k, 'Name': 'Ghost Knight', 'Ghost Knight': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Sorceress' and sorceress.died != 'yes':
                my_box.append({'Class': sorceress, 'Name': 'Sorceress', 'Sorceress': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)])})
            if i == 'Ent' and ent.died != 'yes':
                my_box.append({'Class': ent, 'Name': 'Ent', 'Ent': 'Player1' if i in player1_box else 'Player2' ,'Player': 'Player1' if i in player1_box else 'Player2', 'Initiative': sum([random.randint(1,3)])})


        life = 0
        if archer.died == 'yes':
            life += 1
        if warrior.died == 'yes':
            life += 1
        if wizard.died == 'yes':
            life += 1
        if bounty_hunter.died == 'yes':
            life += 1
        if ogre.died == 'yes':
            life += 1
        if fairy.died == 'yes':
            life += 1
        if dark_elf.died == 'yes':
            life += 1
        if bard.died == 'yes':
            life += 1
        if rogue.died == 'yes':
            life += 1
        if paladin.died == 'yes':
            life += 1
        if troll.died == 'yes':
            life += 1
        if vampire.died == 'yes':
            life += 1
        if ghost_k.died == 'yes':
            life += 1
        if sorceress.died == 'yes':
            life += 1
        if ent.died == 'yes':
            life += 1

        if len(my_box) + life == 10:
            break
    the_round += 1
    the_box = []
    player1 = []
    player2 = []
    for i in my_box:
        my_initiative = sorted(my_box, key=lambda x: x['Initiative'], reverse=True)

    for i in my_initiative:
        the_box.append(i['Name'])
        if i['Player'] == 'Player1':
            player1.append(i)
        else:
            player2.append(i)

    return my_initiative, the_box, the_round, player1, player2


def get_attack_and_defence(box, player1, player2):
        my_player1 = []
        for i in player1:
            my_player1.append(i['Name'])
        my_player2 = []
        for i in player2:
            my_player2.append(i['Name'])

        if box[0] == 'Warrior':
            attacker = warrior
        elif box[0] == 'Wizard':
            attacker = wizard
        elif box[0] == 'Witch Hunter':
            attacker = bounty_hunter
        elif box[0] == 'Ogre':
            attacker = ogre
        elif box[0] == 'Fairy':
            attacker = fairy
        elif box[0] == 'Dark Elf':
            attacker = dark_elf
        elif box[0] == 'Bard':
            attacker = bard
        elif box[0] == 'Rogue':
            attacker = rogue
        elif box[0] == 'Paladin':
            attacker = paladin
        elif box[0] == 'Archer':
            attacker = archer
        elif box[0] == 'Troll':
            attacker = troll
        elif box[0] == 'Vampire':
            attacker = vampire
        elif box[0] == 'Ghost Knight':
            attacker = ghost_k
        elif box[0] == 'Sorceress':
            attacker = sorceress
        elif box[0] == 'Ent':
            attacker = ent


        while True:
            player_attack = 'Player1' if box[0] in my_player1 else 'Player2'
            if attacker.craft > 0 and box[0] in my_player1:
                defense = input(f'\n{colored(attacker, 'magenta')} {attacker.strength*'🔴'} {colored(attacker.strength, 'red', attrs=['bold'])}  {attacker.craft*'🔵'} {colored(attacker.craft, 'blue', attrs=['bold'])}  {attacker.speed*'🟡'} {colored(attacker.speed, 'yellow', attrs=['bold'])}  {attacker.vim*'🟪'} {attacker.mana*'🧊'} {attacker.shots*'🏹'} {attacker.freeze*'❄️ '} {attacker.thunder*'🗲 '} \nAction! ').title()
            elif box[0] in my_player1:
                defense = input(f'\n{colored(attacker, 'magenta')} {attacker.strength*'🔴'} {colored(attacker.strength, 'red', attrs=['bold'])}  {attacker.speed*'🟡'} {colored(attacker.speed, 'yellow', attrs=['bold'])}  {attacker.vim*'🟪'} {attacker.mana*'🧊'} {attacker.shots*'🏹'} {attacker.freeze*'❄️ '} {attacker.thunder*'🗲 '} \nAction! ').title()
            elif attacker.craft > 0 and box[0] in my_player2:
                defense = input(f'\n{colored(attacker, 'cyan')} {attacker.strength*'🔴'} {colored(attacker.strength, 'red', attrs=['bold'])}  {attacker.craft*'🔵'} {colored(attacker.craft, 'blue', attrs=['bold'])}  {attacker.speed*'🟡'} {colored(attacker.speed, 'yellow', attrs=['bold'])}  {attacker.vim*'🟪'} {attacker.mana*'🧊'} {attacker.shots*'🏹'} {attacker.freeze*'❄️ '} {attacker.thunder*'🗲 '} \nAction! ').title()
            elif box[0] in my_player2:
                defense = input(f'\n{colored(attacker, 'cyan')} {attacker.strength*'🔴'} {colored(attacker.strength, 'red', attrs=['bold'])}  {attacker.speed*'🟡'} {colored(attacker.speed, 'yellow', attrs=['bold'])}  {attacker.vim*'🟪'} {attacker.mana*'🧊'} {attacker.shots*'🏹'} {attacker.freeze*'❄️ '} {attacker.thunder*'🗲 '} \nAction! ').title()

            if defense == 'Rest':
                print(f'{attacker} resting')
                return attacker.vim, attacker.mana, attacker.life, None, attacker, None
            elif defense in my_player1 and player_attack == 'Player2' or defense in my_player2 and player_attack == 'Player1':
                if box[0] == 'Warrior':
                    attacker_vim = warrior.vim
                    attacker_mana = warrior.mana
                    attacker_life = warrior.life
                    attacker = warrior
                elif box[0] == 'Wizard':
                    attacker_vim = wizard.vim
                    attacker_mana = wizard.mana
                    attacker_life = wizard.life
                    attacker = wizard
                elif box[0] == 'Witch Hunter':
                    attacker_vim = bounty_hunter.vim
                    attacker_mana = bounty_hunter.mana
                    attacker_life = bounty_hunter.life
                    attacker = bounty_hunter
                elif box[0] == 'Ogre':
                    attacker_vim = ogre.vim
                    attacker_mana = ogre.mana
                    attacker_life = ogre.life
                    attacker = ogre
                elif box[0] == 'Fairy':
                    attacker_vim = fairy.vim
                    attacker_mana = fairy.mana
                    attacker_life = fairy.life
                    attacker = fairy
                elif box[0] == 'Dark Elf':
                    attacker_vim = dark_elf.vim
                    attacker_mana = dark_elf.mana
                    attacker_life = dark_elf.life
                    attacker = dark_elf
                elif box[0] == 'Bard':
                    attacker_vim = bard.vim
                    attacker_mana = bard.mana
                    attacker_life = bard.life
                    attacker = bard
                elif box[0] == 'Rogue':
                    attacker_vim = rogue.vim
                    attacker_mana = rogue.mana
                    attacker_life = rogue.life
                    attacker = rogue
                elif box[0] == 'Paladin':
                    attacker_vim = paladin.vim
                    attacker_mana = paladin.mana
                    attacker_life = paladin.life
                    attacker = paladin
                elif box[0] == 'Archer':
                    attacker_vim = archer.vim
                    attacker_mana = archer.mana
                    attacker_life = archer.life
                    attacker = archer
                elif box[0] == 'Troll':
                    attacker_vim = troll.vim
                    attacker_mana = troll.mana
                    attacker_life = troll.life
                    attacker = troll
                elif box[0] == 'Vampire':
                    attacker_vim = vampire.vim
                    attacker_mana = vampire.mana
                    attacker_life = vampire.life
                    attacker = vampire
                elif box[0] == 'Ghost Knight':
                    attacker_vim = ghost_k.vim
                    attacker_mana = ghost_k.mana
                    attacker_life = ghost_k.life
                    attacker = ghost_k
                elif box[0] == 'Sorceress':
                    attacker_vim = sorceress.vim
                    attacker_mana = sorceress.mana
                    attacker_life = sorceress.life
                    attacker = sorceress
                elif box[0] == 'Ent':
                    attacker_vim = ent.vim
                    attacker_mana = ent.mana
                    attacker_life = ent.life
                    attacker = ent
                if defense == 'Warrior':
                    defending_life = warrior.life
                    defending = warrior
                elif defense == 'Wizard':
                    defending_life = wizard.life
                    defending = wizard
                elif defense == 'Witch Hunter':
                    defending = bounty_hunter
                    defending_life = bounty_hunter.life
                elif defense == 'Ogre':
                    defending = ogre
                    defending_life = ogre.life
                elif defense == 'Fairy':
                    defending = fairy
                    defending_life = fairy.life
                elif defense == 'Dark Elf':
                    defending = dark_elf
                    defending_life = dark_elf.life
                elif defense == 'Bard':
                    defending_life = bard.life
                    defending = bard
                elif defense == 'Rogue':
                    defending = rogue
                    defending_life = rogue.life
                elif defense == 'Paladin':
                    defending = paladin
                    defending_life = paladin.life
                elif defense == 'Archer':
                    defending = archer
                    defending_life = archer.life
                elif defense == 'Troll':
                    defending = troll
                    defending_life = troll.life
                elif defense == 'Vampire':
                    defending = vampire
                    defending_life = vampire.life
                elif defense == 'Ghost Knight':
                    defending = ghost_k
                    defending_life = ghost_k.life
                elif defense == 'Sorceress':
                    defending = sorceress
                    defending_life = sorceress.life
                elif defense == 'Ent':
                    defending = ent
                    defending_life = ent.life

                return attacker_vim, attacker_mana, attacker_life, defending_life, attacker, defending


def get_freezer(box, freezer, temp_box_2):
    if wizard.freeze == 10:
        freezer.append('Wizard')
        if 'Wizard' in box:
            box.remove('Wizard')
            wizard.freeze = 0
            temp_box_2.append('Wizard')


    elif warrior.freeze == 10:
        freezer.append('Warrior')
        if 'Warrior' in box:
            box.remove('Warrior')
            warrior.freeze = 0
            temp_box_2.append('Warrior')

    elif bounty_hunter.freeze == 10:
        freezer.append('Witch Hunter')
        if 'Witch Hunter' in box:
            box.remove('Witch Hunter')
            bounty_hunter.freeze = 0
            temp_box_2.append('Witch Hunter')

    elif ogre.freeze == 10:
        freezer.append('Ogre')
        if 'Ogre' in box:
            box.remove('Ogre')
            ogre.freeze = 0
            temp_box_2.append('Ogre')


    elif fairy.freeze == 10:
        freezer.append('Fairy')
        if 'Fairy' in box:
            box.remove('Fairy')
            fairy.freeze = 0
            temp_box_2.append('Fairy')

    elif dark_elf.freeze == 10:
        freezer.append('Dark Elf')
        if 'Dark Elf' in box:
            box.remove('Dark Elf')
            dark_elf.freeze = 0
            temp_box_2.append('Dark Elf')

    elif bard.freeze == 10:
        freezer.append('Bard')
        if 'Bard' in box:
            box.remove('Bard')
            bard.freeze = 0
            temp_box_2.append('Bard')


    elif rogue.freeze == 10:
        freezer.append('Rogue')
        if 'Rogue' in box:
            box.remove('Rogue')
            rogue.freeze = 0
            temp_box_2.append('Rogue')

    elif paladin.freeze == 10:
        freezer.append('Paladin')
        if 'Paladin' in box:
            box.remove('Paladin')
            paladin.freeze = 0
            temp_box_2.append('Paladin')


    elif archer.freeze == 10:
        freezer.append('Archer')
        if 'Archer' in box:
            box.remove('Archer')
            archer.freeze = 0
            temp_box_2.append('Archer')



    elif troll.freeze == 10:
        freezer.append('Troll')
        if 'Troll' in box:
            box.remove('Troll')
            troll.freeze = 0
            temp_box_2.append('Troll')



    elif vampire.freeze == 10:
        freezer.append('Vampire')
        if 'Vampire' in box:
            box.remove('Vampire')
            vampire.freeze = 0
            temp_box_2.append('Vampire')



    elif ghost_k.freeze == 10:
        freezer.append('Ghost Knight')
        if 'Ghost Knight' in box:
            box.remove('Ghost Knight')
            ghost_k.freeze = 0
            temp_box_2.append('Ghost Knight')


    elif ent.freeze == 10:
        freezer.append('Ent')
        if 'Ent' in box:
            box.remove('Ent')
            ent.freeze = 0
            temp_box_2.append('Ent')

    return box, freezer, temp_box_2


def get_fear(box, fear):

    if wizard.fear == 10:
        fear.append('Wizard')
        if 'Wizard' in box:
            box.remove('Wizard')
            wizard.fear = 0

    elif warrior.fear == 10:
        fear.append('Warrior')
        if 'Warrior' in box:
            box.remove('Warrior')
            warrior.fear = 0

    elif bounty_hunter.fear == 10:
        fear.append('Witch Hunter')
        if 'Witch Hunter' in box:
            box.remove('Witch Hunter')
            bounty_hunter.fear = 0

    elif ogre.fear == 10:
        fear.append('Ogre')
        if 'Ogre' in box:
            box.remove('Ogre')
            ogre.fear = 0

    elif fairy.fear == 10:
        fear.append('Fairy')
        if 'Fairy' in box:
            box.remove('Fairy')
            fairy.fear = 0

    elif dark_elf.fear == 10:
        fear.append('Dark Elf')
        if 'Dark Elf' in box:
            box.remove('Dark Elf')
            dark_elf.fear = 0

    elif bard.fear == 10:
        fear.append('Bard')
        if 'Bard' in box:
            box.remove('Bard')
            bard.fear = 0

    elif rogue.fear == 10:
        fear.append('Rogue')
        if 'Rogue' in box:
            box.remove('Rogue')
            rogue.fear = 0

    elif paladin.fear == 10:
        fear.append('Paladin')
        if 'Paladin' in box:
            box.remove('Paladin')
            paladin.fear = 0

    elif archer.fear == 10:
        fear.append('Archer')
        if 'Archer' in box:
            box.remove('Archer')
            archer.fear = 0

    elif troll.fear == 10:
        fear.append('Troll')
        if 'Troll' in box:
            box.remove('Troll')
            troll.fear = 0

    elif vampire.fear == 10:
        fear.append('Vampire')
        if 'Vampire' in box:
            box.remove('Vampire')
            vampire.fear = 0

    elif sorceress.fear == 10:
        fear.append('Sorceress')
        if 'Ghost Knight' in box:
            box.remove('Sorceress')
            sorceress.fear = 0

    elif ent.fear == 10:
        fear.append('Ent')
        if 'Ent' in box:
            box.remove('Ent')
            ent.fear = 0
    return box, fear

def get_prepare(characters, box, freezer, fear, he_returned):
    while True:
        player1 = []
        player2 = []
        pleya1 = []
        for i in characters:
            if i['Player'] == 'Player1':
                if i['Class'].life > 0:
                    player1.append({'Name': i['Name'], 'Class': i['Class']})
            elif i['Player'] == 'Player2':
                if i['Class'].life > 0:
                    player2.append({'Name': i['Name'], 'Class': i['Class']})
            if i['Player'] == 'Player1':
                pleya1.append(i['Name'])

#creepers
        if wizard.creepers == 1 and ent.life > 0:
            wizard.speed = 0
        else:
            wizard.speed = wizard_speed_max
        if warrior.creepers == 1 and ent.life > 0:
            warrior.speed = 0
        else:
            warrior.speed = warrior_speed_max
        if fairy.creepers == 1 and ent.life > 0:
            fairy.speed = 0
        else:
            fairy.speed = fairy_speed_max
        if bounty_hunter.creepers == 1 and ent.life > 0:
            bounty_hunter.speed = 0
        else:
            bounty_hunter.speed = bounty_hunter_speed_max
        if ogre.creepers == 1 and ent.life > 0:
            ogre.speed = 0
        else:
            ogre.speed = ogre_speed_max
        if rogue.creepers == 1 and ent.life > 0:
            rogue.speed = 0
        else:
            rogue.speed = rogue_speed_max
        if dark_elf.creepers == 1 and ent.life > 0:
            dark_elf.speed = 0
        else:
            dark_elf.speed = dark_elf_speed_max
        if bard.creepers == 1 and ent.life > 0:
            bard.speed = 0
        else:
            bard.speed = bard_speed_max
        if paladin.creepers == 1 and ent.life > 0:
            paladin.speed = 0
        else:
            paladin.speed = paladin_speed_max
        if archer.creepers == 1 and ent.life > 0:
            archer.speed = 0
        else:
            archer.speed = archer_speed_max
        if troll.creepers == 1 and ent.life > 0:
            troll.speed = 0
        else:
            troll.speed = troll_speed_max
        if vampire.creepers == 1 and ent.life > 0:
            vampire.speed = 0
        else:
            vampire.speed = vampire_speed_max
        if ghost_k.creepers == 1 and ent.life > 0:
            ghost_k.speed = 0
        else:
            ghost_k.speed = ghost_k_speed_max
        if sorceress.creepers == 1 and ent.life > 0:
            sorceress.speed = 0
        else:
            sorceress.speed = sorceress_speed_max

        if archer.life <= 0 and 'Archer' in box:
            box.remove('Archer')
        if warrior.life <= 0 and 'Warrior' in box:
            box.remove('Warrior')
        if wizard.life <= 0 and 'Wizard' in box:
            box.remove('Wizard')
        if bounty_hunter.life <= 0 and 'Witch Hunter' in box:
            box.remove('Witch Hunter')
        if ogre.life <= 0 and 'Ogre' in box:
            box.remove('Ogre')
        if fairy.life <= 0 and 'Fairy' in box:
            box.remove('Fairy')
        if dark_elf.life <= 0 and 'Dark Elf' in box:
            box.remove('Dark Elf')
        if bard.life <= 0 and 'Bard' in box:
            box.remove('Bard')
        if paladin.life <= 0 and 'Paladin' in box:
            box.remove('Paladin')
        if rogue.life <= 0 and 'Rogue' in box:
            box.remove('Rogue')
        if troll.life <= 0 and 'Troll' in box:
            box.remove('Troll')
        if vampire.life <= 0 and 'Vampire' in box:
            box.remove('Vampire')
        if ghost_k.life <= 0 and 'Ghost Knight' in box:
            box.remove('Ghost Knight')
        if sorceress.life <= 0 and 'Sorceress' in box:
            box.remove('Sorceress')
        if ent.life <= 0 and 'Ent' in box:
            box.remove('Ent')
        for i in he_returned:
            box.append(i)
        if len(box) > 0:
            print(f'Initiative: {box}')
            for name in player1:
                if name['Name'] in fear and name['Name'] not in box:
                    print(f'\n🦇🟣  {colored(name['Name'], 'magenta')} is fearing! 🟣🦇\n')
                if name['Name'] in freezer and name['Name'] not in box:
                    print(f'\n❄️  {colored(name['Name'], 'magenta')} is frozen! ❄️\n')

            for name in player2:
                if name['Name'] in fear and name['Name'] not in box:
                    print(f'\n🦇🟣  {colored(name['Name'], 'cyan')} is fearing! 🟣🦇\n')
                if name['Name'] in freezer and name['Name'] not in box:
                    print(f'\n❄️  {colored(name['Name'], 'cyan')} is frozen! ❄️\n')

            my_player1 = []
            my_player2 = []
            print('    Player1:')
            for i in player1:
                if i['Class'].life > 0:
                    my_player1.append(f"    {colored(i['Name'], 'magenta')}{int(13-len(i['Name'])) * ' '} {i['Class'].strength * '🔴'} {colored(i['Class'].strength, 'red', attrs=['bold'])} {i['Class'].defend * '🛡️ '} {colored(i['Class'].defend, 'cyan', attrs=['bold'])} {i['Class'].craft * '🔵'} {colored(i['Class'].craft, 'blue', attrs=['bold']) if i['Class'].craft > 0 else  i['Class'].speed * '🟡'} {colored(i['Class'].speed, 'yellow', attrs=['bold']) if i['Class'].craft == 0 else''} {i['Class'].life * '🟢' if i['Class'].craft == 0 else''} {colored(i['Class'].life, 'green', attrs=['bold']) if i['Class'].craft == 0 else''}{i['Class'].speed * '🟡' if i['Class'].craft > 0 else''} {colored(i['Class'].speed, 'yellow', attrs=['bold']) if i['Class'].craft > 0 else''} {i['Class'].life * '🟢' if i['Class'].craft > 0 else ''} {colored(i['Class'].life, 'green', attrs=['bold']) if i['Class'].craft > 0 else''}\n")
            for i in my_player1:
                print(i)
            print('\n    Player2:')
            for i in player2:
                if i['Class'].life > 0:
                    my_player2.append(f"    {colored(i['Name'], 'cyan')}{int(13-len(i['Name'])) * ' '} {i['Class'].strength * '🔴'} {colored(i['Class'].strength, 'red', attrs=['bold'])} {i['Class'].defend * '🛡️ '} {colored(i['Class'].defend, 'cyan', attrs=['bold'])} {i['Class'].craft * '🔵'} {colored(i['Class'].craft, 'blue', attrs=['bold']) if i['Class'].craft > 0 else  i['Class'].speed * '🟡'} {colored(i['Class'].speed, 'yellow', attrs=['bold']) if i['Class'].craft == 0 else''} {i['Class'].life * '🟢' if i['Class'].craft == 0 else''} {colored(i['Class'].life, 'green', attrs=['bold']) if i['Class'].craft == 0 else''}{i['Class'].speed * '🟡' if i['Class'].craft > 0 else''} {colored(i['Class'].speed, 'yellow', attrs=['bold']) if i['Class'].craft > 0 else''} {i['Class'].life * '🟢' if i['Class'].craft > 0 else ''} {colored(i['Class'].life, 'green', attrs=['bold']) if i['Class'].craft > 0 else''}\n")
            for i in my_player2:
                print(i)

        return box, pleya1

def face_off(box, pleya1, attacker, defending, won, vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, p1, p2, warrior_only_once, wizard_only_once, bounty_hunter_only_once, ogre_only_once, fairy_only_once, dark_elf_only_once, bard_only_once, rogue_only_once, paladin_only_once, archer_only_once, troll_only_once, vampire_only_once, ghost_k_only_once, sorceress_only_once, ent_only_once, fear):
    if attacker.special == 'sorceress' and mana == 4:
        attacker.thunder -= 1
    if attacker.special == 'sorceress' and won == 'freeze':
        attacker.freeze -= 1
    if paladin_life == 10 and paladin.life < paladin_life_max:
        paladin.life += 1
        print('\n💚 Paladin heal up himself 💚\n')
    if critical > 0 and vampire_life == 1 and vampire.life < vampire_life_max:
        vampire.life +=1
        print('\n🩸 Vampire heal up himself 🩸\n')
    if won == 'attacker':
        defending.life -= 1
        defending.life -= critical
    if mana == 0:
        if box[0] == 'Wizard':
            if wizard_mana_max > wizard.mana:
                wizard.mana += 1
        elif box[0] == 'Witch Hunter':
            if bounty_hunter_mana_max > bounty_hunter.mana:
                bounty_hunter.mana += 1
        elif box[0] == 'Fairy':
            if fairy_mana_max > fairy.mana:
                fairy.mana += 1
        elif box[0] == 'Dark Elf':
            if dark_elf_mana_max > dark_elf.mana:
                dark_elf.mana += 1
        elif box[0] == 'Bard':
            if bard_mana_max > bard.mana:
                bard.mana += 1
        elif box[0] == 'Rogue':
            if rogue_mana_max > rogue.mana:
                rogue.mana += 1
        elif box[0] == 'Paladin':
            if paladin_mana_max > paladin.mana:
                paladin.mana += 1
        elif box[0] == 'Ghost Knight':
            if ghost_k_mana_max > ghost_k.mana:
                ghost_k.mana += 1
        elif box[0] == 'Sorceress':
            if sorceress_mana_max > sorceress.mana:
                sorceress.mana += 1
    else:
        if box[0] == 'Wizard':
            wizard.mana -= mana
        elif box[0] == 'Witch Hunter':
            bounty_hunter.mana -= mana
        elif box[0] == 'Fairy':
            fairy.mana -= mana
        elif box[0] == 'Dark Elf':
            dark_elf.mana -= mana
        elif box[0] == 'Bard':
            bard.mana -= mana
        elif box[0] == 'Rogue':
            rogue.mana -= mana
        elif box[0] == 'Paladin':
            paladin.mana -= mana
        elif box[0] == 'Ghost Knight':
            ghost_k.mana -= mana
        elif box[0] == 'Sorceress':
            sorceress.mana -= mana
    if vim == 0:
        if box[0] == 'Warrior':
            if warrior_vim_max > warrior.vim:
                warrior.vim += 1
        elif box[0] == 'Troll':
            if troll_vim_max > troll.vim:
                troll.vim += 1
        elif box[0] == 'Wizard':
            if wizard_vim_max > wizard.vim:
                wizard.vim += 1
        elif box[0] == 'Witch Hunter':
            if bounty_hunter_vim_max > bounty_hunter.vim:
                bounty_hunter.vim += 1
        elif box[0] == 'Ogre':
            if ogre_vim_max > ogre.vim:
                ogre.vim += 1
        elif box[0] == 'Fairy':
            if fairy_vim_max > fairy.vim:
                fairy.vim += 1
        elif box[0] == 'Dark Elf':
            if dark_elf_vim_max > dark_elf.vim:
                dark_elf.vim += 1
        elif box[0] == 'Bard':
            if bard_vim_max > bard.vim:
                bard.vim += 1
        elif box[0] == 'Rogue':
            if rogue_vim_max > rogue.vim:
                rogue.vim += 1
        elif box[0] == 'Paladin':
            if paladin_vim_max > paladin.vim:
                paladin.vim += 1
        elif box[0] == 'Archer':
            if archer_vim_max > archer.vim:
                archer.vim += 1
        elif box[0] == 'Vampire':
            if vampire_vim_max > vampire.vim:
                vampire.vim += 1
        elif box[0] == 'Ghost Knight':
            if ghost_k_vim_max > ghost_k.vim:
                ghost_k.vim += 1
        elif box[0] == 'Sorceress':
            if sorceress_vim_max > sorceress.vim:
                sorceress.vim += 1
        elif box[0] == 'Ent':
            if ent_vim_max > ent.vim:
                ent.vim += 1
    else:
        if box[0] == 'Warrior':
            warrior.vim -= vim
        elif box[0] == 'Troll':
            troll.vim -= vim
        elif box[0] == 'Wizard':
            wizard.vim -= vim
        elif box[0] == 'Witch Hunter':
            bounty_hunter.vim -= vim
        elif box[0] == 'Ogre':
            ogre.vim -= vim
        elif box[0] == 'Fairy':
            fairy.vim -= vim
        elif box[0] == 'Dark Elf':
            dark_elf.vim -= vim
        elif box[0] == 'Bard':
            bard.vim -= vim
        elif box[0] == 'Rogue':
            rogue.vim -= vim
        elif box[0] == 'Paladin':
            paladin.vim -= vim
        elif box[0] == 'Archer':
            archer.vim -= vim
        elif box[0] == 'Vampire':
            vampire.vim -= vim
        elif box[0] == 'Ghost Knight':
            ghost_k.vim -= vim
        elif box[0] == 'Sorceress':
            sorceress.vim -= vim
        elif box[0] == 'Ent':
            ent.vim -= vim

    if warrior.life <= 0 and warrior_only_once == 0:
        print('💀 Warrior died! 💀')
        warrior_only_once += 1
        if 'Warrior' in pleya1:
            p2 += 1
        else:
            p1 += 1
    if troll.life <= 0 and troll_only_once == 0:
        print('💀 Troll died! 💀')
        troll_only_once += 1
        if 'Troll' in pleya1:
            p2 += 1
        else:
            p1 += 1
    if wizard.life <= 0 and wizard_only_once == 0:
        if 'Wizard' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Wizard died! 💀')
        wizard_only_once += 1
    if bounty_hunter.life <= 0 and bounty_hunter_only_once == 0:
        if 'Witch Hunter' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Witch Hunter died! 💀')
        bounty_hunter_only_once += 1
    if ogre.life <= 0 and ogre_only_once == 0:
        if 'Ogre' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Ogre died! 💀')
        ogre_only_once += 1
    if fairy.life <= 0 and fairy_only_once == 0:
        if 'Fairy' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Fairy died! 💀')
        fairy_only_once += 1
    if dark_elf.life <= 0 and dark_elf_only_once == 0:
        if 'Dark Elf' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Dark Elf died! 💀')
        dark_elf_only_once += 1
    if bard.life <= 0 and bard_only_once == 0:
        if 'Bard' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Bard died! 💀')
        bard_only_once += 1
    if rogue.life <= 0 and rogue_only_once == 0:
        if 'Rogue' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Rogue died! 💀')
        rogue_only_once += 1
    if paladin.life <= 0 and paladin_only_once == 0:
        if 'Paladin' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Paladin died! 💀')
        paladin_only_once += 1
    if archer.life <= 0 and archer_only_once == 0:
        if 'Archer' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Archer died! 💀')
        archer_only_once += 1
    if vampire.life <= 0 and vampire_only_once == 0:
        if 'Vampire' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Vampire died! 💀')
        vampire_only_once +=1
    if ghost_k.life <= 0 and ghost_k_only_once == 0:
        if 'Ghost Knight' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Ghost Knight died! 💀')
        ghost_k_only_once +=1
    if sorceress.life <= 0 and sorceress_only_once == 0:
        if 'Sorceress' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Sorceress died! 💀')
        sorceress_only_once +=1
    if ent.life <= 0 and ent_only_once == 0:
        if 'Ent' in pleya1:
           p2 += 1
        else:
           p1 += 1
        print('💀 Ent died! 💀')
        ent_only_once +=1
#freeze
    if won == 'freeze' and defending.special == 'wizard' and 'Wizard' in box:
        box.remove('Wizard')
        freezer.append('Wizard')
    elif won == 'freeze' and defending.special == 'wizard':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'warrior' and 'Warrior' in box:
        box.remove('Warrior')
        freezer.append('Warrior')
    elif won == 'freeze' and defending.special == 'warrior':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'witch hunter' and 'Witch Hunter' in box:
        box.remove('Witch Hunter')
        freezer.append('Witch Hunter')
    elif won == 'freeze' and defending.special == 'witch hunter':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'ogre' and 'Ogre' in box:
        box.remove('Ogre')
        freezer.append('Ogre')
    elif won == 'freeze' and defending.special == 'ogre' and 'Ogre':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'fairy' and 'Fairy' in box:
        box.remove('Fairy')
        freezer.append('Fairy')
    elif won == 'freeze' and defending.special == 'fairy':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'dark elf' and 'Dark Elf' in box:
        box.remove('Dark Elf')
        freezer.append('Dark Elf')
    elif won == 'freeze' and defending.special == 'dark elf':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'bard' and 'Bard' in box:
        box.remove('Bard')
        freezer.append('Bard')
    elif won == 'freeze' and defending.special == 'bard':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'rogue' and 'Rogue' in box:
        box.remove('Rogue')
        freezer.append('Rogue')
    elif won == 'freeze' and defending.special == 'rogue':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'paladin' and 'Paladin' in box:
        box.remove('Paladin')
        freezer.append('Paladin')
    elif won == 'freeze' and defending.special == 'paladin':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'archer' and 'Archer' in box:
        box.remove('Archer')
        freezer.append('Archer')
    elif won == 'freeze' and defending.special == 'archer':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'troll' and 'Troll' in box:
        box.remove('Troll')
        freezer.append('Troll')
    elif won == 'freeze' and defending.special == 'troll':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'vampire' and 'Vampire' in box:
        box.remove('Vampire')
        freezer.append('Vampire')
    elif won == 'freeze' and defending.special == 'vampire':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'ghost knight' and 'Ghost Knight' in box:
        box.remove('Ghost Knigth')
        freezer.append('Ghost Knight')
    elif won == 'freeze' and defending.special == 'ghost knight':
        defending.freeze = 10

    if won == 'freeze' and defending.special == 'ent' and 'Ent' in box:
        box.remove('Ent')
        freezer.append('Ent')
    elif won == 'freeze' and defending.special == 'ent':
        defending.freeze = 10

#fearing
    if fearing == 'fear' and defending.special == 'wizard' and 'Wizard' in box:
        box.remove('Wizard')
        fear.append('Wizard')
    elif fearing == 'fear' and defending.special == 'wizard':
        defending.fear = 10
    if fearing == 'fear' and defending.special == 'warrior' and 'Warrior' in box:
        box.remove('Warrior')
        fear.append('Warrior')
    elif fearing == 'fear' and defending.special == 'warrior':
        defending.fear = 10
    if fearing == 'fear' and defending.special == 'witch hunter' and 'Witch Hunter' in box:
        box.remove('Witch Hunter')
        fear.append('Witch Hunter')
    elif fearing == 'fear' and defending.special == 'witch hunter':
        defending.fear = 10
    if fearing == 'fear' and defending.special == 'ogre' and 'Ogre' in box:
         box.remove('Ogre')
         fear.append('Ogre')
    elif fearing == 'fear' and defending.special == 'ogre' and 'Ogre':
         defending.fear = 10
    if fearing == 'fear' and defending.special == 'fairy' and 'Fairy' in box:
         box.remove('Fairy')
         fear.append('Fairy')
    elif fearing == 'fear' and defending.special == 'fairy':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'dark elf' and 'Dark Elf' in box:
         box.remove('Dark Elf')
         fear.append('Dark Elf')
    elif fearing == 'fear' and defending.special == 'dark elf':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'bard' and 'Bard' in box:
         box.remove('Bard')
         fear.append('Bard')
    elif fearing == 'fear' and defending.special == 'bard':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'rogue' and 'Rogue' in box:
         box.remove('Rogue')
         fear.append('Rogue')
    elif fearing == 'fear' and defending.special == 'rogue':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'paladin' and 'Paladin' in box:
         box.remove('Paladin')
         fear.append('Paladin')
    elif fearing == 'fear' and defending.special == 'paladin':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'archer' and 'Archer' in box:
         box.remove('Archer')
         fear.append('Archer')
    elif fearing == 'fear' and defending.special == 'archer':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'troll' and 'Troll' in box:
         box.remove('Troll')
         fear.append('Troll')
    elif fearing == 'fear' and defending.special == 'troll':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'vampire' and 'Vampire' in box:
         box.remove('Vampire')
         fear.append('Vampire')
    elif fearing == 'fear' and defending.special == 'vampire':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'ghost knight' and 'Ghost Knight' in box:
         box.remove('Ghost Knigth')
         fear.append('Ghost Knight')
    elif fearing == 'fear' and defending.special == 'ghost knight':
         defending.fear = 10

    if fearing == 'fear' and defending.special == 'ent' and 'Ent' in box:
         box.remove('Ent')
         fear.append('Ent')
    elif fearing == 'fear' and defending.special == 'ent':
         defending.fear = 10

    if box[0] == 'Wizard':
        box.remove('Wizard')
    elif box[0] == 'Warrior':
        box.remove('Warrior')
    elif box[0] == 'Witch Hunter':
        box.remove('Witch Hunter')
    elif box[0] == 'Ogre':
        box.remove('Ogre')
    elif box[0] == 'Fairy':
        box.remove('Fairy')
    elif box[0] == 'Dark Elf':
        box.remove('Dark Elf')
    elif box[0] == 'Bard':
        box.remove('Bard')
    elif box[0] == 'Rogue':
        box.remove('Rogue')
    elif box[0] == 'Paladin':
        box.remove('Paladin')
    elif box[0] == 'Archer':
        box.remove('Archer')
    elif box[0] == 'Troll':
        box.remove('Troll')
    elif box[0] == 'Vampire':
        box.remove('Vampire')
    elif box[0] == 'Ghost Knight':
        box.remove('Ghost Knight')
    elif box[0] == 'Sorceress':
        box.remove('Sorceress')
    elif box[0] == 'Ent':
        box.remove('Ent')

    if magic_dust == 3:
        print('\n✨✨✨ Magic Dust ✨✨✨\n')
        box.append('Fairy')
    return box, p1, p2, fear, warrior_only_once, wizard_only_once, bounty_hunter_only_once, ogre_only_once, fairy_only_once, dark_elf_only_once, bard_only_once, rogue_only_once, paladin_only_once, archer_only_once, troll_only_once, vampire_only_once, ghost_k_only_once, sorceress_only_once, ent_only_once


def get_player_attack(vim, mana, life, player2_life, attacker, defending, pleya1, characters, freezer, fear, box, temp_box, temp_box_2):
    he_returned = []
    he_was = 'no'
    attacker.creepers = 0
    attacker.fear = 0
    fearing = 'no fear'
    if 'Bard' in box:
        while True:
            if 'Bard' in freezer:
                freezer.remove('Bard')
            else:
                break
    if 'Warrior' in box:
        while True:
            if 'Warrior' in freezer:
                freezer.remove('Warrior')
            else:
                break

    if 'Wizard' in box:
        while True:
            if 'Wizard' in freezer:
                freezer.remove('Wizard')
            else:
                break

    if 'Ghost Knight' in box:
        while True:
            if 'Ghost Knight' in freezer:
                freezer.remove('Ghost Knight')
            else:
                break

    if 'Vampire' in box:
        while True:
            if 'Vampire' in freezer:
                freezer.remove('Vampire')
            else:
                break

    if 'Fairy' in box:
        while True:
            if 'Fairy' in freezer:
                freezer.remove('Fairy')
            else:
                break

    if 'Archer' in box:
        while True:
            if 'Archer' in freezer:
                freezer.remove('Archer')
            else:
                break

    if 'Ent' in box:
        while True:
            if 'Ent' in freezer:
                freezer.remove('Ent')
            else:
                break

    if 'Paladin' in box:
        while True:
            if 'Paladin' in freezer:
                freezer.remove('Paladin')
            else:
                break

    if 'Ogre' in box:
        while True:
            if 'Ogre' in freezer:
                freezer.remove('Ogre')
            else:
                break

    if 'Dark Elf' in box:
        while True:
            if 'Dark Elf' in freezer:
                freezer.remove('Dark Elf')
            else:
                break

    if 'Witch Hunter' in box:
        while True:
            if 'Witch Hunter' in freezer:
                freezer.remove('Witch Hunter')
            else:
                break

    if 'Rogue' in box:
        while True:
            if 'Rogue' in freezer:
                freezer.remove('Rogue')
            else:
                break

    if 'Troll' in box:
        while True:
            if 'Troll' in freezer:
                freezer.remove('Troll')
            else:
                break




    if 'Bard' in box:
        while True:
            if 'Bard' in fear:
                fear.remove('Bard')
            else:
                break
    if 'Warrior' in box:
        while True:
            if 'Warrior' in fear:
                fear.remove('Warrior')
            else:
                break

    if 'Wizard' in box:
        while True:
            if 'Wizard' in fear:
                fear.remove('Wizard')
            else:
                break

    if 'Sorceress' in box:
        while True:
            if 'Sorceress' in fear:
                fear.remove('Sorceress')
            else:
                break

    if 'Vampire' in box:
        while True:
            if 'Vampire' in fear:
                fear.remove('Vampire')
            else:
                break

    if 'Fairy' in box:
        while True:
            if 'Fairy' in fear:
                fear.remove('Fairy')
            else:
                break

    if 'Archer' in box:
        while True:
            if 'Archer' in fear:
                fear.remove('Archer')
            else:
                break
    if 'Ent' in box:
        while True:
            if 'Ent' in fear:
                fear.remove('Ent')
            else:
                break

    if 'Paladin' in box:
        while True:
            if 'Paladin' in fear:
                fear.remove('Paladin')
            else:
                break

    if 'Ogre' in box:
        while True:
            if 'Ogre' in fear:
                fear.remove('Ogre')
            else:
                break

    if 'Dark Elf' in box:
        while True:
            if 'Dark Elf' in fear:
                fear.remove('Dark Elf')
            else:
                break

    if 'Witch Hunter' in box:
        while True:
            if 'Witch Hunter' in fear:
                fear.remove('Witch Hunter')
            else:
                break
    if 'Rogue' in box:
        while True:
            if 'Rogue' in fear:
                fear.remove('Rogue')
            else:
                break

    if 'Troll' in box:
        while True:
            if 'Troll' in fear:
                fear.remove('Troll')
            else:
                break

    magic_dust = 0
    if attacker.special == 'fairy':
        magic_dust = random.randint(1,3)
    paladin_life = 0
    vampire_life = 0
    if player2_life == None and defending == None:
        return None, 0, 0, 0, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
    mandolin_attack = 0
    mandolin_defense = 0
    mandolin_craft = 0
    player1 = []
    for i in pleya1:
        i = i.lower()
        player1.append(i)
    if attacker.special == 'paladin':
        paladin_life = random.randint(8,10)
    magic_craft = random.choice(['attack', 'defend', 'craft'])
    for i in characters:
        if i['Name'] == 'Bard':
            if i['Class'].life > 0 and 'Bard' in pleya1 and i['Name'] not in freezer and i['Name'] not in fear:
                if attacker.special in player1:
                    if magic_craft == 'attack' and attacker.special == 'bard':
                        mandolin_attack = random.choice([8,8,8,8,8,8,8,8,30])
                    elif magic_craft == 'attack':
                        mandolin_attack = random.choice([2,2,2,2,3,3,3,4,4,15])
                    elif magic_craft == 'craft' and attacker.special == 'bard':
                        mandolin_craft = random.choice([8,8,8,8,8,8,8,8,30])
                    elif magic_craft == 'craft':
                        mandolin_craft = random.choice([2,2,2,2,3,3,3,4,4,15])
                elif defending.special in player1:
                    if magic_craft == 'defend' and defending.special == 'bard':
                        mandolin_defense = random.choice([8,8,8,8,8,8,8,8,30])
                    elif magic_craft == 'defend':
                        mandolin_defense = random.choice([2,2,2,2,3,3,3,4,4,15])
            elif i['Class'].life > 0 and 'Bard' not in pleya1 and i['Name'] not in freezer and i['Name'] not in fear:
                if attacker.special not in player1:
                    if magic_craft == 'attack' and attacker.special == 'bard':
                        mandolin_attack = random.choice([8,8,8,8,8,8,8,8,30])
                    elif magic_craft == 'attack':
                        mandolin_attack = random.choice([2,2,2,2,3,3,3,4,4,15])
                    elif magic_craft == 'craft' and attacker.special == 'bard':
                        mandolin_craft = random.choice([8,8,8,8,8,8,8,8,30])
                    elif magic_craft == 'craft':
                        mandolin_craft = random.choice([2,2,2,2,3,3,3,4,4,15])
                elif defending.special not in player1:
                    if magic_craft == 'defend' and defending.special == 'bard':
                        mandolin_defense = random.choice([8,8,8,8,8,8,8,8,30])
                    elif magic_craft == 'defend':
                        mandolin_defense = random.choice([2,2,2,2,3,3,3,4,4,15])

    while True:
        if attacker.special.title() in pleya1:
            print(f'\n{colored(defending, 'cyan')}:\nStrength:{int(9-len('strength')) * ' '}{defending.strength*'🔴'}  {colored(defending.strength, 'red', attrs=['bold'])}\nDefence:{int(9-len('defence')) * ' '}{defending.defend *'🛡️ '}  {colored(defending.defend, 'cyan', attrs=['bold'])}\nCraft:{int(9-len('craft')) * ' '}{defending.craft*'🔵'}  {colored(defending.craft, 'blue', attrs=['bold']) if defending.craft > 0 else ''}\nSpeed:{int(9-len('speed')) * ' '}{defending.speed*'🟡'}  {colored(defending.speed, 'yellow', attrs=['bold'])}\nLife:{int(9-len('life')) * ' '}{player2_life*'🟢'}  {colored(defending.life, 'green', attrs=['bold'])}\n')
            print(f'\n{colored(attacker, 'magenta')}:\nStrength:{int(9-len('strength')) * ' '}{attacker.strength*'🔴'}  {colored(attacker.strength, 'red', attrs=['bold'])}\nDefence:{int(9-len('defence')) * ' '}{attacker.defend *'🛡️ '}  {colored(attacker.defend, 'cyan', attrs=['bold'])}\nCraft:{int(9-len('craft')) * ' '}{attacker.craft*'🔵'}  {colored(attacker.craft, 'blue', attrs=['bold']) if attacker.craft > 0 else ''}\nSpeed:{int(9-len('speed')) * ' '}{attacker.speed*'🟡'} {colored(attacker.speed, 'yellow', attrs=['bold'])}\nStamina:{int(9-len('stamina')) * ' '}{vim*'🟪'}\nMana:{int(9-len('mana')) * ' '}{mana*'🧊'}\nLife:{int(9-len('life')) * ' '}{life*'🟢'} {colored(attacker.life, 'green', attrs=['bold'])}\n{9*' '} {attacker.shots*'🏹'}\n{9*' '} {attacker.freeze*'❄️ '}\n{9*' '} {attacker.thunder*'🗲 '}')
            attack = input(f'{colored(attacker, 'magenta')} attack: ').lower().strip()
        else:
            print(f'\n{colored(defending, 'magenta')}:\nStrength:{int(9-len('strength')) * ' '}{defending.strength*'🔴'}  {colored(defending.strength, 'red', attrs=['bold'])}\nDefence:{int(9-len('defence')) * ' '}{defending.defend *'🛡️ '}  {colored(defending.defend, 'cyan', attrs=['bold'])}\nCraft:{int(9-len('craft')) * ' '}{defending.craft*'🔵'}  {colored(defending.craft, 'blue', attrs=['bold']) if defending.craft > 0 else ''}\nSpeed:{int(9-len('speed')) * ' '}{defending.speed*'🟡'}  {colored(defending.speed, 'yellow', attrs=['bold'])}\nLife:{int(9-len('life')) * ' '}{player2_life*'🟢'}  {colored(defending.life, 'green', attrs=['bold'])}\n')
            print(f'\n{colored(attacker, 'cyan')}:\nStrength:{int(9-len('strength')) * ' '}{attacker.strength*'🔴'}  {colored(attacker.strength, 'red', attrs=['bold'])}\nDefence:{int(9-len('defence')) * ' '}{attacker.defend *'🛡️ '}  {colored(attacker.defend, 'cyan', attrs=['bold'])}\nCraft:{int(9-len('craft')) * ' '}{attacker.craft*'🔵'}  {colored(attacker.craft, 'blue', attrs=['bold']) if attacker.craft > 0 else ''}\nSpeed:{int(9-len('speed')) * ' '}{attacker.speed*'🟡'} {colored(attacker.speed, 'yellow', attrs=['bold'])}\nStamina:{int(9-len('stamina')) * ' '}{vim*'🟪'}\nMana:{int(9-len('mana')) * ' '}{mana*'🧊'}\nLife:{int(9-len('life')) * ' '}{life*'🟢'} {colored(attacker.life, 'green', attrs=['bold'])}\n{9*' '} {attacker.shots*'🏹'}\n{9*' '} {attacker.freeze*'❄️ '}\n{9*' '} {attacker.thunder*'🗲 '}')
            attack = input(f'{colored(attacker, 'cyan')} attack: ').lower().strip()
        archer_headshot = 0
        vampire_hunter = 0



# strength attack
        if attack == 's' and vim > 0 or attack == 'strength' and vim > 0:
            if attacker.special == 'ent':
                defending.creepers = 1
                defending.speed = 0
#faer
            if attacker.special == 'ghost knight':
                if defending.special == 'bard' or defending.special == 'fairy':
                    my_fear = random.randint(4,5)
                elif defending.special == 'archer' or defending.special == 'rogue' or defending.special == 'ent' or defending.special == 'troll':
                    my_fear = random.randint(3,5)
                elif defending.special == 'sorceress':
                    my_fear = random.randint(1,5)
                elif defending.special == 'paladin' or defending.special == 'witch hunter':
                    my_fear = 0
                else:
                    my_fear = random.randint(2,5)
                if my_fear == 5:
                    fearing = 'fear'
            bow = 'no'
            a = attacker.strength
            if attacker.special == 'bard' or attacker.special == 'fairy' or attacker.special == 'wizard' or attacker.special == 'archer':
                add = random.randint(1,4)
            elif attacker.special == 'ent':
                add = random.randint(1,7)
            elif attacker.special == 'dark elf' or attacker.special == 'ghost knight':
                add = random.randint(1,10)
            elif attacker.special == 'rogue' or attacker.special == 'troll' or attacker.special == 'vampire' or attacker.special == 'ogre':
                add = random.randint(1,15)
            elif attacker.special == 'warrior':
                add = random.randint(3,17)
            else:
                add = random.randint(1,6)
            if defending.special == 'vampire':
                if attacker.special == 'paladin':
                    vampire_hunter += 10
                elif attacker.special == 'witch hunter':
                    vampire_hunter += 10
            if defending.special == 'ghost knight':
                if attacker.special == 'paladin':
                    vampire_hunter += 7
            full_attack = a + add + mandolin_attack + vampire_hunter
            if mandolin_attack > 0:
                print('🪕🪕🪕🪕🪕🪕🪕🪕🪕 MAAAAAAAAAAAAAGIC MAAAAAAAAAAAAAAANDOLLLIIIIIIIIIIIIIIIIIIIIIIIIIIIIIN! 🪕🪕🪕🪕🪕🪕🪕🪕🪕')
            if attacker.special == 'witch hunter' and defending.special != 'rogue':
                full_attack += round(defending.craft * 1.4)
#archer
            double_arrow = random.randint(1,3)
            fire_arrow = random.randint(1,10)
            if attacker.special == 'archer' and attacker.shots > 0:
                bow = input('Do you want use a bow? ').lower()
                if bow == 'yes' or  bow == 'y':
                    attacker.shots -= 1
                    full_attack = random.randint(10,25)
                    full_attack += mandolin_attack
                    if defending.special == 'ent':
                        full_attack = random.randint(1,9)
                        full_attack += mandolin_attack
                        fire_arrow = random.randint(9,10)
                    if full_attack >= 24:
                        archer_headshot = 1
                    elif fire_arrow == 10:
                        full_attack += 20
                        print('\n🔥🔥🔥 🏹 Fire Arrow 🏹 🔥🔥🔥')
                    elif double_arrow == 3:
                        attacker.shots -= 1
                        full_attack += 3
                        print('\nDouble Arrow 🏹 🏹')
                elif bow == 'n' or bow == 'no':
                    archer_strength = input('Do you can use strength? ').lower()
                    if archer_strength == 'y' or archer_strength == 'yes':
                        pass
                    elif archer_strength == 'n' or archer_strength == 'no':
                        return None, 0, 0, 0, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
            fire_angel = random.randint(1,8)
            last_bastion = random.randint(1,4)
            last_breath = random.randint(1,3)
            destiny_sword = random.randint(1,3)
            fire_sword = random.randint(1,3)
            magic_sword = random.randint(1,3)
            vampire_fury = random.randint(1,5)
            troll_smash = random.randint(1,5)
            ghost_k_dark = random.randint(1,5)
            call = random.randint(1,5)
            if bow == 'y' or bow == 'yes':
                if archer_headshot == 1:
                    print(p.renderText(f"Dead eye!"))
                else:
                    print(p.renderText(f'Hawkaye    {full_attack}'))

            elif attacker.special == 'ogre' and call == 5:
                full_attack = random.randint(17,43)
                print(p.renderText(f'Call of the blood  {full_attack}'))

            elif attacker.special == 'ghost knight' and ghost_k_dark == 5:
                full_attack += 20
                print(p.renderText(f'Darkness of Knight  {full_attack}'))

            elif attacker.special == 'troll' and troll_smash == 5:
                full_attack += 30
                print(p.renderText(f'Troll Smash  {full_attack}'))

            elif attacker.special == 'vampire' and vampire_fury == 5:
                full_attack += 20
                print(p.renderText(f'Vampire Fury  {full_attack}'))

            elif attacker.special == 'paladin' and last_breath == 3 and attacker.life <= 2:
                full_attack += 30
                print(p.renderText(f'Last Breath  {full_attack}'))

            elif attacker.special == 'paladin' and attacker.mana >= 0 and attacker.vim > 0 and fire_angel == 8:
                full_attack += 27
                if defending.special == 'ent':
                    full_attack += 10
                print(p.renderText(f'Fire Angel  {full_attack}'))

            elif attacker.special == 'paladin' and attacker.mana <= 0 and attacker.vim == 1 and last_bastion == 4:
                full_attack += 12
                print(p.renderText(f'Last Bastion  {full_attack}'))

            elif attacker.special == 'paladin' and attacker.mana == 1 and magic_sword == 3:
                full_attack += 8
                print(p.renderText(f"Blessing Hit  {full_attack}"))

            elif attacker.special == 'paladin' and fire_sword == 3:
                full_attack += 6
                if defending.special == 'ent':
                    full_attack += 10
                print(p.renderText(f'Fire Sword  {full_attack}'))

            elif attacker.special == 'paladin' and destiny_sword == 3:
                full_attack += 4
                print(p.renderText(f'Destiny Sword  {full_attack}'))

            else:
                print(p.renderText(f'Attack  {round(full_attack)}'))

            d = defending.defend
            if defending.special.title() in freezer:
                d = 1
            if defending.special == 'dark elf':
                convert = random.choice([1,1,1,1.5,1.5,1.5,1.5,2,2,2,3,3,4,5,10])
                d = round(d * convert)
            if defending.special == 'witch hunter' and attacker.special == 'vampire' or defending.special == 'paladin' and attacker.special == 'vampire':
                d += 7
            elif defending.special == 'paladin' and attacker.special == 'ghost knight':
                d += 4
            elif defending.special == 'fairy':
                if defending.freeze == 0:
                    convert = random.choice([1,1,2,2,4,4,5,5,15])
                    d = d * convert
                    add = random.randint(1,4)
                else:
                    d = 1
                    add = 0
            elif defending.special == 'ogre' or defending.special == 'ghost knight' or defending.special == 'rogue' or defending.special == 'dark elf' or defending.special == 'troll' or defending.special == 'vampire' or defending.special == 'ent':
                add = random.randint(1,8)
            else:
                add = random.randint(1,6)
            full_defence = d + add + mandolin_defense
            if defending.special.title() in fear:
                full_defence -= random.randint(1,6)
            if mandolin_defense > 0:
                print('🪕🪕🪕🪕🪕🪕🪕🪕🪕 MAAAAAAAAAAAAAGIC MAAAAAAAAAAAAAAANDOLLLIIIIIIIIIIIIIIIIIIIIIIIIIIIIIN! 🪕🪕🪕🪕🪕🪕🪕🪕🪕')
            if defending.special == 'fairy':
                print(p.renderText(f'Dodge  {round(full_defence)}'))
            else:
                print(p.renderText(f'Defend  {round(full_defence)}'))
            vim = 1
            mana = 0
            critical = 0
            warrior_breaking = 0
            if archer_headshot == 1:
                critical += 3
                print('Critical!')
                if defending.special.title() in freezer:
                    defending.freeze = 0
                    print(colored('⛓️‍💥 The Ice block is breaking ⛓️‍💥', 'blue'))
                    if defending.special.title() in temp_box or defending.special.title() in temp_box_2:
                        if defending.special.title() in temp_box_2:
                            temp_box_2.remove(defending.special.title())
                        he_returned.append(defending.special.title())
                while True:
                    if defending.special.title() in freezer:
                        freezer.remove(defending.special.title())
                    else:
                        break
            elif full_attack > full_defence:
                if defending.special.title() in freezer:
                    print(colored('⛓️‍💥 The Ice block is breaking ⛓️‍💥', 'blue'))
                    if defending.special.title() in temp_box or defending.special.title() in temp_box_2:
                        if defending.special.title() in temp_box_2:
                            temp_box_2.remove(defending.special.title())
                        he_returned.append(defending.special.title())
                    defending.freeze = 0
                    if defending.special == 'warrior':
                        warrior_breaking = 1
                while True:
                    if defending.special.title() in freezer:
                        freezer.remove(defending.special.title())
                    else:
                        break
                if full_attack >= 40:
                    critical += 3
                    print('Critical')
                elif full_attack >= 22:
                    critical += 2
                    if attacker.special == 'vampire':
                        vampire_life = 1
                    print(f'Critical!')
                elif full_attack >= 17:
                    critical += 1
                    if attacker.special == 'vampire':
                        vampire_life = 1
                    print('Critical!')
            elif full_attack <= full_defence:
                print('Exellent defense! 🧱🧱🧱🧱')
                if 'Warrior' not in fear and 'Warrior' not in freezer:
                    if defending.special == 'warrior' and fearing == 'no fear':
                        get_warrior_counter(defending, attacker, bow, freezer, pleya1)
                return 'defending', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was

            print(f'Hit! 🩸{critical*'🩸'}\n')
            if defending.special == 'ent':
                vampire_life = 0
            if 0 >= player2_life - critical - 1:
                return 'attacker', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
            if attacker.special.title() in pleya1:
                print(f'{colored(attacker, 'magenta')} stats:\nStrength: {attacker.strength * '🔴'} Defence: {attacker.defend *'🛡️ '} Carft: {attacker.craft*'🔵'}\n')
            else:
                print(f'{colored(attacker, 'cyan')} stats:\nStrength: {attacker.strength * '🔴'} Defence: {attacker.defend *'🛡️ '} Carft: {attacker.craft*'🔵'}\n')
            get_you_cant_do_it(defending, pleya1)
            if 'Warrior' not in fear and 'Warrior' not in freezer:
                if defending.special == 'warrior' and fearing == 'no fear' and warrior_breaking == 0:
                    get_warrior_counter(defending, attacker, bow, freezer, pleya1)
            return 'attacker', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was




        elif vim <= 0:
            print(f"{attacker} doesn't have a stamina, try attack by a craft")


# caraft attack
        if attack == 'c' and mana > 0 or attack == 'craft' and mana > 0 and attacker.craft > 0:
            a = attacker.craft
            vampire_hunter = 0
            wizard = 0
            if attacker.special == 'dark elf':
                convert = random.choice([1,1,1.5,1.5,1.5,1.5,2,2,2,3,3,4,5,10])
                a = round(a * convert)
            if attacker.special == 'dark elf' or attacker.special == 'bard':
                add = random.randint(1,8)
            elif attacker.special == 'fairy' or attacker.special == 'sorceress':
                add = random.randint(1,12)
            elif attacker.special == 'wizard':
                add = random.randint(1,15)
            else:
                add = random.randint(1,6)
            if defending.special == 'vampire':
                if attacker.special == 'paladin':
                    vampire_hunter += 7
                elif attacker.special == 'witch hunter':
                    vampire_hunter += 5
            if defending.special == 'ghost knight':
                if attacker.special == 'paladin':
                    vampire_hunter += 4

            full_attack = a + add + mandolin_craft + vampire_hunter
            if attacker.special == 'witch hunter' and defending.special != 'Rogue':
                full_attack += round(defending.craft * 0.9)
            if mandolin_craft > 0:
                print('🪕🪕🪕🪕🪕🪕🪕🪕🪕 MAAAAAAAAAAAAAGIC MAAAAAAAAAAAAAAANDOLLLIIIIIIIIIIIIIIIIIIIIIIIIIIIIIN! 🪕🪕🪕🪕🪕🪕🪕🪕🪕')
            print(p.renderText(f'Attack  {round(full_attack)}'))
            d = defending.defend
            if defending.special.title() in freezer:
                d = 1
            if defending.special == 'dark elf':
                convert = random.choice([1,1,1,1.5,1.5,1.5,1.5,2,2,2,3,3,4,5,10])
                d = round(d * convert)
            if defending.special == 'fairy':
                if defending.freeze == 0:
                    add = random.randint(1,4)
                    convert = random.choice([1,1,2,2,4,4,5,5,15])
                    d = d * convert
                else:
                    d = 1
                    add = 0
            elif defending.special == 'ogre' or defending.special == 'rogue' or defending.special == 'dark elf' or defending.special == 'troll' or defending.special == 'vampire' or defending.special == 'ent':
                add = random.randint(1,8)
            elif defending.special == 'ghost knight':
                add = random.randint(1,12)
            else:
                add = random.randint(1,6)

            if defending.special == 'wizard':
                wizard = attacker.craft

            full_defence = d + add + mandolin_defense + wizard
            if defending.special.title() in fear:
                full_defence -= random.randint(1,6)
            if defending.special == 'witch hunter':
                full_defence += round(attacker.craft * 1.4)
            if mandolin_defense > 0:
                print('🪕🪕🪕🪕🪕🪕🪕🪕🪕 MAAAAAAAAAAAAAGIC MAAAAAAAAAAAAAAANDOLLLIIIIIIIIIIIIIIIIIIIIIIIIIIIIIN! 🪕🪕🪕🪕🪕🪕🪕🪕🪕')
            if defending.special == 'fairy':
                print(p.renderText(f'Dodge  {round(full_defence)}'))
            else:
                print(p.renderText(f'Defend  {round(full_defence)}'))
            mana = 1
            vim = 0
            critical = 0
            if full_attack > full_defence:
                if defending.special.title() in freezer:
                    defending.freeze = 0
                    print(colored('⛓️‍💥 The Ice block is breaking ⛓️‍💥', 'blue'))
                    if defending.special.title() in temp_box or defending.special.title() in temp_box_2:
                        if defending.special.title() in temp_box_2:
                            temp_box_2.remove(defending.special.title())
                        he_returned.append(defending.special.title())
                while True:
                    if defending.special.title() in freezer:
                        freezer.remove(defending.special.title())
                    else:
                        break
                if full_attack >= 40:
                    critical += 3
                    print('Critical')
                elif full_attack >= 22:
                    print('Critical!')
                    critical += 2
                elif full_attack >= 17:
                    critical += 1
                    print('Critical!')
                print(f'Hit! 🩸{critical*'🩸'}\n')
                if 0 >= player2_life - critical - 1:
                    return 'attacker', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
                if attacker.special.title() in pleya1:
                    print(f'{colored(attacker, 'magenta')} stats:\nStrength: {attacker.strength * '🔴'} Defence: {attacker.defend *'🛡️ '} Carft: {attacker.craft*'🔵'}\n')
                else:
                    print(f'{colored(attacker, 'cyan')} stats:\nStrength: {attacker.strength * '🔴'} Defence: {attacker.defend *'🛡️ '} Carft: {attacker.craft*'🔵'}\n')
                get_you_cant_do_it(defending, pleya1)
                return 'attacker', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
            elif full_attack <= full_defence:
                print('Exellent defense! 🧱🧱🧱🧱')
                return 'defending', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
        elif mana <= 0:
            print(f"{attacker} doesn't have a craft, try attack by a strength")
        if attack == 'rest':
            print(f'{attacker} resting')
            return None, 0, 0, 0, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
        if vim <= 0 and mana <= 0:
            vim = 0
            mana = 0
            critical = 0
            print(f"{attacker} doesn't have a stamina and mana!")
            return None, vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was


#thunder attack
        if attack == 't' and mana >= 4 and attacker.special == 'sorceress' or attack == 'thunder' and mana >= 4 and attacker.special == 'sorceress':
            vim = 0
            mana = 4
            ent = 0
            a = attacker.craft
            vampire_hunter = 0
            wizard = 0
            full_attack = random.randint(15,50)
            if defending.special == 'ent':
                ent = random.randint(9,10)
            full_attack += ent
            print(p.renderText(f'THUNDER!  {full_attack}'))
            d = defending.defend
            if defending.special.title() in freezer:
                d = 1
            if defending.special == 'dark elf':
                convert = random.choice([1,1,1,1.5,1.5,1.5,1.5,2,2,2,3,3,4,5,10])
                d = round(d * convert)
            if defending.special == 'fairy':
                if defending.freeze == 0:
                    add = random.randint(1,4)
                    convert = random.choice([1,1,2,2,4,4,5,5,15])
                    d = d * convert
                else:
                    d = 1
                    add = 0
            elif defending.special == 'ogre' or defending.special == 'rogue' or defending.special == 'dark elf' or defending.special == 'troll' or defending.special == 'vampire' or defending.special == 'ent':
                add = random.randint(1,8)
            elif defending.special == 'ghost knight':
                add = random.randint(1,12)
            else:
                add = random.randint(1,6)
            wizard2 = 0
            if defending.special == 'wizard':
                wizard = attacker.craft
                wizard2 = random.randint(1,2)
                if wizard2 == 2:
                    wizard2 = 50
            full_defence = d + add + mandolin_defense + wizard + wizard2
            if defending.special.title() in fear:
                full_defence -= random.randint(1,6)
            if defending.special == 'witch hunter':
                full_defence += round(attacker.craft * 1.4)
            if mandolin_defense > 0:
                print('🪕🪕🪕🪕🪕🪕🪕🪕🪕 MAAAAAAAAAAAAAGIC MAAAAAAAAAAAAAAANDOLLLIIIIIIIIIIIIIIIIIIIIIIIIIIIIIN! 🪕🪕🪕🪕🪕🪕🪕🪕🪕')
            if defending.special == 'fairy':
                print(p.renderText(f'Dodge  {round(full_defence)}'))
            elif defending.special == 'wizard' and wizard2 == 50:
                print(p.renderText(f'Thunder repulse  {round(full_defence)}'))
            else:
                print(p.renderText(f'Defend  {round(full_defence)}'))
            critical = 0
            if full_attack > full_defence:
                if defending.special.title() in freezer:
                    defending.freeze = 0
                    print(colored('⛓️‍💥 The Ice block is breaking ⛓️‍💥', 'blue'))
                    if defending.special.title() in temp_box or defending.special.title() in temp_box_2:
                        if defending.special.title() in temp_box_2:
                            temp_box_2.remove(defending.special.title())
                        he_returned.append(defending.special.title())
                while True:
                    if defending.special.title() in freezer:
                        freezer.remove(defending.special.title())
                    else:
                        break
                if full_attack >= 40:
                    critical += 3
                    print('Critical')
                elif full_attack >= 22:
                    print('Critical!')
                    critical += 2
                elif full_attack >= 17:
                    critical += 1
                    print('Critical!')
                print(f'Hit! 🩸{critical*'🩸'}\n')
                if 0 >= player2_life - critical - 1:
                    return 'attacker', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
                if attacker.special.title() in pleya1:
                    print(f'{colored(attacker, 'magenta')} stats:\nStrength: {attacker.strength * '🔴'} Defence: {attacker.defend *'🛡️ '} Carft: {attacker.craft*'🔵'}\n')
                else:
                    print(f'{colored(attacker, 'magenta')} stats:\nStrength: {attacker.strength * '🔴'} Defence: {attacker.defend *'🛡️ '} Carft: {attacker.craft*'🔵'}\n')
                get_you_cant_do_it(defending, pleya1)
                return 'attacker', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
            elif full_attack <= full_defence:
                print('Exellent defense! 🧱🧱🧱🧱')
                return 'defending', vim, mana, critical, paladin_life, vampire_life, magic_dust, freezer, fearing, he_returned, he_was
        elif attack == 't' or attack == 'thunder':
            print(f"{attacker} can't use a thunder attack")



# freeze attack!
        if attack == 'f' and attacker.freeze > 0 and attacker.special == 'sorceress' or attack == 'freeze' and attacker.freeze > 0 and attacker.special == 'sorceress':
            if defending.special == 'bard':
                freezer.append('Bard')
            if defending.special.title() in box:
                he_was = defending.special.title()
            else:
                he_was = 'no'
            return 'freeze', 0, 0, 0, 0, 0, 0, freezer, fearing, he_returned, he_was
        elif attack == 'f' or attack == 'freeze':
            print(f"{attacker} can't use a freeze attack")


        if attack != 's' and attack != 'strength' and attack != 'c' and attack != 'craft' and attack != 't' and attack != 'thunder':
            print(f"Input: 'Craft' or 'C' to use {attacker}'s craft or 'Strength' or 'S' to use {attacker}'s strength. Sorcerres can use thunder and freeze attack\n" )

def get_you_cant_do_it(warrior, pleya1):
    if warrior.strength == 1 and warrior.defend == 1 and warrior.craft == 0:
        discard == None
        return discard
    if warrior.special.title() in pleya1:
        print(f'{colored(warrior, 'magenta')}\nStrength: {warrior.strength*'🔴'}  Defence: {warrior.defend*'🛡️ '}  Craft: {warrior.craft*'🔵' if warrior.craft > 0 else None}  Stamina: {warrior.vim*'🟪'}  Mana: {warrior.mana*'🧊'}')
    else:
        print(f'{colored(warrior, 'cyan')}\nStrength: {warrior.strength*'🔴'}  Defence: {warrior.defend*'🛡️ '}  Craft: {warrior.craft*'🔵' if warrior.craft > 0 else None}  Stamina: {warrior.vim*'🟪'}  Mana: {warrior.mana*'🧊'}')
    while True:
        discard = input(f'You heve to discard 1 skill point form {warrior.strength*'🔴'} {warrior.defend*'🛡️ '} {warrior.craft*'🔵'} : ').lower().strip()
        if discard == 'strength' and warrior.strength <= 1 or discard == 's' and warrior.strength <= 1:
            print("You can't do it. You must have at least 1 skill strength's point")
        elif discard == 'craft' and warrior.craft <= 0 or discard == 'c' and warrior.craft <= 0:
            print("you can't do it. You don't have craft's points")
        elif discard == 'defence' and warrior.defend <= 1 or discard == 'd' and warrior.defend <= 1:
            print("You can't do it. You must have at least 1 skill defence's point")
        elif discard == 'strength' or discard == 's':
            warrior.strength -= 1
            break
        elif discard == 'craft' or discard == 'c':
            warrior.craft -= 1
            break
        elif discard == 'defence' or discard == 'd':
            warrior.defend -= 1
            break


def get_warrior_counter(defending, attacker, bow, freezer, pleya1):
    hit = 0
    if defending.special == 'warrior' and defending.vim > 0 and 'Warrior' not in freezer:
        if bow == 'no' or bow == 'n':
            defending.vim -= 1
            full_attack = round((defending.strength + random.randint(3,17)) * 0.7)
            de = attacker.defend
            if attacker.special == 'dark elf':
                convert = random.choice([1,1,1,1.5,1.5,1.5,1.5,2,2,2,3,3,4,5,10])
                de = round(de * convert)
            if attacker.special == 'fairy':
                convert = random.choice([1,1,2,2,4,4,5,5,15])
                de = de * convert
                add = random.randint(1,4)
            elif attacker.special == 'ogre' or attacker.special == 'ghost knight' or attacker.special == 'rogue' or attacker.special == 'dark elf' or attacker.special == 'troll' or attacker.special == 'vampire' or attacker.special == 'ent':
                add = random.randint(1,8)
            else:
                add = random.randint(1,6)
            full_defence = de + add
            print(p.renderText(f'Warrior Counter  {round(full_attack)}'))
            if attacker.special == 'fairy':
                print(p.renderText(f'Dodge  {round(full_defence)}'))
            else:
                print(p.renderText(f'Defend  {round(full_defence)}'))
            critical = 0
            hit = 0
            if full_attack > full_defence:
                hit = 1
                if full_attack >= 22:
                    critical += 2
                    print(f'Critical!')
                elif full_attack >= 17:
                    critical += 1
                    print('Critical!')
                hit + critical
                attacker.life -= hit
                print(f'Hit! 🩸{critical*'🩸'}\n')
                if attacker.life > 0:
                    if attacker.special.title() in pleya1:
                        print(f'{colored(attacker, 'magenta')} stats:\nStrength: {defending.strength * '🔴'} Defence: {defending.defend *'🛡️ '} Carft: {defending.craft*'🔵'}\n')
                    else:
                        print(f'{colored(attacker, 'cyan')} stats:\nStrength: {defending.strength * '🔴'} Defence: {defending.defend *'🛡️ '} Carft: {defending.craft*'🔵'}\n')
                    get_you_cant_do_it(attacker, pleya1)
            elif full_attack <= full_defence:
                print('Exellent defense! 🧱🧱🧱🧱')
    elif defending.vim <= 0:
        print(f"{defending} doesn't have a stamina")

if __name__=='__main__':
    main()
