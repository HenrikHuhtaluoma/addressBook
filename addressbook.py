
#Author: Henrik Huhtaluoma
import sqlite3
from sqlite3 import Error

#Create SQLite connection.
def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)

    return conn
#Creating query for adding a new contact.
def creteContact(conn, contact):
    
    sql = """ INSERT INTO contacts(contact_id,first_name,last_name,email,phone)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()

#Selection screen for which of the to modes you want to use view/edit.
def selectionScreen():

    print("Press 1 to view existing contacts or 2 to add new.")
    selection = input(":")
    return(selection)

#Asking user for contact details.
def addContact(database):

    conn = createConnection(database)
    with conn:
        #Checking amount of entries to generate userId.
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        userId = len(results)
        
        firstName = input("Give first name:")
        lastName = input("Give last name:")
        phoneNumber = input("Give phone number:")
        email = input("Give email:")
        contact = (userId, firstName, lastName, email, phoneNumber)
        creteContact(conn, contact)
#Printing existing contacts in db.
def viewContacts(database):

    conn = createConnection(database)
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
    for result in results:
        print(result)

def main():

    while True:
        #replace YOUR_DB_PATH with the full path of your sqlite .db file. r"YOUR_DB_PATH" in windows for escaping \.
        database = "YOUR_DB_PATH"
        selection  = selectionScreen()
        if selection == "2":
            addContact(database)
        elif selection == "1":
            viewContacts(database)
        else:
            print("unknown input")


if __name__ == '__main__': main() 
 
