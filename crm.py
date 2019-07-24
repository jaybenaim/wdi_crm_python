from contact import Contact
import sys
import sqlite3

class CRM:
    def main_menu(self):
        try:
            while True:
                self.print_main_menu()
                user_selected = int(input())
                self.call_option(user_selected)
        except ValueError:
            sys.exit("Goodbye!")

    def print_main_menu(self):
        print("[1] Add a new contact")
        print("[2] Modify an existing contact")
        print("[3] Delete a contact")
        print("[4] Display all the contacts")
        print("[5] Search by id")
        print("[6] Exit")
        print("Enter a number: ")

    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_id()
        elif user_selected == 6:
            sys.exit("Goodbye!")
            close() 
        else:
            return "You entered an invalid selection"

    def add_new_contact(self):

        first_name = input("Enter First Name:\n")
        last_name = input("Enter Last Name:\n")
        email = input("Enter Email Address:\n")
        note = input("Enter a Note:\n")
        
        contact = Contact.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            note=note)

        

    def modify_existing_contact(self):
        
        user_id = input("Please enter your id number\n")
        attribute_to_update = input("What are you trying to change? \n (first_name, last_name, email, note)\n").lower()
        value = input("Which would you like to change it to?\n")
        
        try: 
            cur=Contact.db.cursor() 
            if attribute_to_update == 'first_name': 
                qry=f"update contact set first_name=? where id=?"
                cur.execute(qry,(f'{value}', f'{user_id}'))
                Contact.db.commit()
                print('record updated succesfully')
            if attribute_to_update == 'last_name': 
                qry=f"update contact set last_name=? where id=?"
                cur.execute(qry,(f'{value}', f'{user_id}'))
                print('record updated succesfully')
            if attribute_to_update == 'email': 
                qry=f"update contact set email=? where id=?"
                cur.execute(qry,(f'{value}', f'{user_id}'))
                print('record updated succesfully')
            if attribute_to_update == 'note': 
                qry=f"update contact set note=? where id=?"
                cur.execute(qry,(f'{value}', f'{user_id}'))
                print('record updated succesfully')
        except: 
            print("something went wrong")
            # Contact.rollback() 
            # Contact.db.close() 
        
        # user_id = input("Please enter your id number\n")
        # attribute_to_update = input("What are you trying to change? \n (first name, last name, email, note)\n").lower()
        # value = input("Which would you like to change it to?\n")

        # contact = Contact.get(id=user_id)
        # if user_id == contact.id:
        #     if attribute_to_update == 'first name': 
        #         contact.first_name = value
        #         contact.save()  
        #     elif attribute_to_update == 'last name': 
        #         contact.last_name = value
        #         contact.save()  
        #     elif attribute_to_update == 'email': 
        #         contact.email = value
        #         contact.save()
        #     elif attribute_to_update == 'note': 
        #         contact.note = value
        #         contact.save() 

        
    def delete_contact(self):
        contact_to_delete = input("Which contact would you like to delete? \nEnter the id for the contact you wish to delete:\t")
        contact = Contact.get(id=contact_to_delete)
        confirm = input('Are you sure you would like to delete this contact?\t (y/n)').lower()
        
        if confirm == 'y': 
            contact.delete_instance() 
            print("Succesfully deleted contact!")
        else: 
            self.main_menu() 
        
    def display_all_contacts(self):

        cur = Contact.db.cursor()
        cur.execute("SELECT * FROM contact;")
        all_contacts = cur.fetchall() 
        
        for contact in all_contacts: 
            print(contact) 
        

    def search_by_id(self):
        contact_id = input("What is the id of the contact you are searching for? \n")
        contact = Contact.get(id=contact_id)
        print(f'First Name: {contact.first_name} Last Name: {contact.last_name} Email: {contact.email} Note: {contact.note}')
        return contact.id
        # print(Contact.find_by(search_by_id, search_by_value)
        # #which_search_method = ("Would you like to search by the 'ids' or 'values'? \n").lower() 
        # search_by_id = input("What id would you like to search for?\n ")
        # search_by_value = input("Which value would you like to search for?\n")



crm = CRM()
crm.main_menu()


# Contact.create("Jacob", "Benaim", "B@m.com", "hi")
# crm.delete_contact()
# crm.search_by_id()
# print(Contact.all())
