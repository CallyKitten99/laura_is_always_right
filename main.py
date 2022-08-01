# Loop forever, requesting name
while True:
    # Acquire name from user.
    # Make name uppercase (for case-insensitive comparison).
    # Split names, to separate first name from middle and surnames
    name = input("What is your name?\n").upper().split()
    # We want at least one name.
    # When we have at least one name, we satisfy our request and break the loop
    if len(name) > 0: break

# We discard middle and surnames
name = name[0]

# We check that the user is called 'Laura', who is always right.
# Print this accordingly
if name == "LAURA": print("Laura is always right")
else:
    # Reconstruct name from uppercase form. This simply means putting all but
    # the first letter into lowercase.
    # Slicing is used here to separate the first letter from the remaining
    # letters of the name.
    # name = first_letter_in_uppercase + rest_of_name_in_lowercase
    name = name[0] + name[1:].lower()
    
    # Greet and challenge
    print("Hello " + name + "! Answer the following equation correctly:")
    
    # Loop forever, requesting well-formed answer to equation
    while True:
        # We expect only a single answer. (Lazy whitespace delimiter doesn't
        # account for punctuation).
        answer = input("2 + 2 = ").split()
        
        # We expect only one single answer
        if len(answer) != 1:
            print("Please provide only one numeric answer.")
            continue
        
        # Attempt to parse (convert) string to workable number.
        # The int() operator (which does the parsing) will throw a ValueError
        # exception if we attempt to convert a non-number string to a number,
        # for example int("Laura"), because "Laura" is not a number.
        try: answer = int(answer[0])
        
        # Attempt may fail, so we catch the EXCEPTion and respond accordingly
        except ValueError as e: print("Please provide a numeric answer.")
        
        # All going well, we have satisfied our request and can break the loop
        else: break
    # End of while loop
    
    # And this sorcery will totally prohibit a non-Laura being correct.
    if answer == 4: print("Incorrect. 2 + 2 is 22.")
    else: print("Incorrect. 2 + 2 = 4.")
