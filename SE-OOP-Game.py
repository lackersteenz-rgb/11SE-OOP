import random 
import time 

#haven't refactored
# STORYLINE  (Add your story here)


def story_intro():
    # purpose: opening intro to the game.
    # Example: print("Leaving your home planet behind, you venture into the unknown...")
    pass

def story_turn_player():
    #Purpose: The enemys statement before attack to the enemy
    # (continue storyline)
    pass

def story_turn_enemy():
    # Purpose: The enemys statement before attack to the player
    # (storyline continues)
    pass

def story_victory_round1():
    pass
# Purpose What is said after round 1 win - storyline


def story_victory_round2():
    pass
# Purpose: What is said after round 2 win - storyline


class Fighter:
    # Purpose: This is the overall class stats for the fighter each round. - name, health, speed, agility.
    def __init__(self, name, starting_health, speed, agility):
        self.name = name
        self._health = starting_health  
        self.speed = speed
        self.agility = agility
  
    def report(self):
        # Purpose: This function reports the health of the fighter.
        print(self.name + ': Health: ' + str(self._health))

    def get_health(self):
        # Purpose: This function returns the health of the fighter to the user.
        return self._health

    def set_health(self, new_health):
        # Purpose: This function sets the new value of the fighters health after recieving damage from the enemy.
        self._health = new_health

    def is_dead(self):
        # Purpose: This function checks if the fighter has died from the health returning as '0' or below.
        if self._health <= 0:
            return True
        else:
            return False

    def defend(self, attack_power):
        # Purpose: This function is the main defense sequence for the fighter. Asking the user when to hit 'Enter" to dodge or attack the enemy.
        target = random.randint(2, 5)
        print('An attack is incoming! Try to move out of the way!')
        print('') 
        print('Hit enter in exactly ' + str(target) + ' seconds.')
        
        # Purpose: This is the timing mechanism for the attack. The user will have to hit 'Enter' as close to the target time as possible to successfully dodge the attack. If they are successful, they will avoid taking damage. If they are unsuccessful, they will take damage and their health will be reduced.
        tic = time.time()
        input()
        toc = time.time()
        
        # Purpose: This is the simple calculations for the timing mechanism. Calculating the difference between the target time and time taken for the user to hit 'Enter'. The user will have to dodge within a certain gap of time to successfully dodge the attack. The gap is inlarged with their agility stat. 
        time.sleep(2) 
        time_taken = toc - tic
        
        # Purpose: 
        difference = target - time_taken
        if difference < 0:
            difference = difference * -1 
            
        dodge_window = 0.5 + (self.agility / 200)
        
        if difference <= dodge_window:
            print('Successful maneuver fighter! You moved out of the way in-time!')
            return True 
        else:
            damage = attack_power
            self._health = self._health - damage
            print(' You got hit! You could not move out of the way! You took ' + str(damage) + ' damage.')
            return False 

# purpose: player Subclass
class CombatJetFighter(Fighter):
    def __init__(self, name, starting_health, speed, agility, combat_bonus):
        Fighter.__init__(self, name, starting_health, speed, agility)
        self.combat_bonus = combat_bonus

    def defend(self, attack_power):
        target = random.randint(2, 5)
        print('An attack is incoming! Try to move out of the way!')
        print('')
        print('Hit enter in exactly ' + str(target) + ' seconds.')
        
        tic = time.time()
        input()
        toc = time.time()
        
        time.sleep(2) 
        time_taken = toc - tic
        difference = target - time_taken
        if difference < 0:
            difference = difference * -1
            
        dodge_window = 0.5 + (self.agility / 200)
        if difference <= dodge_window:
            print('Successful maneuver fighter! You moved out of the way in-time!')
            return True
        else:
            damage = attack_power
            self._health = self._health - damage
            print(' You got hit! You could not move out of the way! You took ' + str(damage) + ' damage.')
            return False

    def precision_strike(self):
        target = random.randint(4, 6)
        print(' + [LOCKING TARGET] Steady your crosshairs...')
        print('')
        print('Hit enter in exactly ' + str(target) + ' seconds to fire a shot.')
        
        tic = time.time()
        input()
        toc = time.time()
        
        time.sleep(2) 
        time_taken = toc - tic
        difference = target - time_taken
        if difference < 0:
            difference = difference * -1
            
        low_bound = self.speed // 3
        high_bound = self.speed // 2
        base_attack = random.randint(low_bound, high_bound)
        
        if difference <= 0.4:
            total_damage = base_attack + self.combat_bonus
            print(' CRITICAL HIT! Perfect aim figther! Damage: ' + str(total_damage))
            return total_damage
        else:
            print(' Standard hit. Damage: ' + str(base_attack))
            return base_attack


