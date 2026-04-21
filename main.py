import os
import time
import random
from stock import get_stocks, calculate_date
from monthly import monthly
from situations import situation
from tutorial import tutorial
from gamestate import state

def check_bankrupt():
    if state.available_cash <= 0:
        print("You went bankrupt! You lose. Be more careful next time")
        raise SystemExit

def gameloop():
    for month in range(60):
        state.available_cash = round(state.available_cash, 2)
        print(f"--- Month {state.months_since_start + 1} ---")
        num_of_situations = random.randint(1, 2)
        for _ in range(num_of_situations):
            random_situation = random.randint(1, 14)
            situation(random_situation)
            time.sleep(.1)

        monthly()
        check_bankrupt()
        time.sleep(.1)
        state.update_cash()
        os.system('clear')

    win_screen()

def win_screen():
    print("You survived for 1 year!")
    print("You made it!")
    print("\nThis is what you ended with:")
    print(f"    Your house: {state.house}")
    print(f"    Your car: {state.car}")
    

    if state.pets:
        pets_str = ', '.join(state.pets)
        print(f"    You own: {pets_str}.")
    else:
        print("    You did not own any pets.")
    
    if state.stocks_owned:
        stocks_str = ', '.join([f"{qty} shares of {symbol}" for symbol, qty in state.stocks_owned.items()])
        print(f"    You own: {stocks_str}.")
    else:
        print("    You did not own any stocks.")
    
    print(f"\nYour final lifestyle points were: {state.points}.")
    if state.points > 200:
        print("You lived an incredible and lavish life! You were incredibly rich!")
    elif state.points > 100:
        print("You lived a great and comfortable life!")
    elif state.points > 50:
        print("You lived an above average life.")
    else:
        print("You lived a life full of frugality and savings. Great job for saving your money.")
    
    raise SystemExit

if __name__ == "__main__":
    tutorial()
    
    gameloop()
