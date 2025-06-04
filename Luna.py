class MagicalCreature:
    def __init__(self):
        self.name = "Luna"
        self.color = "pink"
        self.age = 3
        self.mood = "neutral"

    def greet(self):
        print(f"Hi, I’m {self.name}, your magical creature!")
        print(f"My color is {self.color} and I am {self.age} years old.")
        print("How are you feeling today?")

    def react(self, feeling):
        if feeling.lower() == "happy":
            self.mood = "joyful"
            print("Yay! I’m so glad you’re feeling happy! 🌞 Wanna tell me why?")
        elif feeling.lower() == "sad":
            self.mood = "concerned"
            print("Oh no… I’m here for you, always 🫂 Wanna tell me why?")
        else:
            self.mood = "curious"
            print("Hmm… that’s interesting. I’m listening 🌙")

    def respond_to_reason(self, reason):
        reason = reason.lower()
        work_words = ["work", "study", "job", "school", "unemployed", "boss", "office", "exam"]
        family_words = ["friends", "family", "partner", "parents", "siblings", "children"]

        if any(word in reason for word in work_words):
            print("I see... lots of strength and luck! 💪🍀")
        elif any(word in reason for word in family_words):
            if self.mood == "joyful":
                print("Woow, I’m so happy to hear it! 🥳")
            elif self.mood == "concerned":
                print("Oh, I’m sorry to hear that... sending you a big hug 🤗")
            else:
                print("Friends and family are important. I’m here for you.")
        else:
            print("Thanks for sharing that with me.")

    def show_mood(self):
        print(f"{self.name}'s current mood is: {self.mood}")

# Código para interactuar con Luna
luna = MagicalCreature()
luna.greet()
feeling = input("You: ")
luna.react(feeling)
reason = input("You: ")
luna.respond_to_reason(reason)
luna.show_mood()