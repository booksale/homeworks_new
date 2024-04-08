#Task1
#Rb+r

#Task2
import re
def validate_number_of_card(number):
    pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
    if re.match(pattern, number):
        return True
    else:
        return False

number = input("Enter the cart number:")
print(validate_number_of_card(number))

#
def validate_number_of_card_2(number):
    pattern = r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$"
    if re.match(pattern, number):
        return True
    else:
        return False

number = input("Enter the cart number:")
print(validate_number_of_card_2(number))



#Task3
import re
def validate_email(email):
    if not email:
        return "Email cannot be empty."

    if email[0] == '-' or email[0] == '_':
        return "Email cannot start with '-' or '_'."

    pattern = r'^[0-9a-zA-Z]+(?[_-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return f"Email '{email}' is correct."
    else:
        return f"Email '{email}' is not correct."

email = input("Enter an email address:")
print(validate_email(email))

#Task4
import re

def validate_login(login):
    pattern = r"^[a-zA-Z0-9]{2,10}$"
    if re.match(pattern, login):
        return True
    else:
        return False

login = input("Enter the login:")
print(validate_login(login))

#
import re

def validate_login_2(login):
    pattern = r"^[a-zA-Z\d]{2,10}{2,10}$"
    if re.match(pattern, login):
        return True
    else:
        return False

login = input("Enter the login:")
print(validate_login(login))

