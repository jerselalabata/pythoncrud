
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='jersel',
    password='jerselalabata',
    db='sqlcrud'
)

print("myphonebook")
def print_menu():
	print("[1] -View Phone Numbers")
	print("[2] -Add Phone Numbers")
	print("[3] -Remove a Phone Number")
	print("[4] -Lookup a Phone Number")
	print("[5] -Exit")


def add_record(name,number):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `crud` (`name`, `number`) VALUES (NULL, %s, %s);"
        try:
            cursor.execute(sql, (name,number))
            print("New Record Successfully Added!")
        except:
            print("Oops! Something wrong")

    connection.commit()

numbers = {}
names = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = raw_input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Lookup Number")
        name = raw_input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print_menu()