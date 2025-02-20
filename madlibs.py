while(True):
    print("Welcome to the Mad Libs game! Fill in the blanks to create a fun story.\n")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    story = f"One day, a {adjective} {noun} went to {place}. It decided to {verb} all day long. Everyone around was amazed!"
    print("\nHere’s your final story :\n")
    print(story)
    again=input("Do you want to play again? Yes/No?").lower()
    if(again!='yes'):
        print("Thanks for playing...!!!")
        break
