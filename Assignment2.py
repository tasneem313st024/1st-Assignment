# -------------------->Numbers<----------------------
import random
print(random.randrange(5,35))

a = 4.5
b = 4
c = "WizInsights"
d = 3+6j
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))



# ----------------->list<------------------------------
my_list = [23, 25, 7, 5, 9, "pakistan", "india", "USA", "UK", "Europe"]
a_list = [True, False, True, False, 2]
print(my_list)

# check length of list
print(len(my_list))

# access lis items
print(my_list[4])
print(my_list[:4])
print(my_list[3:])
print(my_list[4:9])
print(my_list[-6:-3])

# sort list
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)

# Add items
my_list.append("England")
print(my_list)
my_list.insert(3, "NewLand")
print(my_list)
my_list.extend(a_list)
print(my_list)

# joining of lists
print(a_list + my_list)
my_list.extend(a_list)
print(my_list)

# Remove item from list
my_list.remove("USA")
print(my_list)
del my_list[4]
print(my_list)

# pop method also used to remove a specific item from list.
my_list.pop()
print(my_list)

# check index
print(my_list.index("Europe"))

# change item of list
my_list[1:3] = ["Japan", "China"]
print(my_list)

# check type of list
print(type(my_list))

# copy list
my_list = a_list.copy()
print(my_list)
my_list = list(a_list)
print(my_list)


#---------------------> Dictionaries<-------------------------------

country = {"pakistan":23, "india":25, "USA":7, "UK":5, "Europe":9}
print(country["USA"])
# check keys of dictionary
print(country.keys())
# check type of dictionary
print(type(country))
# change dictionary
country["USA"] = 10
print(country)
# update dictionary
country.update({"UK": 15})
print(country)
# copy dictionary
my_dictionary = country.copy()
print(my_dictionary)
# del method remove a specific item and also removes the whole dictionary this will cause an error
del (country["india"])
print(country)
country.pop("USA")
print(country)
country.popitem()
print(country)
# remove items from dictionary
country.clear()
print(country)