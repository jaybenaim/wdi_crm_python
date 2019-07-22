class Contact:
    contacts = []
    next_id = 1 

    def __init__(self, first_name, last_name, email, note):
        """This method should initialize the contact's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note
        self.id = Contact.next_id
        if self.first_name not in Contact.contacts and self.last_name not in Contact.contacts: 
            Contact.next_id += 1 
        # Contact.contacts.append(self)
       

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.note}"
    


    @classmethod
    def create(cls, first_name, last_name, email, note):
        """This method should call the initializer,
    store the newly created contact, and then return it
    """
        new_contact = Contact(first_name, last_name, email, note)
        if new_contact not in cls.contacts: 
            cls.contacts.append(new_contact)
        return new_contact 

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        all_contacts = [] 
        for contact in cls.contacts: 
            all_contacts.append(contact) 
        return all_contacts

    @classmethod
    def find(cls, contact_id):
        """ This method should accept an id as an argument
    and return the contact who has that id
    """
        for contact in cls.contacts:
            if contact.id == contact_id:  
                return contact


    def update(self, attr_to_update, new_value):
        """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    # """
        if attr_to_update.lower() == 'first_name': 
            self.first_name = new_value
        if attr_to_update.lower() == 'last_name': 
            self.last_name = new_value
        if attr_to_update.lower() == 'email': 
            self.email = new_value
        if attr_to_update.lower() == 'note': 
            self.note = new_value

            
           
    @classmethod
    def find_by(cls, attribute, value):
        """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
        if attribute == 'first_name': 
            for contact in cls.contacts:
                if contact.first_name == value:  
                    return contact
        if attribute == 'last_name': 
            for contact in cls.contacts:
                if contact.last_name == value:  
                    return contact
        if attribute == 'email': 
            for contact in cls.contacts:
                if contact.email == value:  
                    return contact
        if attribute == 'note': 
            for contact in cls.contacts:
                if contact.note == value:  
                    return contact

         
    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""
        cls.contacts.clear() 
        

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return f'{self.first_name} {self.last_name}'

    def delete(self):
        """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
        Contact.contacts.remove(self) 


    # Feel free to add other methods here, if you need them.



# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')

# print(Contact.contacts)
# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id)
# print(Contact.find(contact1.id))
# print(Contact.all())
# contact1.update('first_name', 'John')
# contact1.update('last_name', 'Smith')
# contact1.update('email', 'JohnSmith@smith.com')
# contact1.update('note', 'lorum lorem lorem lorem lorem')
# print(Contact.find_by('note', 'beep boop'))
# print(Contact.all())
# Contact.delete_all() 
# print(Contact.all())

# print(contact1.full_name())

# print(Contact.all())
# contact1.delete() 
# print(Contact.all())