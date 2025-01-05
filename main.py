#There's a box that needs a key to open it 
#The key is somewhere in these other boxes 
#Look through each box till you find a key 
#Let's make it so its a game of random choice on which number the computer picks
import random



def recursion():
    #Hello there
    hiddenKey = computerKey()
    print("Welcome to the lost key game")
    print("There are 10 boxes, labeled 1-10. The key is in one of them")
    choice = input("Pick a number between 1 - 10: ")
    while hiddenKey != choice:
            print("Uh oh, you got it wrong.")
            choice = input("Pick a number between 1 - 10: ")

            if choice == hiddenKey:
                print("Wahoo! you guessed correctly")
    return ("Well done you won!")
    
    
def computerKey():
    guess = random.choice(["1", "10", "3", "4", "5", "6", "7", "8", "9", "10"])
    return(guess)
    
     
def main():
    recursion()
if __name__ == "__main__":
    main()