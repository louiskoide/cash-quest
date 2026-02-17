import time
import os
from gamestate import state

def tutorial():
    
    print("Welcome to Cash Quest")
    print("A fun way to learn how to invest stocks and budget your money")
    print("There will be many scenarios where you can choose to spend your money")
    print("Make it to the end of the month to recieve your pay and make big purchases")
    print("The goal of the game is to learn to use your money effectively and live the best lifestyle possible")
    print("Make sure you don't lose all your money!\n")
    
    print("These are your starting stats:")
    print(f"Your salary is ${state.salary}")
    print(f"Your rent is ${state.rent}")
    print(f"Your available cash is ${state.available_cash}")
    print(f"Your monthy expenses is ${state.monthly_expenses}")
    
    input("\nPress enter to begin the game ")
    os.system('clear')
    
    for i in range(1, 4):
        #Gives the user a tip on how to input their answers into the budgeting software
        print(f"\nLoading Budget Software{'.'*i}")
        time.sleep(.6) #Stalls outputs for half a second
        os.system('clear')
