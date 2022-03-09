from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3 )

item1.apply_discount()

print(item1.price)


# Inheritance
# methods uses across childe class


# polymorphism in action
# len("jim") = 3
# len(["hello", "world"])
# one method is able to apply to multiple objects

'''
Item.instantiate_from_csv()
print(Item.all)
'''

'''
print(Item.__dict__) # all attributes for class level
print(item1.__dict__) # all attributes for instance level
# show that the attribute are found in the class level but not the instance level
'''
