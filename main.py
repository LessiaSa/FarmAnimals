class Animals:
    type_of_animal = ""
    name = ""
    voice = ""
    feeding = ""
    weight = 0
    egg = 0

    def eat(self, feeding):
        self.weight += feeding

    def collect_eggs(self,egg):
        self.egg += egg

    instance_ref = []
    def __init__(self):
        Animals.instance_ref.append(self)

green = Animals()
green.type_of_animal = "Goose"
green.name = "Серый"
green.voice = "Га-га"
green.feeding = "трава, рыба"
green.weight = 5
green.egg = 3



white = Animals()
white.type_of_animal = "Goose"
white.name = "Белый"
white.voice = "Га-га"
white.feeding = "трава, рыба"
white.weight = 6
white.egg =8


cow = Animals()
cow.type_of_animal = "Cow"
cow.name = "Манька"
cow.voice = "Муу"
cow.feeding = "сено"
cow.weight = 975
def milking(self, milk):
    self.milking_milk +=milk


sheep = Animals()
sheep.name = "Барашек"
sheep.type_of_animal = "Sheep"
sheep.voice = "Беее"
sheep.feeding = "трава"
sheep.weight = 35
def cut(self,wool):
    self.cut_it += wool



sheep1 = Animals()
sheep.name = "Кудрявый"
sheep.type_of_animal = "Sheep"
sheep.voice = "Беее"
sheep.feeding = "трава"
sheep.weight = 30
def cut1(self,wool):
    self.cut_it += wool

chicken = Animals()
chicken.type_of_animal = "Chicken"
chicken.name = "Ко-ко"
chicken.voice = "Ко-ко-ко,кудах"
chicken.feeding = "зерно"
chicken.weight = 2
chicken.egg = 15

chicken1 = Animals()
chicken1.type_of_animal = "Chicken"
chicken1.name = "Кукареку"
chicken1.voice = "Ко-ко-ко,кудах"
chicken1.feeding = "зерно"
chicken1.weight = 3

goat_horns = Animals()
goat_horns.type_of_animal = "Goat"
goat_horns.name = "Рога"
goat_horns.voice = "Мее"
goat_horns.feeding = "трава,сено,зерно"
goat_horns.weight = 25
def milking1(self, milk):
    self.milking_milk +=milk

goat_hooves = Animals()
goat_hooves.type_of_animal = "Goat"
goat_hooves.name = "Копыта"
goat_hooves.voice = "Мее"
goat_hooves.feeding = "трава, сено, зерно"
goat_hooves.weight = 29
def milking2(self, milk):
    self.milking_milk +=milk

duck = Animals()
duck.type_of_animal = "Duck"
duck.name = "Кряква"
duck.voice = "Кря-кря"
duck.feeding = "трава, рыба, зерно"
duck.weight = 4
duck.egg = 9

add = sum([x.weight for x in Animals.instance_ref])
print(add)
maximum = max([x.weight for x in Animals.instance_ref])
print(maximum)