# Enemy Subclass 1
class SpaceSeahorse(Fighter):
    def __init__(self, name, starting_health, speed, agility, closer_attack_point):
        Fighter.__init__(self, name, starting_health, speed, agility)
        self.closer_attack_point = closer_attack_point

    def defend(self, attack_power):
        target = random.randint(2, 5)
        print('An attack is incoming! Try to move out of the way!')
        print('')
        print('Hit enter in exactly ' + str(target) + ' seconds.')
        
        tic = time.time()
        input()
        toc = time.time()
        
        time.sleep(2) 
        time_taken = toc - tic
        difference = target - time_taken
        if difference < 0:
            difference = difference * -1
            
        dodge_window = 0.5 + (self.agility / 200)
        if difference <= dodge_window:
            print('Successful maneuver fighter! You moved out of the way in-time!')
            return True
        else:
            damage = attack_power
            self._health = self._health - damage
            print(' BAM! The Space Seahorse caught your shot! Space Seahorse took ' + str(damage) + ' damage.')
            return False

    def close_range_attack(self):
        # Purpose:
        # Print statement (): Storyline of the enemy leaving its Jet to attack with closer range.
        print(' () ' + self.name + ' (more about what the space seahorse is doing now that it is out of the space craft) gets into closer range!')
        low_bound = self.speed // 4
        high_bound = self.speed // 2
        base_attack = random.randint(low_bound, high_bound)
        
        chance = random.randint(1, 2)
        if chance == 1:
            total_damage = base_attack + self.closer_attack_point
            print('Spacecraft vehicle bypassed! Closer attack points applied!')
            return total_damage
        else:
            print('Normal thruster swipe deployed.')
            return base_attack

# purpose: enemy subclass 2 ready for round 2.
# Enemy Subclass 2
class RockMonster(Fighter):
    def __init__(self, name, starting_health, speed, agility, rock_damage):
        Fighter.__init__(self, name, starting_health, speed, agility)
        self.rock_damage = rock_damage

    def defend(self, attack_power):
        target = random.randint(2, 5)
        print('(storyline about next enemy)An attack is incoming! Try to move out of the way!')
        print('')
        print('Hit enter in exactly ' + str(target) + ' seconds.')
        
        tic = time.time()
        input()
        toc = time.time()
        
        time.sleep(2) 
        time_taken = toc - tic
        difference = target - time_taken
        if difference < 0:
            difference = difference * -1
            
        dodge_window = 0.5 + (self.agility / 200)
        if difference <= dodge_window:
            print(' Successful maneuver! The Rock Monster deflected the blast!')
            return True
        else:
            damage = attack_power
            self._health = self._health - damage
            print(' Hit! The Rock Monster cracked! The rock monster took ' + str(damage) + ' damage.')
            return False

    def heavy_rock_smash(self):
        print('BAM! ' + self.name + ' hurls a massive asteroid chunk at your jet!')
        low_bound = self.speed // 4
        high_bound = self.speed // 2
        base_attack = random.randint(low_bound, high_bound)
        
        chance = random.randint(1, 2)
        if chance == 1:
            total_damage = base_attack + self.rock_damage
            print('CRUSHING BLOW! Extreme rock damage applied!')
            return total_damage
        else:
            print('The asteroid scraped your jets wings. Normal damage applied.')
            return base_attack


#Game setup and loops
# Purpose: The start of functioanl gameplay code that the user will recieve.
story_intro()

# Initialize the Player
you = CombatJetFighter('You (Combat Jet Fighter)', 100, 100, 60, 50)

# ------------------------------------------
# ROUND 1: THE SPACE SEAHORSE
# ------------------------------------------
seahorse = SpaceSeahorse('The Space Seahorse', 80, 60, 20, 50)

print('--- INITIAL ENEMY DETECTED ---')
you.report()
seahorse.report()

game_over = False

while True:
    print('')
    print('')
    print('         ROUND 1: ENGAGING SEAHORSE      ')
    print('')
    print('')
    
    # Story lines will print out right here
    story_turn_player()
    
    print('You attack ' + seahorse.name)
    attack = you.precision_strike()
    
    seahorse_dodged = seahorse.defend(attack)
    
    print('')
    print('>>> TURN RESULT <<<')
    if seahorse_dodged == True:
        print('X ATTACK MISSED: The Space Seahorse escaped taking 0 damage!')
    else:
        print('+ ATTACK LANDED: The Space Seahorse took a direct hit!')
        
    print('')
    print('FIELD REPORT')
    you.report()
    seahorse.report()
    print('')
    
    # Increased to 6 seconds for comfortable reading
    time.sleep(6) 
    if seahorse.is_dead():
        story_victory_round1()
        print('')
        print(' You defeated the Space Seahorse!')
        break
        
    print('')
    # Story lines will print out right here
    story_turn_enemy()
    
    print(seahorse.name + ' attacks you . . .')
    enemy_attack = seahorse.close_range_attack()
    
    you_dodged = you.defend(enemy_attack)
    
    print('')
    print('>>> This Rounds Results <<<')
    if you_dodged == True:
        print(' SAFE: You cleanly moved out of the way of the attack!')
    else:
        print('!! ALERT: Your jet was struck by the incoming enemy fire!')
        
    print('')
    print('Final Health Status')
    you.report()
    seahorse.report()
    print('')
    
    time.sleep(6)
    if you.is_dead():
        print('')
        print('>> ' + seahorse.name + ' wins!')
        game_over = True
        break

