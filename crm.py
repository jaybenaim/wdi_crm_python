from contact import Contact
import sys 

class CRM:

    def main_menu(self):
      try: 
        while True: # repeat indefinitely
          self.print_main_menu()
          user_selected = int(input())
          self.call_option(user_selected)
      except ValueError: 
          sys.exit("Goodbye!") 

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')


    
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
            self.search_by_attribute()
        elif user_selected == 6:
            sys.exit("Goodbye!") 
        else: 
          return 'You entered an invalid selection'

    
        
    def add_new_contact(self):
        
        first_name = input('Enter First Name:\n')
        last_name = input('Enter Last Name:\n')
        email = input('Enter Email Address:\n')
        note = input('Enter a Note:\n')
        Contact.create(first_name, last_name, email, note)
    
    # def modify_existing_contact(self):
    #     attribute_to_update = input("Which attribute are you trying to change?\n")
    #     value = input("Which value would you like to change?\n")
  
    #     Contact.update(attribute_to_update, value)
          #
          #
          # def delete_contact(self):
          #
          #
    def display_all_contacts(self):

        print(Contact.all())
        print() 
        

          #
          # def search_by_attribute(self):


crm = CRM() 

crm.main_menu()
# Contact.create("Jacob", "Benaim", "B@m.com", "hi")
