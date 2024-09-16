import mysql.connector

mydata = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amir@9860",
    database="bank"
)
cursor = mydata.cursor()
def admin():
    ID = input("Enter the id:")
    password = input("Password:")
    if(ID == "admin" and password == "admin123"):
        adminlist()
    else:
        print("Invalid password or id")



def adminlist():
    print("1.New account")
    print("2.Deposit")
    print("3.Delete account")
    print("4.Exit")
    choice = int(input("Enter the choices:"))
    match choice:
       case 1:
        new_account()
       case 2:
        deposit()
       case 3:
        delete()
       case 4:
        exit(0)
       case _:
        print("Invalid choices.")
    
def new_account():
    acc_number = input("Enter account number: ")
    name = input("Enter name: ")
    balance = int(input("Enter balance: "))
    
    insert_query = "INSERT INTO DETAILS (account_number, name, balance) VALUES (%s, %s, %s)"
    values = (acc_number, name, balance)
    
    cursor.execute(insert_query, values)
    
    mydata.commit()
    print("NEW ACCOUNT CREATED.")

def deposit():
    acc_number = input("Enter the account number you want to deposit: ")
    amount = int(input("Enter the amount to deposit: "))

    select_query = "SELECT balance FROM DETAILS WHERE account_number = %s"
    values = (acc_number,)
    cursor.execute(select_query, values)
    result = cursor.fetchone()

    if result:
        current_balance = result[0]
        new_balance = current_balance + amount

        update_query = "UPDATE DETAILS SET balance = %s WHERE account_number = %s"
        update_values = (new_balance, acc_number)
        cursor.execute(update_query, update_values)
        mydata.commit()
        print(f"Deposited {amount}. New balance: {new_balance}")
    else:
        print("No account found with the given account number.")
     
def delete():
    acc_delete = input("Enter the account number you want to delete:")
    select_query = "Select * from DETAILS WHERE account_number = %s" 
    values = (acc_delete,)
    cursor.execute(select_query, values)
    result = cursor.fetchone()   
    if result:
     delete_query = "DELETE from DETAILS WHERE account_number = %s" 
     values = (acc_delete,)
     cursor.execute(delete_query, values)
     mydata.commit()
     print("Account sucess Deleted.")
    else:
     print("No given account.")

def user():
    acc_number = input("Enter your account number:")
    select_query = "select * from DETAILS where account_number = %s"
    values = (acc_number,)
    cursor.execute(select_query,values)
    result = cursor.fetchone()
    if result:
        account_number = result[0]
        name = result[1]
        balance = result[2]
        print(f"Account number : {account_number}")
        print(f"Name : {name}")
        print(f"Balance : {balance}")


    else:
        print("Account not found") 


    print("1.SEND MONEY") 
    print("2.EXIT")    
    choice = int(input("Enter your choice:"))
    match choice:
     case 1 :
       send(acc_number)
     case 2 :
       exit(0) 
     case _ :
       print("Invalid choice. Enter again.")
def send(sender_Account):
    acc_number = input("Enter the account number to send money:")
    amount = int(input("Enter the amount to send:"))
    select_query = "SELECT balance FROM DETAILS WHERE account_number = %s"
    values = (acc_number,)
    cursor.execute(select_query, values)
    result = cursor.fetchone()

    if result:
        current_balance = int(result[0])
        new_balance = current_balance + amount

        update_query = "UPDATE DETAILS SET balance = %s WHERE account_number = %s"
        update_values = (new_balance, acc_number)
        cursor.execute(update_query, update_values)
        mydata.commit()
        confirm = True
    else:
        print("No account found with the given account number.")
        confirm = False

    select_query = "SELECT balance FROM DETAILS WHERE account_number = %s"
    values = (sender_Account,)
    cursor.execute(select_query, values)
    result = cursor.fetchone()

    if result:
        if(result[0] > amount):
         sender_balance = int(result[0])
         news_balance = sender_balance - amount
         update_query = "UPDATE DETAILS SET balance = %s WHERE account_number = %s"
         update_values = (news_balance, sender_Account)
         cursor.execute(update_query, update_values)
         mydata.commit()
         confirm_two = True
        else:
            print("Insufficient amount.") 
    else:
        print("No account found with the given account number.")
        confirm_two = False 
    
    if (confirm and confirm_two):
        print("Sended sucessfully")
    
    else:
        print("Send unsucessfull.")


#  main  
print("1.Admin")
print("2.User")
print("3.Exit")
choices = int(input("Enter the choices:"))
match choices:
  case 1:
   admin()

  case 2:
   user()
    
  case 3:
   exit(0)

  case _:
   print("Invalid choices.") 
  
