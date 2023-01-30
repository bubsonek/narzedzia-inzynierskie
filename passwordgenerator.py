#Password Generator Project - wygeneruj hasło według swoich kryteriów
import random
# listy z wyszczególnionymi możliwymi literami, symbolami oraz cyframi
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '[', ']']

print("Welcome to the PyPassword Generator!")

#wybierz ilość poszczególnych liter, symboli oraz cyfr dla swojego hasła
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list=[]

#wylosuj spośród przygotowanych list poszczególne litery, symbole i cyfry
for letter in range(1,nr_letters+1):
    password_list.append(random.choice(letters))

for symbol in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))

for number in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

#zmień kolejność podanych liter, symboli i cyfr w haśle
random.shuffle(password_list)

#połącz hasło - z listy na string
password=""
for x in password_list:
    password=password+x

#wywołaj hasło
print(password)