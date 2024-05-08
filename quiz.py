def main():
    print('Welcome to my Soccer Quiz!')

    playing = input('Do you want to play? ').lower()

    if playing != 'yes':
        quit()

    print("Okay! Let's play :)")

if __name__ == "__main__":
    main()