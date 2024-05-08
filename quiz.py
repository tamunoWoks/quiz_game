def main():
    print('Welcome to my Soccer Quiz!')

    playing = input('Do you want to play? ')

    if playing.lower() != 'yes':
        quit()
    print("Okay! Let's play :)")
    score = 0

    answer = input("What is the world's oldest football competition? ").lower()
    if answer == "fa cup":
        print("Correct")
        score +=1
    else:
        print("Incorrect")

    answer = input("Which player is allowed to use hands? ").lower()
    if answer == "goalkeeper":
        print("Correct")
        score +=1
    else:
        print("Incorrect")
    
    answer = input("What is football's highest governing body? ").lower()
    if answer == "fifa":
        print("Correct")
        score +=1
    else:
        print("Incorrect")
    
    answer = input("How many minutes constitute a half? ").lower()
    if "45" in answer:
        print("Correct")
        score +=1
    else:
        print("Incorrect")

    print(f"You got {score} correct")
    print(f"You scored {round((score/4) * 100)}%")

if __name__ == "__main__":
    main()