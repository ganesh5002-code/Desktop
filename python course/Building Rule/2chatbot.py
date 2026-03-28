import re
import random


times = {
    'tokyo':'8:00',
    'sydney':'10:00',
    'delhi':'4:30',
    'paris':'0:00',
    'london':'23:00',
    'bangkok':'6:00'
}

news_reports = [
    "There has been a toxic-poppy theft where 1700 poppies were stolen.",
    "Many floods are happening across Australia.",
    "Coughing has started to increase in rates.",
]


def normalize_input(text):
    return re.sub(r'\s+', ' ', text.strip().lower())


def weather():
    print("The temperature in Perth today was between 14–28 degrees Celsius.")


def news():
    print("chatbot:", random.choice(news_reports))


def time():
    print("travel_bot: You can choose from: Tokyo, Sydney, Delhi, Paris, London, Bangkok")
    print("travel_bot: Which city would you like to know the time for?")
    
    while True:
        answer = input("you: ").strip()
        answer = normalize_input(answer)
        
        if answer in times:
            print(f"travel_bot: In {answer.capitalize()} it is {times[answer]} when it's 7:00 in Perth.")
            print("travel_bot: Do you like this suggestion? (yes/no)")
            
            while True:
                like = input("you: ").strip().lower()
                if like in ("yes", "y"):
                    print("travel_bot: Awesome, enjoy the trip!")
                    return
                elif like in ("no", "n"):
                    print("travel_bot: Let's try another city then.")
                    break
                else:
                    print("travel_bot: Please answer yes or no.")
        elif answer in ("exit", "quit", "back"):
            return
        else:
            print("travel_bot: Sorry, I don't have that destination. Try one of: Tokyo, Sydney, Delhi, Paris, London, Bangkok")


def show_help():
    print("I am a simple multi-purpose chatbot.")
    name = input("What is your name? ").strip()
    if name:
        print(f"Hello {name}, nice to meet you!")
    else:
        name = "friend"
        print("Okay, I'll call you friend then 😄")

    print("\nI can help you with:")
    print("  1. Weather report (Perth)")
    print("  2. Random news update")
    print("  3. Local time in other cities (relative to 7:00 in Perth)")
    print("\nJust type 1, 2, 3 or 'exit' to quit.\n")

    while True:
        user_input = input(f"{name}: ").strip()
        user_input = normalize_input(user_input)

        if user_input in ("1", "weather", "w"):
            weather()
        elif user_input in ("2", "news", "n"):
            news()
        elif user_input in ("3", "time", "t", "cities", "city"):
            time()
        elif user_input in ("exit", "quit", "bye", "q"):
            print("Goodbye! Have a great day.")
            break
        else:
            print("Sorry, I didn't understand. Please type 1, 2, 3 or 'exit'.")


if __name__ == "__main__":
    show_help() 
