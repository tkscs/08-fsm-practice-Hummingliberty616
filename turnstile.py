# write code to implement a turnstile

current_state = "locked"

while True:
    if current_state == "locked":
        print("I am locked.")
    elif current_state == "unlocked":
        print("I am unlocked.")
    
    current_input = input("What do you want to do?")
    
    if current_state == "locked":
        if current_input == "coin":
            current_state = "unlocked"
        elif current_input == "push":
            current_state = "locked"
    elif current_state == "unlocked":
        if current_input == "coin":
            current_state = "unlocked"
        elif current_input == "push":
            current_state = "locked"