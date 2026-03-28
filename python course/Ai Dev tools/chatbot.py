day = input("How was your day? (good/bad): ").lower()

if day == 'good':
    print("That's great to hear! Stay happy and positive!")
    ask = input("Is there anything you would like to ask? (homework/personal issues) ").lower()

    if ask == 'homework':
        print("Okay, I'll help you out in a bit.")
    elif ask == 'personal issues':
        print("I'm sorry about that. I'll go through some tips with you.")
    else:
        print("Sorry, I couldn't quite understand you.")

elif day == 'bad': 
    print("If it helps, take some time to rest and think about the positives.")
    ask2 = input("What happened that made your day a bad one? (got in trouble/bullying)").lower()

    if ask2 == 'got in trouble':
        print("It's alright—everyone messes up sometimes. Next time, try to be a bit nicer in class.")
    elif ask2 == 'bullying':
        print("I'm really sorry that happened. If you want tips to cope with it, ask me anytime.")
    else:
        print("Thanks for sharing. Want to talk more about it?")

else:
    print("Thanks for letting me know how you feel.")