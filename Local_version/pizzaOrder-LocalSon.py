# Import Neccessary libraries
from datetime import datetime
import csv
from typing import List
import os


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def showMenu():
  with open("G:\Drive'ım\GlobalAI-PizzaOrder\Menu.txt", 'r') as f:
    print(f.read())

def ordersList():
  with open("G:\Drive'ım\GlobalAI-PizzaOrder\Orders_Database.csv", mode="r+") as db:
    print(db.read())
    
    
# Define Pizza Classes
class Pizza:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        
    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name

class ClassicPizza(Pizza):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class MargheritaPizza(Pizza):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class TurkPizza(Pizza):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class DominosPizza(Pizza):
    def __init__(self, name, cost):
        super().__init__(name, cost)
        
        
# Define Pizza Size Classes
class PizzaSize:
    def __init__(self, name, multiplyCost):
        self.name = name
        self.multiplyCost = multiplyCost
        
    def get_multiplyCost(self):
        return self.multiplyCost
    
    def get_name(self):
        return self.name

class BigSize(PizzaSize):
    def __init__(self, name, multiplyCost):
        super().__init__(name, multiplyCost)

class NormalSize(PizzaSize):
    def __init__(self, name, multiplyCost):
        super().__init__(name, multiplyCost)

class SmallSize(PizzaSize):
    def __init__(self, name, multiplyCost):
        super().__init__(name, multiplyCost)
        
            
# Define Sauce Classes
class Sauce:
  def __init__(self, name, cost ):
    self.name = name
    self.cost = cost

  def get_cost(self):
    return self.cost

  def get_name(self):
    return self.name

class Olive(Sauce):
  def __init__(self, name, cost):
    super().__init__(name, cost)

class Mushrooms(Sauce):
  def __init__(self, name, cost):
    super().__init__(name, cost)

class GoatCheese(Sauce):
  def __init__(self, name, cost):
    super().__init__(name, cost)

class Meat(Sauce):
  def __init__(self, name, cost):
    super().__init__(name, cost)

class Onion(Sauce):
  def __init__(self, name, cost):
    super().__init__(name, cost)

class Corn(Sauce):
  def __init__(self, name, cost):
    super().__init__(name, cost)
    

# Define Decorator class for use pizza, pizzaSize and sauces classes together
class Decorator:
    def __init__(self, pizza: Pizza, pizzaSize: PizzaSize , sauces: List[Sauce] ):
        self.pizza = pizza
        self.pizzaSize = pizzaSize
        self.sauces = sauces

    def get_total_cost(self):
        return self.pizza.get_cost()*self.pizzaSize.get_multiplyCost() + sum([s.get_cost() for s in self.sauces])

    def get_all_name(self):
        return self.pizzaSize.get_name() + ' ' + self.pizza.get_name() + ' - ' + ' '.join([s.get_name() for s in self.sauces])


# Define chose Pizza, PizzaSize and Sauce functions for user choose.
def choosePizza(pizzaKod):
    return pizzas.get(pizzaKod)

def choosePizzaSize(pizzaSizeKod):
    return pizzaSizes.get(pizzaSizeKod)

def chooseSauce(*sauceKods):
    return [sauces.get(code) for code in sauceKods]

# Function for get User informations.
def getUserInfo():
    global name, tc, card, passw
    name = input("Lütfen İsminizi Giriniz(Çıkmak için q): ")
    if name == 'q':
        return None
    while True:
        tc = input("TC Kimlik giriniz(Çıkmak için q): ")
        if tc == 'q':
            return None
        elif (len(tc) != 11) | (not tc.isdigit()):
            print("Lütfen TC'niz olarak 11 haneli rakam değeri giriniz")
            continue
        break
    while True:
        card = input("Kredi Kartı numarası giriniz(Çıkmak için q): ")
        if card == 'q':
            return None
        elif (len(card) != 8) | (not card.isdigit()):
            print("Lütfen Kartınız olarak 8 haneli rakam değeri giriniz")
            continue
        break
    passw = input("Kredi Kartı şifresini giriniz(Çıkmak için q): ")
    if passw == 'q':
        return None
    return 1

# Function for get order informations
def getOrderInfo():
    while True:
        global pizzaKod, pizzaSizeKod, sauceKod, sauceKodList
        showMenu()
        pizzaKod = input("Lütfen seçmek istediğiniz pizza kodunu giriniz (Çıkmak için q): ")
        if pizzaKod == 'q':
            return None
        pizzaSizeKod = input("Lütfen seçmek istediğiniz pizza boyutunun kodunu giriniz (Çıkmak için q): ")
        if pizzaSizeKod == 'q':
            return None
        sauceKod = input("Lütfen seçmek istediğiniz sos kodlarını aralarında boşluk bırakarak giriniz (Çıkmak için q): ")
        if sauceKod == 'q':
            return None
        sauceKodList = sauceKod.split()
        
        if (pizzaKod not in pizzas.keys()) or (pizzaSizeKod not in pizzaSizes.keys()) or (not all(code in sauces.keys() for code in sauceKodList)):
            clear_screen()
            print('Lütfen kodları doğru bir şekilde giriniz.')
            continue
        return 1

# Function for save orders
def saveOrder():
    with open("G:\Drive'ım\GlobalAI-PizzaOrder\Orders_Database.csv", mode='a') as db:
        writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL , lineterminator='\n')
        writer.writerow([name, tc, card, passw, order.get_all_name(), order.get_total_cost(), date])
    
orders = []
# Define a loop for customer chooses.
while True:
    pizzas = {
    '1': ClassicPizza('Klasik Pizza', 40),
    '2': MargheritaPizza('Margarita Pizza', 50),
    '3': TurkPizza('Türk Pizza', 45),
    '4': DominosPizza('Dominos Pizza', 48)
    }

    pizzaSizes = {
    '01': BigSize('Büyük Boy', 1.5),
    '02': NormalSize('Normal Boy', 1),
    '03': SmallSize('Küçük Boy', 0.75),
    }

    sauces = {
    '11': Olive('Zeytinli', 4),
    '12': Mushrooms('Mantarlı', 5),
    '13': GoatCheese('Keci Peynirli', 7),
    '14': Meat('Etli', 12),
    '15': Onion('Soganlı', 2),
    '16': Corn('Mısırlı', 3)
    }  
    
    if getOrderInfo() is None :
        clear_screen()
        print('İyi günler dileriz.')
        break
    sauces = chooseSauce(*sauceKodList)
    order = Decorator(choosePizza(pizzaKod),choosePizzaSize(pizzaSizeKod), sauces)
    # print(order.get_name(), str(order.get_cost()) + "TL")
    orders.append(order)
    total_cost = sum([order.get_total_cost() for order in orders])
    for order in orders :
        print(f"Alınan ürün: {order.get_all_name()} \tTutar : {order.get_total_cost()} TL")
    print(f"Toplam tutar: {str(total_cost)} TL")
    
    cont_p = input("Siparişinize başka bir pizza eklemek istiyor musunuz: e/h => ")
    if cont_p == "e":
        clear_screen()
        continue
    
    print("Siparişiniz için kullanıcı bilgileriniz gerekmektedir.")
    if getUserInfo() is None :
        clear_screen()
        print('İyi günler dileriz.')
        break
        
    date = datetime.now()

    saveOrder()
    print('Siparişiniz alınmıştır.')

    cont = input("Başka sipariş vermek istiyor musunuz: e/h => ")
    if cont == "e":
        clear_screen()
        orders = []
        continue
    elif cont == "h":
        clear_screen()
        print('Afiyet olsun, iyi günler dileriz...')
        break

