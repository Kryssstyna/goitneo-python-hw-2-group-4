class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            return str(e)

    def remove_phone(self, phone):
        try:
            self.phones.remove(Phone(phone))
        except ValueError:
            return "Phone number not found."

    def edit_phone(self, old_phone, new_phone):
        try:
            idx = self.phones.index(Phone(old_phone))
            self.phones[idx] = Phone(new_phone)
        except ValueError:
            return "Phone number not found."

    def find_phone(self, phone):
        try:
            idx = self.phones.index(Phone(phone))
            return str(self.phones[idx])
        except ValueError:
            return "Phone number not found."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(map(str, self.phones))}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, "Record not found.")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return "Record not found."

    def __str__(self):
        return '\n'.join(map(str, self.data.values()))


def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")

    book.delete("Jane")

    print(book)


if __name__ == "__main__":
    main()