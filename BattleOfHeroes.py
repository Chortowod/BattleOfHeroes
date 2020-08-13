# необходимо установить модуль: pip install pyinputplus
from random import randint, choice
import csv
from datetime import datetime as dt
import os.path
import pyinputplus as pyip
import names

# для быстрого вывода текста другого цвета
def print_y(string): print(bcolors.YELLOW + string + bcolors.ENDC)
def print_r(string): print(bcolors.RED + string + bcolors.ENDC)
def print_g(string): print(bcolors.GREEN + string + bcolors.ENDC)
def print_gr(string): print(bcolors.GRAY + string + bcolors.ENDC)
def print_lb(string): print(bcolors.LBLUE + string + bcolors.ENDC)
def print_yn(string): return pyip.inputYesNo(bcolors.YELLOW + string + bcolors.ENDC)

# для изменения цвета в консоли
class bcolors:
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    LGRAY = '\033[90m'
    GRAY = '\033[2m'
    LBLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BORDER = '\033[7m'
    LBORDER = '\033[100m'
    RED_BORDER = '\033[101m'
    GREEN_BORDER = '\033[102m'
    BLUE_BORDER = '\033[104m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

# по идее это абстрактный класс, хотя он может работать в игре, но я его использую для создания подклассов
class Fighter:
    # инициализация
    def __init__(self, name, lvl = 1, max_hp = 80, hp = 80, exp = 0, next_lvl_exp = 1000, dmg = 20, defc = 0, defc_mag = 0, style = ""):
        self.name = name                    # имя
        self.lvl = lvl                      # уровень
        self.max_hp = max_hp                # максимальные НР
        self.__hp = hp                      # текущие НР
        self.__exp = exp                    # текущий опыт
        self.next_lvl_exp = next_lvl_exp    # опыт до следующего уровня
        self.dmg = dmg                      # наносимый урон
        self.defc = defc                    # защита от физического урона
        self.defc_mag = defc_mag            # защита от магии
        self.style = style

    # проверка на переполнение полоски опыта: происходит после каждого сеттера текущего опыта;
    # если опыта достаточно, то даем следующий уровень и повышаем характеристики героя
    def check_lvl_up(self):
        if self.__exp >= self.next_lvl_exp:
            self.__exp = self.__exp - self.next_lvl_exp
            self.next_lvl_exp = round(self.next_lvl_exp * 1.5)
            self.lvl += 1
            self.lvl_up()
            print_g("%s получил уровень %d и восстановил HP!" % (self.name, self.lvl))
            
    
    def lvl_up(self):
        raise NotImplementedError("Subclass must implement this method")
        
    # hp getter/setter
    @property
    def hp(self): return self.__hp
    @hp.setter
    def hp(self, hp):
        self.__hp = hp
        if self.__hp <= 0:
            self.__hp = 0
            # print_r("%s погиб, получив смертельный урон." % self.name)

    # exp getter/setter
    @property
    def exp(self): return self.__exp
    @exp.setter
    def exp(self, exp):
        self.__exp = exp
        self.check_lvl_up()     # если опыта больше, чем нужно, то повышаем уровень

    # вывести информацию о бойце
    def __str__(self):
        string = "{} {} | HP: {} | Ур. {} | Урон: {} | Защита: {} | Маг. защита: {} | Опыт: {}/{}".format(
            self.style, self.name, self.__hp, self.lvl, self.dmg, self.defc, self.defc_mag, self.__exp, self.next_lvl_exp)
        return string

    # сохранить бойца в файл
    def save(self):
        if self.__hp == 0:
            print_y("Боец мертв, невозможно сохранить.")
            return
        filename = "heroes.csv"
        filepath = './heroes.csv'

        hero = [self.name, self.lvl, self.max_hp, self.__hp, self.__exp, 
                self.next_lvl_exp, self.dmg, self.defc, self.defc_mag, self.style]

        # если файл сохранения уже существует...
        if os.path.isfile(filepath):
            rows = []
            # ...то сначала считываем все строки...
            with open(filename, "r", encoding="utf-8", newline="") as fh:
                reader = csv.reader(fh)
                rows = list(reader)   
            # ...затем заново их записываем в файл...
            with open(filename, "w", encoding="utf-8", newline="") as fh:
                writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
                check = False
                for row in rows:
                    # ...и если встречаем бойца с данным именем...
                    if self.name in row[0]:
                        # ... то записываем вместо имеющейся строчки о нем новую...
                        writer.writerow(hero)
                        check = True
                    else:
                        writer.writerow(row)
                # а если не встречаем, то записываем его в конце
                if not check: writer.writerow(hero)
        # если файла сохранения нет, то создаем его и записываем туда бойца
        else:
            with open(filename, "w", encoding="utf-8", newline="") as fh:
                writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
                writer.writerow(hero)
        print_g("Персонаж сохранен.")

    # удаление бойца из сохранения
    def delete(self):
        # на всякий случай спрашиваем подтверждение
        ans_new = print_yn("Вы действительно хотите удалить бойца из сохранения? y/n\n")
        if ans_new == "no": return
        filename = "heroes.csv"
        filepath = './heroes.csv'

        # проверяем, есть ли файл сохранений
        if os.path.isfile(filepath):
            rows = []
            check = False
            # считываем все строки...
            with open(filename, "r", encoding="utf-8", newline="") as fh:
                reader = csv.reader(fh)
                rows = list(reader)   
            # ...затем заново их записываем в файл...
            with open(filename, "w", encoding="utf-8", newline="") as fh:
                writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
                for row in rows:
                    # ...и если встречаем бойца с данным именем...
                    if self.name in row[0]:
                        # ...то просто пропускаем запись о нем, не записывая ее в файл
                        print_y("Персонаж удален.")
                        check = True
                        continue
                    else:
                        writer.writerow(row)
            if not check: print_y("Персонаж не найден.")
        else:
            print_y("Сохранение отсутствует.")

    # удаление из памяти
    def __del__(self):
        print(self.name + " удален из памяти.")

