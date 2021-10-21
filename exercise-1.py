monthly_expense = {
    "January": 2200,
    "Febuary": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190
}


# 1. In Feb, how many dollars you spent extra compare to January? 

dollars_extra = monthly_expense["Febuary"] - monthly_expense["January"]
print(dollars_extra)

# 2. Find out your total expense in first quarter (first three months) of the year.

def quaterExpense():
    value = monthly_expense["January"] + monthly_expense["January"] + monthly_expense["January"]
    return value


print(quaterExpense())

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly 
# expense list

monthly_expense["June"] = 1980
print(monthly_expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

monthly_expense["April"] = monthly_expense["April"] - 200
print(monthly_expense)

print("\n")
print("\n")
print("\n")
# 2. You have a list of your favourite marvel super heros.

heros = ['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list

n = len(heros)
print(n)

# 2. Add 'black panther' at the end of this list

heros.append("black panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
n = len(heros)
def hulkChange(heros, n):
    for i in range(n):
        if heros[i] == "hulk":
            return i


heros.insert(int(hulkChange(heros, n)) + 1, "Black Panther")
print(heros)
    
# 4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.

heros.remove("hulk" and "thor") and heros.append("doctor strange")
print(heros)

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


heros = ['spider man','thor','hulk','iron man','captain america']

heros.sort()
print(heros)

print("\n")
print("\n")

# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

max_value = input('max value: ')

odd_list = []
def fullListValues(): 
    for x in range(int(max_value)):
        values = int(max_value) - x
        if values % 2 == 0:
            odd_list.append(values)

fullListValues()
print(odd_list)
        
        
