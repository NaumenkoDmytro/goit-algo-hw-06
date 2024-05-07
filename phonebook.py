from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("The number is not valid!")
        super().__init__(value)

                   
             

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
           self.phones.append(Phone(phone))
    

    def remove_phone(self, phone):
           self.phones = [p for p in self.phones if p != phone]
           
    
    def edit_phone(self, old_phone, edited_phone):
        for i, p in enumerate(self.phones):
            if str(p) == old_phone:
                self.phones[i] = Phone(edited_phone)
                break


    

    def find_phone(self, current_phone):
           for phone in self.phones:
               if current_phone == str(phone):
                     return phone  


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):


    def add_record(self,record):
       self.data[record.name.value] = record
           


    def find(self, name):
           return self.data.get(name)
           
    

    def delete(self,name):
       del self.data[name]


if __name__ == "__main__":


# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("123456789012asdf")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
       print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

