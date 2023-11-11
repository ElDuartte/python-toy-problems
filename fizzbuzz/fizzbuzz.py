# for some reason python needs to import a module to use user input
import sys

userNumber = int(sys.argv[1])

def fizzbuzz(userNumber):
    print("Your number is:", userNumber)

    for i in range(userNumber):
        i += 1
        # if the division residue is 0
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", i)
        elif i % 3 == 0:
            print("Fizz", i)
        else:
            print("Buzz", i)


fizzbuzz(userNumber)
