pizzas = ["pronto", "vegan" , "kolbasish", "koyakin"]
for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I really like pizza!")
friend_pizzas = pizzas[:]
pizzas.append("chumovaya")
friend_pizzas.append("afdaddfgsfdg")
for pizza in pizzas:
    print (pizza)

for pizza in friend_pizzas:
    print(pizza)
