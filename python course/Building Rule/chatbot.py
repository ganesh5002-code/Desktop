import re, random

destinations = {
"beaches": ["Bali", "Maldieves", "Phuket"],
"mountains": ["Himalayas", "Blue Mountains", "Tibet"],
"cities": ["Tokyo", "Sydney", "Delhi"]
}

jokes = [
"Why don't programmers like nature? Too many bugs!",
"Why did the computer go to the doctor? Because it had a virus!",
"Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s", " ", text.strip().lower())

def recommend():
    print("travel_bot: what destinations, beaches, mountains and cities")
    answer = input("you:")
    answer = normalize_input(answer)
    
    if answer in destinations:
        suggestion = random.choice(destinations[answer])
        print("travel_bot: how about", suggestion)
        print("travel_bot: do you like it (yes/no)")
        answer = input("you:").lower()
    
        if answer == "yes":
            print("travel_bot: Awesome, enjoy the trip!")
        elif answer == "no":
            print("travel_bot: Let's try another")
            recommend()
        else:
            print("travel_bot: I'll suggest again")
            recommend()
    else:
        print("Sorry, I don't have that type of destination")
        recommend()

def packing():
    print("travel_bot: where to?")
    location = normalize_input(input("You:"))
    print("travel_bot: how many days?")
    days = input("You:")
    
    print(f"travel_bot: packing tips for {days} at {location}")
    print(f"versatile clothes \n charger/adaptor \n check the weather forecast")
    
def joke():
    print(f"travel_bot: {random.choice(jokes)}")
        

def show_help():
    print("I can offer")
    print("Suggest travel tips/spots")
    print("Offer some packing tips")
    print("Tell a joke")
    print("Type exit or bye to end")

def chat():
    print("Hello I am a travel bot")
    name = input("What is your name?")
    print(f"Hello {name}, nice to meet you")
    show_help()
    
    while True:
        user_input = input(f"{name}:")
        user_input = normalize_input(user_input)
        
        if "travel" in user_input or 'suggest' in user_input:
            recommend()
        elif "pack" in user_input or 'packing' in user_input:
            packing()
        elif "joke" in user_input or 'funny' in user_input:
            joke()
        elif "help" in user_input or 'please help' in user_input:
            show_help()
        elif "exit" in user_input or 'bye' in user_input:
            print("travel_bot: have a safe travel")
            break
        else:
            print("travel_bot: could you please rephrase")
    
if __name__ == "__main__":
    chat()