# подкласс основного класса - Маг
class Mage(Fighter):
    def __init__(self, name, lvl = 1, max_hp = 80, hp = 80, exp = 0, next_lvl_exp = 1000, dmg = 25, defc = 0, defc_mag = 5, style = "Маг"):
        super().__init__(name, lvl, max_hp, hp, exp, next_lvl_exp, dmg, defc, defc_mag, style)
    def lvl_up(self):
        if self.lvl % 2 == 0: self.defc_mag += 5     # каждый второй уровень увеличивает маг. защиту на 5
        if self.lvl % 3 == 0: self.defc += 5         # каждый третий уровень увеличивает защиту на 5
        self.max_hp += 15
        self.hp = self.max_hp
        self.dmg += 7

# подкласс основного класса - Воин
class Warrior(Fighter):
    def __init__(self, name, lvl = 1, max_hp = 100, hp = 100, exp = 0, next_lvl_exp = 1000, dmg = 20, defc = 5, defc_mag = 0, style = "Воин"):
        super().__init__(name, lvl, max_hp, hp, exp, next_lvl_exp, dmg, defc, defc_mag, style)

    def lvl_up(self):
        if self.lvl % 2 == 0: self.defc += 5             # каждый второй уровень увеличивает защиту на 5
        if self.lvl % 3 == 0: self.defc_mag += 5         # каждый третий уровень увеличивает маг. защиту на 5
        self.max_hp += 20
        self.hp = self.max_hp
        self.dmg += 5


