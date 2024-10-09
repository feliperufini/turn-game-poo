import random

class Character:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def getName(self):
    return self.__name

  def getLife(self):
    return self.__life

  def getLevel(self):
    return self.__level

  def showDetails(self):
    return f"Nome: {self.getName()}\nVida: {self.getLife()}\nNível: {self.getLevel()}"

  def defend(self, damage):
    self.__life -= damage
    if self.__life <= 0:
      self.__life = 0

  def attack(self, enemy):
    damage = random.randint(self.getLevel() * 2, self.getLevel() * 4)
    enemy.defend(damage)
    print(f"{self.getName()} atacou {enemy.getName()} causando {damage} de dano!")

class Hero(Character):
  def __init__(self, name, life, level, skill):
    super().__init__(name, life, level)
    self.__skill = skill

  def getSkill(self):
    return self.__skill

  def showDetails(self):
    return f"{super().showDetails()}\nHabilidade: {self.getSkill()}\n"

  def specialAttack(self, enemy):
    damage = random.randint(self.getLevel() * 4, self.getLevel() * 6)
    enemy.defend(damage)
    print(f"{self.getName()} usou a habilidade especial {self.getSkill()} em {enemy.getName()} e causou {damage} de dano!")

class Enemy(Character):
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level)
    self.__type = type

  def getType(self):
    return self.__type

  def showDetails(self):
    return f"{super().showDetails()}\nTipo: {self.getType()}\n"

class Game:
  def __init__(self) -> None:
    self.myHero = Hero(name="Felsky", life=100, level=5, skill="Super Força")
    self.theEnemy = Enemy(name="Ykslef", life=50, level=4, type="Fogo")

  def startGame(self):
    print("Iniciando o combate!")
    while self.myHero.getLife() > 0 and self.theEnemy.getLife() > 0:
      print("\nDetalhes dos pensonagens:")
      print(self.myHero.showDetails())
      print(self.theEnemy.showDetails())

      input("Pressione Enter para atacar...")
      print("Ataques diponíveis:\n1. Ataque Normal\n2. Ataque Especial\n")

      while True:
        chosenAttack = input("Ataque escolhido: ")
        if chosenAttack == "1":
          self.myHero.attack(self.theEnemy)
          break
        elif chosenAttack == "2":
          self.myHero.specialAttack(self.theEnemy)
          break
        else:
          print("Informe um valor válido...")

      if self.theEnemy.getLife() > 0:
        self.theEnemy.attack(self.myHero)

    if self.myHero.getLife() > 0:
      print("\nParabéns, você derrotou o inimigo!")
    else:
      print("\nVocê foi derrotado pelo inimigo!")

game = Game()
game.startGame()