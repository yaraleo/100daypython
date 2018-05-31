players = ['charles', 'martina', 'michael', 'florence', 'eli', 'asdf']
print("Here is players")
for player in players[:3]:
    print(player.title())
my_players = players[:]
print(players)
print(my_players)
print("The first thre items:")
print(players[:3])
print(players[2:5])
print(players[-3:])
