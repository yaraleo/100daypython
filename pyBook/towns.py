"""This is exercise 3-10 book Python"""
towns = ["kyev", "moskow", "anapa", "tula", "rzhev", "tomsk"]
print(towns)
print(towns[0].title())
print(towns[3].title())
print(towns[-1].title())
towns.append("lensk")
print(towns)
del towns[3]
print(sorted(towns))
print(towns)
print(towns.sort())
print(towns)
towns.reverse()
print(towns)
