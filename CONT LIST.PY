names_list = []
phone_numbers_list = []
number_of_entries = 2
for _ in range(number_of_entries):
    name = input("please enter the valid name: ")
    phone_number = input("please enter the valid phone no: ") 
    names_list.append(name)
    phone_numbers_list.append(phone_number)
print("\nname\t\t\tphone number\n")
for i in range(number_of_entries):
    print(f"{names_list[i]}\t\t\t{phone_numbers_list[i]}")
search_term = input("\nEnter search term: ")
print("Searching for the  result:")
if search_term in names_list:
    index = names_list.index(search_term)
    phone_number = phone_numbers_list[index]
    print(f"Name: {search_term}, Phone Number: {phone_number}")
else:
    print("Name that you entered is not found")