## print numbers from 1 to 100 (inclusive)
## if number is divisible by 3, print "Crackle"
## if number is divisible by 5, print "Pop"
## if number is divisible by 3 and 5, print "CracklePop"

def main():
    i = 1
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("CracklePop")
        if i % 3 == 0:
            print("Crackle")
        elif i % 5 == 0:
            print("Pop")
        else:
            print(i)

if __name__ == "__main__":
    main()