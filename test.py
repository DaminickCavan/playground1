
class Playground():

    def __init__(self, data):
        self.data = data 


    def get_item(self, key):
        return self.data.get(key)
    

playground_instance = Playground({
    "name": "Jeff",
    "age": 25,
    "city": "Des Moines"
})

print(playground_instance.get_item("name"))          # Output: Alice
print(playground_instance.get_item("age"))           # Output: 25
print(playground_instance.get_item("city"))          # Output: Des Moines
print(playground_instance.get_item("country"))       # Output: None


    