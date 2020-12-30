#----------------------->Function<------------------------
def my_friends():
    print("Aadila", "Mahnoor", "Khadija")
my_friends()
#by passing arguments
def my_friends(fname):
    print(fname + " " +"is my friend.")
my_friends("Aadila")
my_friends("Mahnoor")
my_friends("Khadija")
#call the function with 2 arguments.
def my_friends(fname, lname):
    print(fname+" "+lname)
my_friends("Aadila", "Fatima")
my_friends("Mahnoor", "Khan")
my_friends("Khadija", "tul kubra") #If we try to call the function with 1 or 3 arguments, we will get an error:

#By passing Arbitrary Keyword Arguments, (**kwargs)
# function will recieve dictionary argument
def my_friends(**friend):
    print("Arbitrary keyword argument = ", "Her last name is" + " "+ friend["lname"])
my_friends(fname="Mahnoor", lname="Khan")

# by passing Arbitrary Arguments, (*args) ....*args access item accordingly
# function will recieve tuple arguments
def my_friends(*friend):
    print("Arbitrary arguments = ", "My best friend is" + " " + friend[1])
my_friends("Mahnoor", "Aadila", "Sehrish")

#Keyword Arguments
#we can also send arguments with the key = value syntax.
def my_friends(f1, f2, f3):
  print("Keyword argument = ", "My best friend is " + f2)
my_friends(f1="Aadila", f2="Mahnoor", f3="Khadija")

#default parameter value
def my_friends(city = "Rahim Yar Khan"):
  print("I am from " + city)
my_friends("Sadiqabad")
my_friends("Sanjarpur")
my_friends()
my_friends("Lahore")

#Passing a List as an Argument
def my_friends(books):
    for x in books:
        print(x)
books = ["HR management", "communication skills", "Computer architecture"]
my_friends(books)

# return values
def my_friends(number):
    return 5 *number
print(my_friends(4))
print(my_friends(5))
print(my_friends(6))

#pass statement
def my_friends():
     pass   #if function with no content put the pass statement to avoid getting error

#---------------------------->Recursive function<------------------------
# the benefit of recursion is that we can loop through data to reach a result.
def try_recursion(x):
  if(x >= 0):
    result = x + try_recursion(x - 1)
    print(result)
  else:
    result = 0
  return result

print("My Recursion example results")
try_recursion(13)

#-------------------------->Methods<---------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def my_friend(self):
    print("Hello my name is " + self.name + " " + "and my age is= " + self.age)

p1 = Person("Aadila", "23")
p1.my_friend()

#modify object properties
p1.age = 25
print("Modified age is =", p1.age)
# delete object properties
#del p1.age
#print(p1.age) ........it causes error because there' no more p1.age value

#delete objects.........it causes error because there' no more p1 value
#del p1
#print(p1)
# pas statement
class Person:
    pass
