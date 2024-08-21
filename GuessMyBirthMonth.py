import time
indexMonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def ask_user(month):
    print(f"Were you born in {month}?")
    print("Type 'Y' for Yes and 'N' for No")
    return input("Your answer (Y/N): ").upper()


def before_after(month):
    print(f"Were you born BEFORE or AFTER {month}?")
    print("Type 'B' for BEFORE and 'A' for AFTER")
    return input('Your answer (B/A): ').upper()


def warning():
    time.sleep(2)
    print("You think you can fool me, bro? NO WAY!")
    time.sleep(1)
    print("You know what? I'm out bro! BYE!")


begin = 0
end = len(indexMonths) - 1
notFound = True
while notFound:
    mid = (begin + end) // 2
    guessMonth = months[indexMonths[mid]]
    userAnswer = ask_user(guessMonth)
    if userAnswer == 'Y':
        time.sleep(1)
        print(f'Your birthday month is in {guessMonth}!')
        time.sleep(1.5)
        print('Happy Birthday!')
        notFound = False
    elif userAnswer == 'N':
        print("Alright, I give up")
        time.sleep(5)
        print("Just kidding! HAHAHAHA")
        time.sleep(1)
        invalid = True
        while invalid:
            answer = before_after(guessMonth)
            if answer == 'B':
                if guessMonth == "January":
                    warning()
                    notFound = False
                end = mid - 1
                invalid = False
            elif answer == 'A':
                if guessMonth == "December":
                    warning()
                    notFound = False
                begin = mid + 1
                invalid = False
            else:
                print("DON'T MESS WITH ME! IMMA SUPER COMPUTER BRO!")
    else:
        time.sleep(1.5)
        print("Sorry. I don't understand that. Please repeat that again!")
