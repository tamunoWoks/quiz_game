def main():
    print('Welcome to my Soccer Quiz!')

    playing = input('Do you want to play? ').lower()

    if playing != 'yes':
        quit()
    print("Okay! Let's play :)")

    answer = input("What is the world's oldest football competition? ").lower()
    if answer == "fa Cup":
        print("Correct")
    else:
        print("Incorrect")

    answer = input("Which player is allowed to use hands? ").lower()
    if answer == "goalkeeper":
        print("Correct")
    else:
        print("Incorrect")
    
    answer = input("What is football's highest governing body? ").lower()
    if answer == "fifa":
        print("Correct")
    else:
        print("Incorrect")
    
    answer = input("How many minutes constitute a half? ").lower()
    if answer == ("45", "45mins", '45 minutes'):
        print("Co"45"rrect")
    else:
        print("Incorrect")

if __name__ == "__main__":
    main()