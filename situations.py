import random
import os
from gamestate import state

def situation(random_num):
    # Event 1: Alleyway encounter
    if random_num == 1:
        print(f"Available Cash: ${state.available_cash:.2f}")
        while True:
            answer1 = input("You come across an alleyway, would you like to go down it? (yes/no): ").lower()
            if answer1 == "yes":
                thief_or_not = random.randint(0, 1)
                if thief_or_not == 0:
                    print("You run into a thief in the alley!")
                    loss = state.available_cash * 0.2
                    print(f"The thief takes ${loss:.2f} from you.")
                    state.available_cash *= 0.8
                    break
                elif thief_or_not == 1:
                    print("You spot a dumpster.")
                    while True:
                        answer1v1 = input("Would you like to check the dumpster? (yes/no): ").lower()
                        if answer1v1 == "yes":
                            print("You see a raccoon sleeping in the dumpster.")
                            print("Beside it is a bag. There seems to be something important inside.")
                            while True:
                                answer1v2 = input("Would you like to check the bag? (yes/no): ").lower()
                                if answer1v2 == "yes":
                                    raccoon_or_not = random.randint(0, 1)
                                    if raccoon_or_not == 0:
                                        print("You tried to check the bag and the raccoon woke up!")
                                        print("The raccoon attacked you and you ran away.")
                                        break
                                    elif raccoon_or_not == 1:
                                        print("You checked the bag and found $100 inside. You did not wake the raccoon.")
                                        print("You exited the alleyway.")
                                        state.available_cash += 100
                                        break
                                elif answer1v2 == "no":
                                    print("You left the bag alone and exited the alleyway.")
                                    break
                                else:
                                    print("Please enter either 'yes' or 'no'.")
                            break
                        elif answer1v1 == "no":
                            print("You left the dumpster alone and exited the alleyway.")
                            break
                        else:
                            print("Please enter either 'yes' or 'no'.")
                            continue
                    break
            elif answer1 == "no":
                break
            else:
                print("Please enter either 'yes' or 'no'.")
                continue
            break
        input("Press enter to continue...")
        os.system("clear")

    # Event 2: Car breakdown
    elif random_num == 2:
        mandys_price = random.randint(35, 200)
        tyrones_price = random.randint(220, 500)
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("You were driving on the highway when your car broke down.")
        print("These are the tow services you can call:")
        print(f"1. ${mandys_price} Handy Mandy's")
        print(f"2. ${tyrones_price} Tyrone's Towing")
        while True:
            print(f"Available Cash: ${state.available_cash:.2f}")
            tow_truck = input("Which tow service would you like to use? 1 or 2? ")
            if tow_truck == "1":
                if state.available_cash < mandys_price:
                    print("Not enough cash to use Handy Mandy's.")
                    break
                state.available_cash -= mandys_price
                print("You went with Handy Mandy's")
                break
            elif tow_truck == "2":
                if state.available_cash < tyrones_price:
                    print("Not enough cash to use Tyrone's Towing.")
                    break
                print("You went with Tyrone's Towing")
                state.available_cash -= tyrones_price
                state.points += 2
                break
            else:
                print("\nPlease enter a correct input. 1 or 2.\n")
                break
        input("Press enter to continue...")
        os.system("clear")

    # Event 3: Grocery shopping
    elif random_num == 3:
        random_food_price = random.uniform(0.6, 1.5)
        calvins_egg_price = round(7 * random_food_price, 2)
        carls_egg_price = round(9 * random_food_price, 2)
        franks_egg_price = round(10 * random_food_price, 2)
        pauls_egg_price = round(12 * random_food_price, 2)
        nates_milk_price = round(2.5 * random_food_price, 2)
        charlies_milk_price = round(3 * random_food_price, 2)
        gavins_milk_price = round(4 * random_food_price, 2)
        orlandos_milk_price = round(6 * random_food_price, 2)
        bens_meat_price = round(12 * random_food_price, 2)
        andrews_meat_price = round(15 * random_food_price, 2)
        nicks_meat_price = round(18 * random_food_price, 2)
        sherrys_drink_price = round(3 * random_food_price, 2)
        adams_drink_price = round(5 * random_food_price, 2)
        coles_drink_price = round(7 * random_food_price, 2)
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("You decided to buy some groceries.")
        input("Press enter to continue...")
        os.system("clear")
        while True:
            print(f"Available Cash: ${state.available_cash:.2f}")
            print("Items available to buy:")
            print("1. Eggs")
            print("2. Milk")
            print("3. Meat")
            print("4. Drinks")
            try:
                food_choice = int(input("Which item would you like to buy? (Enter 1, 2, 3, or 4): "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if food_choice == 1:
                print("\nYou chose to buy eggs.\n")
                print(f"Available Cash: ${state.available_cash:.2f}")
                print("Options:")
                print(f"1. ${calvins_egg_price} - Calvin's Cage Eggs")
                print(f"2. ${carls_egg_price} - Carl's Cage Free")
                print(f"3. ${franks_egg_price} - Frank's Free Range")
                print(f"4. ${pauls_egg_price} - Paul's Pasture Raised")
                try:
                    egg_choice = int(input("Which eggs would you like? (Enter 1-4): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                if egg_choice == 1:
                    if state.available_cash < calvins_egg_price:
                        print("Not enough cash for Calvin's Cage Eggs.")
                        continue
                    print("You chose Calvin's Cage Eggs.")
                    state.available_cash -= calvins_egg_price
                elif egg_choice == 2:
                    if state.available_cash < carls_egg_price:
                        print("Not enough cash for Carl's Cage Free.")
                        continue
                    print("You chose Carl's Cage Free.")
                    state.available_cash -= carls_egg_price
                    state.points += 0.5
                elif egg_choice == 3:
                    if state.available_cash < franks_egg_price:
                        print("Not enough cash for Frank's Free Range.")
                        continue
                    print("You chose Frank's Free Range.")
                    state.available_cash -= franks_egg_price
                    state.points += 1
                elif egg_choice == 4:
                    if state.available_cash < pauls_egg_price:
                        print("Not enough cash for Paul's Pasture Raised.")
                        continue
                    print("You chose Paul's Pasture Raised.")
                    state.available_cash -= pauls_egg_price
                    state.points += 2
                print(f"Your available cash is now ${state.available_cash:.2f}\n")
            elif food_choice == 2:
                print("\nYou chose to buy milk.\n")
                print(f"Available Cash: ${state.available_cash:.2f}")
                print("Options:")
                print(f"1. ${nates_milk_price} - Nate's Non-Organic")
                print(f"2. ${charlies_milk_price} - Charlie's Chocolate Milk")
                print(f"3. ${gavins_milk_price} - Gavin's Goat Milk")
                print(f"4. ${orlandos_milk_price} - Orlando's Organic Milk")
                try:
                    milk_choice = int(input("Which milk would you like? (Enter 1-4): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                if milk_choice == 1:
                    if state.available_cash < nates_milk_price:
                        print("Not enough cash for Nate's Non-Organic.")
                        continue
                    print("You chose Nate's Non-Organic.")
                    state.available_cash -= nates_milk_price
                elif milk_choice == 2:
                    if state.available_cash < charlies_milk_price:
                        print("Not enough cash for Charlie's Chocolate Milk.")
                        continue
                    print("You chose Charlie's Chocolate Milk.")
                    state.available_cash -= charlies_milk_price
                    state.points += 0.5
                elif milk_choice == 3:
                    if state.available_cash < gavins_milk_price:
                        print("Not enough cash for Gavin's Goat Milk.")
                        continue
                    print("You chose Gavin's Goat Milk.")
                    state.available_cash -= gavins_milk_price
                    state.points += 1
                elif milk_choice == 4:
                    if state.available_cash < orlandos_milk_price:
                        print("Not enough cash for Orlando's Organic Milk.")
                        continue
                    print("You chose Orlando's Organic Milk.")
                    state.available_cash -= orlandos_milk_price
                    state.points += 2
                print(f"Your available cash is now ${state.available_cash:.2f}\n")
            elif food_choice == 3:
                print("\nYou chose to buy meat.\n")
                print(f"Available Cash: ${state.available_cash:.2f}")
                print("Options:")
                print(f"1. ${bens_meat_price} - Ben's Chicken Breast")
                print(f"2. ${andrews_meat_price} - Andrew's Flank Steak")
                print(f"3. ${nicks_meat_price} - Nick's New York Strip")
                try:
                    meat_choice = int(input("Which meat would you like? (Enter 1-3): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                if meat_choice == 1:
                    if state.available_cash < bens_meat_price:
                        print("Not enough cash for Ben's Chicken Breast.")
                        continue
                    print("You chose Ben's Chicken Breast.")
                    state.available_cash -= bens_meat_price
                elif meat_choice == 2:
                    if state.available_cash < andrews_meat_price:
                        print("Not enough cash for Andrew's Flank Steak.")
                        continue
                    print("You chose Andrew's Flank Steak.")
                    state.available_cash -= andrews_meat_price
                    state.points += 1
                elif meat_choice == 3:
                    if state.available_cash < nicks_meat_price:
                        print("Not enough cash for Nick's New York Strip.")
                        continue
                    print("You chose Nick's New York Strip.")
                    state.available_cash -= nicks_meat_price
                    state.points += 2
                print(f"Your available cash is now ${state.available_cash:.2f}\n")
            elif food_choice == 4:
                print("\nYou chose to buy drinks.\n")
                print(f"Available Cash: ${state.available_cash:.2f}")
                print("Options:")
                print(f"1. ${sherrys_drink_price} - Sherry's Soda")
                print(f"2. ${adams_drink_price} - Adam's Apple Juice")
                print(f"3. ${coles_drink_price} - Cole's Coffee")
                try:
                    drink_choice = int(input("Which drink would you like? (Enter 1-3): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                if drink_choice == 1:
                    if state.available_cash < sherrys_drink_price:
                        print("Not enough cash for Sherry's Soda.")
                        continue
                    print("You chose Sherry's Soda.")
                    state.available_cash -= sherrys_drink_price
                elif drink_choice == 2:
                    if state.available_cash < adams_drink_price:
                        print("Not enough cash for Adam's Apple Juice.")
                        continue
                    print("You chose Adam's Apple Juice.")
                    state.available_cash -= adams_drink_price
                    state.points += 1
                elif drink_choice == 3:
                    if state.available_cash < coles_drink_price:
                        print("Not enough cash for Cole's Coffee.")
                        continue
                    print("You chose Cole's Coffee.")
                    state.available_cash -= coles_drink_price
                    state.points += 2
                print(f"Your available cash is now ${state.available_cash:.2f}\n")
            else:
                print("\n!!Please enter a correct input!!\n")
            more = input("Would you like to buy more food? (yes/no): ").lower()
            if more == "no":
                print("You left the grocery store.")
                break
        input("Press enter to continue...")
        os.system("clear")
    # Event 4: Boss call
    elif random_num == 4:
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("You left work and are about to drive home until your boss calls you. He wants you to come into his office.")
        while True:
            boss_question = input("Do you want to go in or leave? ").lower()
            print(f"Available Cash: ${state.available_cash:.2f}")
            if boss_question in ["go", "go in"]:
                if state.available_cash < 0: 
                    print("Not enough cash for bonus interaction.")
                    break
                print("He says you have been working hard and you receive a $5000 bonus!")
                state.available_cash += 5000
                input("Press enter to continue...")
                os.system("clear")
                break
            elif boss_question == "leave":
                print("You went home and never found out what your boss wanted to tell you.")
                input("Press enter to continue...")
                os.system("clear")
                break
            else:
                print("\n!!Please enter a correct input!!\n")
    # Event 5: Rent increase and housing decision
    elif random_num == 5:
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("Your landlord decided to raise rent.")
        increase = state.rent * 0.2
        print(f"He says it is going to be an extra ${increase:.2f} every month.")
        move_question = input("Do you want to stay in your current home or move? ").lower()
        if move_question == "stay":
            state.rent *= 1.2
            print(f"Rent is now ${state.rent:.2f}.")
            input("Press enter to continue...")
            os.system("clear")
        elif move_question in ["leave", "move"]:
            print("Housing options:")
            print("1: $30,000 200 sqft Camper van. (No rent)")
            print("2: $200,000 916 sqft apartment in NYC. ($1500/month rent)")
            print("3: $400,000 1500 sqft house in Houston. ($3800/month rent)")
            print("4: $1,500,000 3300 sqft house in Phoenix. ($6200/month rent)")
            print("5: $3,200,000 4600 sqft luxury home in Los Angeles. ($9800/month rent)")
            while True:
                house_question = input("Would you like to buy house 1, 2, 3, 4, or 5? (Enter 0 to cancel): ").strip()
                os.system("clear")
                if house_question == "1":
                    if state.available_cash < 30000:
                        print("Not enough cash to buy a Camper Van!")
                        continue
                    print("You bought a Camper Van!")
                    state.available_cash -= 30000
                    input("Press enter to continue...")
                    os.system("clear")
                    break
                elif house_question == "2":
                    rent_or_buy = input("Would you like to rent or buy? ").lower()
                    if rent_or_buy == "rent":
                        if state.available_cash < 1500:
                            print("Not enough cash to rent an apartment in NYC!")
                            continue
                        print("You rented an apartment in NYC!")
                        state.rent = 1500
                    elif rent_or_buy == "buy":
                        if state.available_cash < 200000:
                            print("Not enough cash to buy an apartment in NYC!")
                            continue
                        print("You bought an apartment in NYC!")
                        state.available_cash -= 200000
                    else:
                        print("Invalid option. Please choose rent or buy.")
                        continue
                    input("Press enter to continue...")
                    os.system("clear")
                    state.points += 10
                    break
                elif house_question == "3":
                    rent_or_buy = input("Would you like to rent or buy? ").lower()
                    if rent_or_buy == "rent":
                        if state.available_cash < 3800:
                            print("Not enough cash to rent a house in Houston!")
                            continue
                        print("You rented a house in Houston!")
                        state.rent = 3800
                    elif rent_or_buy == "buy":
                        if state.available_cash < 400000:
                            print("Not enough cash to buy a house in Houston!")
                            continue
                        print("You bought a house in Houston!")
                        state.available_cash -= 400000
                    else:
                        print("Invalid option. Please choose rent or buy.")
                        continue
                    input("Press enter to continue...")
                    os.system("clear")
                    state.points += 30
                    break
                elif house_question == "4":
                    rent_or_buy = input("Would you like to rent or buy? ").lower()
                    if rent_or_buy == "rent":
                        if state.available_cash < 6200:
                            print("Not enough cash to rent a house in Phoenix!")
                            continue
                        print("You rented a house in Phoenix!")
                        state.rent = 6200
                    elif rent_or_buy == "buy":
                        if state.available_cash < 1500000:
                            print("Not enough cash to buy a house in Phoenix!")
                            continue
                        print("You bought a house in Phoenix!")
                        state.available_cash -= 1500000
                    else:
                        print("Invalid option. Please choose rent or buy.")
                        continue
                    os.system("clear")
                    state.points += 50
                    break
                elif house_question == "5":
                    rent_or_buy = input("Would you like to rent or buy? ").lower()
                    if rent_or_buy == "rent":
                        if state.available_cash < 9800:
                            print("Not enough cash to rent a luxury home in Los Angeles!")
                            continue
                        print("You rented a luxury home in Los Angeles!")
                        state.rent = 9800
                    elif rent_or_buy == "buy":
                        if state.available_cash < 3200000:
                            print("Not enough cash to buy a luxury home in Los Angeles!")
                            continue
                        print("You bought a luxury home in Los Angeles!")
                        state.available_cash -= 3200000
                    else:
                        print("Invalid option. Please choose rent or buy.")
                        continue
                    input("Press enter to continue...")
                    state.points += 100
                    break
                elif house_question == "0":
                    state.rent *= 1.2
                    print(f"Rent is now ${state.rent:.2f}.")
                    input("Press enter to continue...")
                    os.system("clear")
                    break
                else:
                    print("\n!!Please enter a correct input!!")
        else:
            print("\n!!Please enter a correct input!!")
    # Event 6: Parking ticket
    elif random_num == 6:
        parking_fee = random.randint(25, 115)
        print(f"Available Cash: ${state.available_cash:.2f}")
        print(f"You got a parking ticket for ${parking_fee}.")
        if state.available_cash < parking_fee:
            print("Not enough cash to pay the parking ticket.")
        else:
            state.available_cash -= parking_fee
        input("Press enter to continue...")
        os.system("clear")
    # Event 7: Speeding ticket
    elif random_num == 7:
        speeding_fee = random.randint(80, 250)
        print(f"Available Cash: ${state.available_cash:.2f}")
        print(f"You got a speeding ticket for ${speeding_fee}.")
        if state.available_cash < speeding_fee:
            print("Not enough cash to pay the speeding ticket.")
        else:
            state.available_cash -= speeding_fee
        print(f"You now have ${state.available_cash}.")
        input("Press enter to continue...")
        os.system("clear")
    # Event 8: New job offer
    elif random_num == 8:
        random_salary = random.randint(int(state.salary * 0.9), int(state.salary * 1.3))
        print(f"Available Cash: ${state.available_cash:.2f}")
        print(f"You have just been offered a new job. It pays ${random_salary} per year.")
        print(f"Your current salary is {state.salary}.")
        job_question = input("Do you want to take it or leave it? ").lower()
        while True:
            if job_question in ["take", "take it"]:
                state.salary = random_salary
                state.monthly_salary = state.salary // 12
                print(f"You now make ${state.salary} per year.")
                break
            elif job_question in ["leave", "leave it"]:
                print("You keep your current job.")
                break
            else:
                print("\n!!Please enter a correct input!!")
        input("Press enter to continue...")
        os.system("clear")
    # Event 9: Birthday purchase
    elif random_num == 9:
        print(f"Available Cash: ${state.available_cash:.2f}")
        random_present = random.randint(1, 4)
        if random_present == 1:
            if state.available_cash < 900:
                print("Not enough cash to buy the iPhone.")
            else:
                print("It's your friend's birthday. He wanted the new iPhone, so you bought it for $900.")
                state.available_cash -= 900
                state.points += 2
        elif random_present == 2:
            if state.available_cash < 500:
                print("Not enough cash to buy the gaming console.")
            else:
                print("It's your friend's birthday. He wanted the new gaming console, so you bought it for $500.")
                state.available_cash -= 500
                state.points += 1
        elif random_present == 3:
            if state.available_cash < 600:
                print("Not enough cash to buy the TV.")
            else:
                print("It's your friend's birthday. He wanted a new TV, so you bought one for $600.")
                state.available_cash -= 600
                state.points += 1
        elif random_present == 4:
            if state.available_cash < 1400:
                print("Not enough cash to buy the laptop.")
            else:
                print("It's your friend's birthday. He wanted a new laptop, so you bought one for $1400.")
                state.available_cash -= 1400
                state.points += 2
        print(f"Your available cash is now ${state.available_cash}.")
        input("Press enter to continue...")
        os.system("clear")
    # Event 10: Lottery ticket
    elif random_num == 10:
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("You hear about a lottery ticket on the news. The jackpot is $1,000,000.")
        ticket_question = input("Do you want to buy an $8 ticket? (yes/no): ").lower()
        if ticket_question == "yes":
            if state.available_cash < 8:
                print("Not enough cash to buy the lottery ticket.")
            else:
                state.available_cash -= 8
                win_or_lose = random.randint(1, 5000)
                if win_or_lose == 1:
                    state.available_cash += 1000000
                    print("YOU WON THE JACKPOT!!!")
                else:
                    print("You didn't win.")
        elif ticket_question == "no":
            print("You decided to save your money.")
        else:
            print("\n!!Please enter a correct input!!")
        input("Press enter to continue...")
        os.system("clear")
    # Event 11: Dinner decision
    elif random_num == 11:
        print(f"Available Cash: ${state.available_cash:.2f}")
        out_dinner_cost = random.randint(40, 100)
        in_dinner_cost = random.randint(10, 20)
        print("You were thinking about going out for dinner.")
        while True:
            dinner_or_not = input("Would you like to go out for dinner? (yes/no): ").lower()
            if dinner_or_not == "yes":
                if state.available_cash < out_dinner_cost:
                    print("Not enough cash to go out for dinner.")
                    break
                print("You decided to go out for dinner.")
                state.available_cash -= out_dinner_cost
                print(f"It only costed you ${out_dinner_cost}\n")
                state.points += 1
                break
            elif dinner_or_not == "no":
                if state.available_cash < in_dinner_cost:
                    print("Not enough cash to stay in for dinner.")
                    break
                print("You decided to stay in for dinner.")
                state.available_cash -= in_dinner_cost
                print(f"It only costed you ${in_dinner_cost}\n")
                break
            else:
                print("Please enter either 'yes' or 'no'.")
                continue
        input("Press enter to continue...")
        os.system("clear")
    # Event 12: Vegas trip
    elif random_num == 12:
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("Your friend invites you to Las Vegas. He claims he knows how to win big.")
        vegas_or_no = input("Do you want to risk it? (yes/no): ").lower()
        if vegas_or_no == "yes":
            profit = random.randint(-1000, 5000)
            state.available_cash += profit
            state.points += 10
            if profit >= 0:
                print(f"You went to vegas and made ${profit}")
            elif profit < 0:
                print(f"You went to vegas and lost ${abs(profit)}")
            print(f"Your available cash is now {state.available_cash:.2f}")
        elif vegas_or_no == "no":
            print("You saved your money, but your friend called you lame.")
        else:
            print("\n!!Please enter a correct input!!")
        input("Press enter to continue...")
        os.system("clear")
    # Event 13: Promotion
    elif random_num == 13:
        print(f"Available Cash: ${state.available_cash:.2f}")
        bonus = state.salary * 0.3
        print(f"You get a promotion! Your boss offers you an extra ${bonus:.2f} per year.")
        state.salary *= 1.3
        state.monthly_salary = state.salary // 12
        print(f"You now make ${state.salary} per year.")
        input("Press enter to continue...")
        os.system("clear")
    # Event 14: Shopping for clothes
    elif random_num == 14:
        print(f"Available Cash: ${state.available_cash:.2f}")
        print("You are running out of clothes and have to go to the mall.")
        store_question = input("Do you want to save money and go to walmart or splurge and go to Gucci? ").lower()
        while True:
            if store_question in ["walmart", "go to walmart", "save"]:
                if state.available_cash < 65:
                    print("Not enough cash to shop at Walmart.")
                else:
                    print("You spent $65")
                    state.available_cash -= 65
                break
            elif store_question in ["gucci", "go to gucci", "splurge"]:
                if state.available_cash < 800:
                    print("Not enough cash to shop at Gucci.")
                else:
                    print("You splurged at Gucci and spent $800\nYour friends said you looked swagger")
                    state.available_cash -= 800
                    state.points += 2
                break
            else:
                print("Please enter a valid option (Walmart or Gucci).")
        input("Press enter to continue...")
        os.system("clear")

if __name__ == "__main__":
    random_num = 1
    situation(random_num)
