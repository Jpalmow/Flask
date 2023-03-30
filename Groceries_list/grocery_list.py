import sqlite3


groceries = [
    
    "apple",
    "bananas",
    "clemintines",
    "dill",
    "eggs",
    "flour",
    "granola",
    "honey",
    "ice cream",
    "juice",
    "ketchup",
    "lemon", 
    "margarine",
    "nugats",
    "onion",
    "potatoes",
    "rosmary",
    "salt",
    "thyme",
    "vinegar",
    "watermelon",
    "pears",
    "cucumbers",
    "garlic",   
    "carrots",
    "pastrines",
    "eggplants",
    "milk",
    "coffe",
    "tea",
    "rice",
    "noodles",
    "strawberies",
    "mangos",
    "pappers",
    "lime",
    "broth",
    "mushrooms",
    "chicken",
    "beef",
    "pork",
    "fish",
    "cream",
    "paprika",
    "cinamon",
    "pumpkin",
    "basil",
    "oregano",
    "tomatoes",
    "bread",
    "cake",
    "gum",
    "pineapple",
    "oranges",
    "cheese",
        
]

groceries = sorted(groceries)
connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
    cursor.execute("insert into groceries (name) values (?)", [groceries[i]])
    print("added ", groceries[i])
    
connection.commit()
connection.close()






