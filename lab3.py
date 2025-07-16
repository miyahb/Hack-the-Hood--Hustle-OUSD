# Lab 3 - Samiyah

# Task 1
food = "crab legs"
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
seperated = food.split()
print(seperated)
combined = ' '.join(seperated)
print(combined)

#Task 2
number_list = [12, 34, 56, 78, 910]
number_list.append(345)
print(number_list)
number_list.insert(3, 345)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(34)
print(number_list)
print(number_list[0:3])
print(number_list[-3:])

#Task 3
books = {"Elisabetta Dami" : "Four Mice Deep in the Jungle",
"Selina" : "Working in Python", 
"Rabindranath Tagore": "Gitanjali", "Dr.Seuss":"Cat in the Hat"}
print(books.keys())
books.values()
print(books.values())
print(books.get("Dr.Seuss"))
print(books.pop("Rabindranath Tagore"))
print(books)
del books["Elisabetta Dami"]
print(books)