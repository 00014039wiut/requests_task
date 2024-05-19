from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'gender', 'height', 'weight'])
Emma = Person("Emma Watson", 25, 'female', 175, 65)

for i in [Emma.name, Emma.age, Emma.gender, Emma.height , Emma.weight]:
    print(i)
print("------------------------------------------------------------------------------------------------------------")
Product = namedtuple("Product", ["name", "price", "color", "country", "category"])
telephone = Product("Galaxy S22", 800, 'black', 'China', "Smartphones")
for i in [telephone.name, telephone.price, telephone.color, telephone.country, telephone.category]:
    print(i)