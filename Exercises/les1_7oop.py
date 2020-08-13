from random import randint

class Fighter:
    # инициализация
    def __init__(self, name):
        self.name = name                # имя
        self.__lvl = 1                  # уровень
        self.__max_hp = 100             # максимальные НР
        self.__hp = self.__max_hp       # текущие НР
        self.__exp = 0                  # текущий опыт
        self.__next_lvl_exp = 1000      # опыт до следующего уровня
        self.__dmg = 20                 # наносимый урон

    # проверка на переполнение полоски опыта: происходит после каждого сеттера текущего опыта;
    # если опыта достаточно, то даем следующий уровень и повышаем характеристики героя
    def check_lvl_up(self):
        if self.__exp >= self.__next_lvl_exp:
            self.__exp = self.__exp - self.__next_lvl_exp
            self.__max_hp += 20
            self.__hp = self.__max_hp
            self.__next_lvl_exp += round(self.__next_lvl_exp * 1.1)
            self.__dmg += 5
            self.__lvl += 1
            print("%s получил уровень %d и восстановил HP!" % (self.name, self.__lvl))

    # НР getter/setter
    @property
    def hp(self): return self.__hp
    @hp.setter
    def hp(self, hp):
        self.__hp = hp
        if self.__hp <= 0:
            self.__hp = 0
            print("%s погиб, получив смертельный урон." % self.name)

    # damage getter
    @property
    def dmg(self): return self.__dmg

    # exp getter/setter
    @property
    def exp(self): return self.__exp
    @exp.setter
    def exp(self, exp):
        self.__exp = exp
        self.check_lvl_up()     # если опыта больше, чем нужно, то повышаем уровень

    # вывести информацию о бойце
    def __str__(self):
        string = "Имя: {} | HP: {} | Ур. {} | Урон: {} | Опыт: {}/{}".format(
            self.name, self.__hp, self.__lvl, self.__dmg, self.__exp, self.__next_lvl_exp)
        return string

    # удаление из памяти
    def __del__(self):
        print(self.name + " удален из памяти.")


class Battle:
    # инициализация (добавляем бойцов к битву)
    def __init__(self, unit1, unit2):
        self.__unit1 = unit1
        self.__unit2 = unit2

    # показать текущее состояние битвы
    def show_status(self):
        print("%s: %d HP | %s: %d HP" % 
        (self.__unit1.name, self.__unit1.hp, self.__unit2.name, self.__unit2.hp))

    def attack(self, attc, victim):
        """
        Наносит урон жертве и выводит информацию об ударе на экран.
        Увеличивает опыт атакующего в зависимости от нанесенного урона.
        Входные параметры:
            - атакующий;
            - жертва;
        """
        exp_gained = attc.dmg * 20          # опыт за удар
        hp_left = victim.hp - attc.dmg      # кол-во хп жертвы после удара
        print("%s(%d HP) нанес %d урона по %sу(%d HP) и получил %d опыта" % 
        (attc.name, attc.hp, attc.dmg, victim.name, 0 if hp_left < 0 else hp_left, exp_gained))
        victim.hp -= attc.dmg
        attc.exp += exp_gained

    # объявить победителя и вывести о нем информацию
    def declare_victory(self, winner, loser):
        print("%s победил %sа!" % (winner.name, loser.name))
        print(str(winner))

    # начать битву
    # битва будет продолжаться, пока НР одного их бойцов не кончится
    def start(self):
        print("Боец №1:", str(self.__unit1))
        print("Боец №2:", str(self.__unit2))
        # в зависимости от рандома (1 или 2) атакует 1 или 2 боец соответственно
        while self.__unit1.hp > 0 and self.__unit2.hp > 0:
            if randint(1, 2) == 1:
                self.attack(self.__unit1, self.__unit2)
            else:
                self.attack(self.__unit2, self.__unit1)
        # объявляем победителем того, у кого остались НР
        if self.__unit1.hp > 0:
            self.declare_victory(self.__unit1, self.__unit2)
        else:
            self.declare_victory(self.__unit2, self.__unit1)

    # удаление из памяти
    def __del__(self):
        print("Битва стерта из истории.")

# создаем бойцов           
figher_1 = Fighter("Лестер")
figher_2 = Fighter("Карутус")

# создаем битву
battle = Battle(figher_1, figher_2)
# начинаем битву
battle.start()