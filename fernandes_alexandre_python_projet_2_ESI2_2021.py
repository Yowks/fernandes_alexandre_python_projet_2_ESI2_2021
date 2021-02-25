pizzas_instances = []
meat = ["boeuf","poulet","merguez", "jambon"]
perso = True

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


class Pizza:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.ingredients = []
    self.veggie = self.is_veggie()

  def addIngredients(self, ingredient):
    for i in ingredient : 
      self.ingredients.append(i.lower())

  def display(self):
    self.veggie = self.is_veggie()
    if self.veggie == True : 
      veggie = "Végétarien"
    else : 
      veggie = "Non végétarien"
    
    print("Pizza %s | %s€ | %s" % (self.name, round(self.price,2),veggie))
    for inc in self.ingredients:
      print("- %s" %(inc))

  def is_veggie(self):
    common = list(set(meat).intersection(self.ingredients))
    if len(common)>0 : 
      return False
    else :
      return True

class CustomPizza(Pizza):
    def __init__(self, name, price):
        Pizza.__init__(self, name, price)

    def requestIngredients(self):
        more = 0
        while more == 0 :
          compo = input('Indiquez les ingrédients à ajouter à votre pizza personnalisé (ENTER pour terminé) : ')
          if compo == "":
            more = 1
            self.display()
            return
          else :
            self.ingredients = self.ingredients + [compo]
            self.price += 1.2

# Default :
pizza_1 = Pizza("4 fromages", 8.5)
pizza_1.addIngredients(['Brie','Emmental', 'Compté', 'Parmesan'])

pizza_2 = Pizza("4 saisons", 11)
pizza_2.addIngredients(['Oeuf','Emmental', 'Tomate', 'Jambon', 'Olives'])

pizza_3 = Pizza("Végétarienne", 7.8)
pizza_3.addIngredients(['Champignons', 'Tomate', 'Oignons', 'Poivrons'])

pizzas_instances = [pizza_1, pizza_2, pizza_3]



while perso == True :
  choice = int(input('Voir le menu (1) ou créer votre propre pizza(2) ?'))

  if choice == 1 :
    for i in range(len(pizzas_instances)) :
      pizzas_instances[i].display()
  elif choice == 2 : 
    pizza_perso = CustomPizza('perso', 7)
    pizza_perso.requestIngredients()
    pizzas_instances.append(pizza_perso)