class Battle:
    # инициализация (добавляем бойцов к битву)
    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy
        self.is_over = False        # переменная для отслеживания состояния битвы
        self.battles = []           # для записи лога о битве

    # показать текущее состояние битвы
    def show_status(self):
        print("%s: %d HP | %s: %d HP" % 
        (self.__player.name, self.__player.hp, self.__enemy.name, self.__enemy.hp))

    def attack(self, attc, victim):
        """
        Наносит урон жертве и выводит информацию об ударе на экран.
        Увеличивает опыт атакующего в зависимости от нанесенного урона.
        Входные параметры:
            - атакующий;
            - жертва;
        """
        if attc.style == "Воин": damage = round(attc.dmg * (1 - victim.defc / 100))
        elif attc.style == "Маг": damage = round(attc.dmg * (1 - victim.defc_mag / 100))
        else: raise Exception('Неопознанный класс игрока')
        exp_gained = damage * 20          # опыт за удар
        hp_left = victim.hp - damage      # кол-во хп жертвы после удара
        print_gr("%s(%d HP) нанес %d урона по %s(%d HP) и получил %d опыта" % 
            (attc.name, attc.hp, damage, victim.name, 0 if hp_left < 0 else hp_left, exp_gained))
        victim.hp -= damage
        attc.exp += exp_gained

    # объявить победу
    def declare_victory(self, winner, loser):
        print_g("Ваш боец [%s] одержал победу! %s повержен." % (winner.name, loser.name))
        self.is_over = True
        self.battles.append([winner.name, loser.name, dt.now().strftime("%d.%m.%Y %H.%M.%S")])
    
    # объявить поражение
    def declare_loss(self, winner, loser):
        print_r("%s победил вашего бойца. %s мертв." % (winner.name, loser.name))
        print("--------------------------------------")
        print("-----------БИТВА ОКОНЧИЛАСЬ-----------")
        print("--------------------------------------")
        self.is_over = True
        self.battles.append([winner.name, loser.name, dt.now().strftime("%d.%m.%Y %H.%M.%S")])


    # начать битву
    # битва будет продолжаться, пока НР одного их бойцов не кончится
    def start(self):
        print("Боец №1:", str(self.__player))
        print("Боец №2:", str(self.__enemy))
        print("--------------------------------------")
        print("------------БИТВА НАЧАЛАСЬ------------")
        print("--------------------------------------")
        # в зависимости от рандома (1 или 2) атакует 1 или 2 боец соответственно
        while self.__player.hp > 0 and self.__enemy.hp > 0:
            if randint(1, 2) == 1:
                self.attack(self.__player, self.__enemy)
            else:
                self.attack(self.__enemy, self.__player)
        # объявляем победу или поражение в зависимости от исхода
        if self.__player.hp > 0:
            self.declare_victory(self.__player, self.__enemy)
            return True
        else:
            self.declare_loss(self.__enemy, self.__player)
            return False

    # сохранить итог битвы в файл
    def save(self):
        # проверка статуса битвы (битву в процессе нельзя сохранить)
        if self.is_over:
            filename = "battles.csv"
            filepath = './battles.csv'
            # список покупок

            # проверяем, есть ли файл сохранений
            if os.path.isfile(filepath):
                with open(filename, "a", encoding="utf-8", newline="") as fh:
                    writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
                    for row in self.battles:
                        writer.writerow(row)
            else:
                with open(filename, "w", encoding="utf-8", newline="") as fh:
                    writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
                    writer.writerow(["Победитель", "Проигравший", "Время"])  # Заголовки столбца
                    for row in self.battles:
                        writer.writerow(row)
            print_g("Битва сохранена в истории.")
        else:
            print_y("Битва еще не окончена!")

    # удаление из памяти
    def __del__(self):
        self.save()

# загрузить бойца из файла сорхранения
def load(name):
    filename = "heroes.csv"
    filepath = './heroes.csv'

    # если файл сохранений существует
    if os.path.isfile(filepath):
        rows = []
        with open(filename, "r", encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh)
            rows = list(reader)
        for row in rows:
            # если находит бойца с данным именем, то вызываем конструктор
            if name in row[0]:
                # запускаем конструктор в зависимости от класса
                if row[9] == "Воин":
                    hero = Warrior(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), 
                                int(row[5]), int(row[6]), int(row[7]), int(row[8]), row[9])
                elif row[9] == "Маг":
                    hero = Mage(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), 
                                int(row[5]), int(row[6]), int(row[7]), int(row[8]), row[9])
                else:
                    print_r("Файл сохранения слишком старый или поврежден. Обратитесь к разработчику для помощи.")
                    return None
                print_g("Боец загружен!")
                return hero
        # если указанного персонажа нет, то предложить создать
        response = print_yn("Персонаж не найден! Хотите создать? y/n\n")
        if (response == "yes"):
            return create_fighter(name)
        else:
            return None
    else:
        print_y("Файла сохранения не обнаружено!")
        return None

def isExist(name):
    filename = "heroes.csv"
    filepath = './heroes.csv'

    # если файл сохранений существует
    if os.path.isfile(filepath):
        rows = []
        with open(filename, "r", encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh)
            rows = list(reader)
        for row in rows:
            # если находит бойца с данным именем, то возвращаем False
            if name in row[0]:
                return True
            else:
                return False
    return False

