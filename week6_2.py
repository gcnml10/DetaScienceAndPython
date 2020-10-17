class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def speak(self):
        print('Ah~')

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

kim = Person('min',25,'male')

print(kim.get_sex())