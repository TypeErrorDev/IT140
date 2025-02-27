# Create a Pet class where each pet has:
# - A name and type (like "dog" or "cat")
# - A method called 'speak' that prints a different sound based on the type
# - A method called 'play' that prints what the pet is playing with
class Pet:
    def __init__(self):
        self.name = ''
        self.type = ''

    def speak(self, sound):
        print('')

    def play(self, toy):
        print('')
# Example usage should work like this:
fluffy = Pet("Fluffy", "cat")
rex = Pet("Rex", "dog")
fluffy.speak()  # Should print: Fluffy says: Meow!
rex.speak()     # Should print: Rex says: Woof!
fluffy.play("yarn")  # Should print: Fluffy is playing with yarn