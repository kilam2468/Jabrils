# Init Variables
theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["", "", "", ""]
adj = ["", ""]
# Get input from User
print("Welcome User!")
print("Lets play a game of MadLibs")
neo = input("Please share with me your name: ")

# Getting the matrix variable from user
print(f"Hello {neo}! Are your ready?")
theMatrix = input("What is something you want to know more about: ")

# Getting system variable from user
print(f"Oooh! You want to know more about {theMatrix} huh?")
print(f"Okay well first, tell me what you already know about {theMatrix}")
system = input(f"What noun would you categorize {theMatrix} as: ")

# Getting enemy from user
enemy = input(f"Give me an opposing noun to {system}: ")

# Getting inside from user
inside = input(f"Now give me any relaxing noun (present tense): ")

# Getting all profession variables from user
print(f"Okay, now I need 4 professions relating to {system}")
for i in range(len(profession)):
    profession[i] = input(f"profession (plural) {i + 1} / {len(profession)}: ")

# Getting the save variable
save = input(f"Hive me a hero-related verb (present tense): ")

# Getting an Unplugged Variable
unplugged = input(f"Now give me a verb that make you think about relief (past tense): ")

# Getting the adjectives
print(f"Lastly, I need 2 dystopian adjectives")

for i in range(len(adj)):
    adj[i] = input(f"Adjective {i + 1} / {len(adj)}: ")

# Getting the fight variable
fight = input(f"& a verb: ")

# Init Story
madlibsStory = (f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
                f"\nBut when you're {inside}, you look around, what do you see? " +
                f"\n{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds " +
                f"\nof the people we are trying to {save}. But until we do, " +
                f"\nthese people are still a part of that {system} and that makes " +
                f"\nthem our {enemy}. You have to understand, most of these people " +
                f"\nare not ready to be {unplugged}. And many of them are so {adj[0]}, " +
                f"\nso hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

# Print Story
print(madlibsStory)
input()
