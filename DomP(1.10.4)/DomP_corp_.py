from Clients import Client

Cl1 = Client("Иван Петров"," г. Москва","Наставник")
Cl2 = Client("Иван Пупкин"," г. Киев","Помощник")
Cl3 = Client("Вася Артемов"," г. Львов","Генеральный директор")




clients = [Cl1,Cl2,Cl3]

for client in clients:
    if isinstance(client,Client):
        print(client.GetName(),"|",client.GetCity(),"|","Статус-",client.GetStatus())
