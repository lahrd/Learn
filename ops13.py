import requests
Confirm=imput ("Comfirm")
HTTPMethod=input("Enter your HTTP Method: GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS.")
print("My HTTP Method", HTTPMethod)
print("Confirm?", HTTPMethod, Confirm)
Confirm=imput("Comfirm")
if Confirm == "Yes":
    print("Yay!")
elif Confirm == "No":
    print("Start Over.")