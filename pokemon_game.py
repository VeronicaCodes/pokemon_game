class Pokemon:
  def __init__(self, name, type, level):
    self.name = name
    self.level = level
    self.type = type
    self.hp = level * 10
    self.max_hp = level * 10
    self.is_knocked_out = False

  def repr(self):
    return "This Pokeball coinatins {name} Pokemon, {type} type, level {level}.".format(name = self.name, type = self.type, level = self.level)

  def attack(self, opponent):
    if (self.type == "Electric" and opponent.type == "Water", self.type == "Water" and opponent.type == "Fire"):
      print('{name} attacked {opponent} and dealt {damage} points of damage!'.format(name = self.name, opponent = opponent.name, damage = self.level * 2))
      opponent.lose_health(self.level * 2)
      print('Wow! What a hit!')
    if (self.type == "Fire" and opponent.type == "Electric"):
      print('{name} attacked {opponent} and dealt {damage} points of damage!'.format(name = self.name, opponent = opponent.name, damage = self.level * 1.5))
      print('Nice one, {name}!'.format(name = self.name))
      opponent.lose_health(self.level * 1.5)
    if (self.type != "Fire" or self.type != "Water" or self.type != "Electric"):
      print ("Unknown type of Pokemon! Research it later!")
    if self.is_knocked_out == True:
      print("{name} cannot attack, it was knocked out!".format(name = self.name))
    else:
      print("Oops, that wasn't very effective... Choose another Pokemon!")
  
  def lose_health(self, points):
    self.hp -= points
    if self.hp <= 0 or self.hp == 0:
      self.hp = 0
      self.is_knocked_out = True
      print("Oh, no! {name} was knocked out!".format(name = self.name))
    else:
      print("Ouch! {name} now has {hp} health points left.".format(name = self.name, hp = self.hp))
    
  def gain_health(self, points):
    self.hp += points
    if self.hp >= self.max_hp:
      self.hp = self.max_hp
      print("Feeling good! {name}'s health is maxed!". format(name = self.name))

  def revive(self):
    if self.is_knocked_out == True:
      self.is_knocked_out = False
      self.hp = 1
      print("What was that? {name} was revived.")

class Pikachu(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Pikachu", "Electric", level)

class Charmander(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Squirtle", "Water", level)

class Trainer:
  def __init__(self, pokeballs, hp_potions, name):
    self.name = name
    self.pokeballs = pokeballs
    self.hp_potions = hp_potions
    self.active_pokemon = 0

  def __repr__(self):
    print("The trainer {name} uses the pokeball!".format(name = self.name))
    for pokemon in self.pokeballs:
      print(pokemon)
    return "The active pokemon is {name}".format(name = self.pokeballs[self.active_pokemon].name)

  def num_pokemons(self):
    pokemons = 0
    for pokemon in self.pokeballs:
      pokemons += 1
      if pokemons >= 6:
        print("Can't carry any more Pokeballs.")
    print('{name} has {number} number of pokeballs in his pocket!'.format(name = self.name, number = pokemons))

  def choose_pokemon(self, active_pokeball):
    if active_pokeball < self.num_pokemons() and active_pokeball >= 0:
      if self.pokeballs[active_pokeball].is_knocked_out == True:
        print("{name} is knocked out. Cannot activate this Pokeball!".format(name = self.pokeballs[active_pokeball].name))
      if active_pokeball == self.active_pokemon:
        print("{name} pokeball is already activated!".format(name = self.pokeballs[active_pokeball].name))
      else:
        self.active_pokemon = active_pokeball
        print("{name}, I choose you!".format(name = self.pokeballs[self.active_pokemon].name))
    
  def attack_enemy(self, enemy):
    my_pokemon = self.pokeballs[self.active_pokemon]
    enemy_pokemon = enemy.pokeballs[enemy.active_pokemon]
    my_pokemon.attack(enemy_pokemon)

  def use_potion(self):
    if self.hp_potions > 0:
      self.pokeballs[self.active_pokemon].gain_health(10)
      print("Used a health potion on {name}.".format(name = self.pokeballs[self.active_pokemon].name))
      self.hp_potions -= 1
    else:
      print("Oh no, you're out of potions! Cheese it!")
       
#Pokemons!

a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Pikachu(10)
e = Charmander()
f = Squirtle(2)

#Trainers!

Ash = Trainer([d,e,f], 3, "Ash")
Paul = Trainer([a,b,c], 5, "Paul")

print(Ash)
print(Paul)

# Testing attacking, giving potions, and switching pokemon.
Ash.attack_enemy(Paul)
Paul.attack_enemy(Ash)
Paul.use_potion()
Ash.attack_enemy(Paul)
Ash.choose_pokemon(0)
Paul.choose_pokemon(1)


    
    
