# ------------------------->Tuples<------------------------------
veg = ("onion", "potato", "tomato", "pepper", "carrot")
Fruits = ("orange", "banana", "apples", "grapes")
print(veg)
print(type(veg))
print(len(veg))
print(veg[1])
print(veg[-2])
print(veg[2:4])
b = list(veg)
b[2:4] = "pea", "cabbage"
veg = tuple(b)
print(veg)
b.append("tomato")
veg = tuple(b)
print(veg)
b.remove("cabbage")
veg = tuple(b)
print(veg)
# del veg -> print(veg) tuple is deletd due to this it cause an error.
# unpacking of tuple
print("onion")
print("potato")
print("tomato")
print("pepper")
print("carrot")

# joining and multiplying of tuples

print(veg + Fruits)
print(veg*3)

# ------------------------->Sets<------------------------------
# sets are unchangeable, Unindexed and unordered
nida_friends = {"Aadila", "Mahnoor", "Tasneem", "Sumaira"}
print(nida_friends)
print(type(nida_friends))
print(len(nida_friends))
# by using set constructor
my_friends = set(("Aadila", "Mahnoor", "Khadija", "Sumaira", "Nida"))
# access the set item
print(my_friends)
for x in my_friends:
    print(x)
print("Mahnoor" in my_friends)
# add items in a set.
my_friends.add("Sehrish")
print(my_friends)
my_friends.update(nida_friends) # we can add list in a set by using update() method.
print(my_friends)
# joining of sets
print(my_friends.union(nida_friends)) # update() also used to join the sets.
nida_friends.intersection_update(my_friends)
print(nida_friends)
print(my_friends.intersection(nida_friends))
# Remove item from set
my_friends.remove("Nida")
print(my_friends)
my_friends.discard("Sehrish")
print(my_friends)
a = nida_friends.pop()
print(a)
nida_friends.clear()
print(nida_friends)
# del method removes the whole set and it causes error.
#del my_friends
#print(my_friends)

#------------------------>Booleans<--------------------------
print(nida_friends > my_friends)
print(my_friends == nida_friends)
print(my_friends >= nida_friends)
if my_friends > nida_friends:
    print("Tasneem's friends are greater than Nida's friends.")
else:
    print("Nida's friends are greater than Tasneem's friends.")