# создать бойца
def create_fighter(name = None):
    while True:
        # если параметров не было, то попросить ввести имя
        if name == None:
            name = pyip.inputStr("Введите имя: ", blockRegexes=[r'[@#$%^&*()_+!"№;:?*-=.,><"]$'])
        # если такое имя есть...
        if isExist(name):
            # то предложить создать бойца с другим именем
            response = print_yn("Боец с таким именем уже существует! Хотите ввести другое? y/n\n")
            if (response == "yes"):
                name = None
                continue
            else:
                return
        # если нет такого имени, то продолжаем
        else:
            break

    
    # выбрать класс
    ans_class = pyip.inputInt("Выберите класс: 1 - Воин, 2 - Маг\n", min=1, max=2)
    new_fighter = None
    if (ans_class == 1): new_fighter = Warrior(name)
    else: new_fighter = Mage(name)
    print_g("Боец создан!")
    return new_fighter

# справка по игре
def help():
    print("--------------------------------------")
    print("В этой игре вы можете создать персонажа (мага или воина) и сразиться на арене с противником. " + 
    "Если вы погибнете, то можете создать нового персонажа или загрузить старого. " + 
    "Для сохранения персонажа между дуэлями используйте соответствующую команду, однако помните: " + 
    "если вы сохранитесь при низком уровне ХП, то шансы на победу будут минимальными.")
    print("--------------------------------------")
    print(bcolors.GREEN + "create"  + bcolors.ENDC + " - создать бойца.")
    print(bcolors.LBLUE + "load"  + bcolors.ENDC + " - загрузить бойца из сохранения.")
    print(bcolors.RED + "delete"  + bcolors.ENDC + " - удалить бойца из сохранения и памяти. " + 
            bcolors.RED + "Неотвратимое действие!" + bcolors.ENDC)
    print(bcolors.YELLOW + "info"  + bcolors.ENDC + " - посмотреть информацию о текущем бойце.")
    print(bcolors.GREEN + bcolors.BOLD + "save"  + bcolors.ENDC + " - сохранить бойца.")
    print(bcolors.LGRAY + "exit"  + bcolors.ENDC + " - выйти из игры.")
    print(bcolors.VIOLET + bcolors.BOLD + "battle"  + bcolors.ENDC + " - начать дуэль.")
    print("--------------------------------------")

# начало игры
def start():
    # создаем массив с именами для врагов
    enemy_names = []
    choose_f = "Сначала выберите бойца!"
    for __ in range(50):
        enemy_names.append(names.get_first_name())
    # приветствие
    print("Добро пожаловать в Битву Героев. Введите " + bcolors.YELLOW + 
    "help" + bcolors.ENDC + " для ознакомления с базовыми командами.")
    print("Если вы уже знакомы с командами, то введите их ниже.")
    # создаем противника и болванку для героя
    fighter = None
    enemy = Warrior(choice(enemy_names))
    # пока пользователь не введет exit, игра будет работать
    while True:
        answer = pyip.inputStr()
        
        if answer == "help":
            help()

        elif answer == "create":
            if fighter is not None:
                ans_new = print_yn("Вы уже выбрали бойца. Уверены, что хотите создать нового? y/n\n")
                if ans_new == "yes": fighter = create_fighter()
            else:
                fighter = create_fighter()

        elif answer == "delete":
            if fighter is not None:
                fighter.delete()
                fighter = None
            else: print_y(choose_f)

        elif answer == "load":
            if fighter is not None:
                ans_new = print_yn("Вы уже выбрали бойца. Уверены, что хотите загрузить другого? y/n\n")
                if ans_new == "no":
                    continue
            ans_load = pyip.inputStr("Введите имя сохраненного бойца: ")
            fighter = load(ans_load)
        
        elif answer == "battle":
            if fighter is not None:
                battle = Battle(fighter, enemy)
                print("--------------------------------------")
                if battle.start():
                    enemy = Warrior(choice(enemy_names))
                    fighter.hp = fighter.max_hp
                else:
                    fighter = None
            else: print_y(choose_f)
        
        elif answer == "info":
            if fighter is not None:
                print(fighter)
            else: print_y(choose_f)
        
        elif answer == "save":
            if fighter is not None:
                fighter.save()
            else: print_y(choose_f)
        
        elif answer == "exit":
            if fighter is not None:
                fighter.save()
            return
        else:
            print_y("Неизвестная команда. Введите help для ознакомления с базовыми командами.")

# точка входа
start()
print_lb("Спасибо за игру!")