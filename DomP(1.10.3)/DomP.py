from Clients import Client

Cl1 = Client("Иван Петров",50)
Cl2 = Client("Ваня Пупкин",9 )

print("Клиент:",Cl1.GetName(),"Баланс:", Cl1.GetBalance(),"руб")
print("Клиент:",Cl2.GetName(),"Баланс:", Cl2.GetBalance(),"руб")