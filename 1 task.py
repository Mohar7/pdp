
class Srudent:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def about(self):
        return f"Name: {self.first_name}\n" \
               f"Lastname: {self.last_name}\n" \
               f"Age: {self.age}"


person = Srudent('Muxriddin', 'Muxiddinxojayev', 17)

print(person.about)