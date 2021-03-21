from Cats import Cat
from dogs import Dog

Baron = Cat("Baron","Man",2)
Sem = Cat("Sam","Man",2)

Felix = Dog("Felix","Man",2)
Linda = Dog("Linda","Girl",2)
Muhtar= Dog("Muhtar","Man",0)

print("Cats:\n")
print(Baron.get_name(),Baron.get_gender(),Baron.get_age())
print(Sem.get_name(),Sem.get_gender(), Sem.get_age())

print("\n------------------------------\n")

print("Dogs:\n")
print(Felix.get_name(),Felix.get_gender(),Felix.get_age())
print(Linda.get_name(),Linda.get_gender(), Linda.get_age())
print(Muhtar.get_name(),Muhtar.get_gender(), Muhtar.get_age())



