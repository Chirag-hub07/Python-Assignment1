# Name= Chirag Virdi
# Roll no= 2501420017
# Class= Btech CSE DS (Sem 1)
# Date= 4/10/2025
# Project Title= Calorie Tracking Console App

print('                                     Calorie Tracking Console App')
print('                                                              -Because your calories deserve a checkpoint!')
print(''' 
                                                  ⢱⣆⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
                                                ⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
                                            ⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
                                            ⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
                                            ⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
                                            ⢰⢀⣾⣿⣿⠟⡀⠀⣾⢿⣿⣿⣿⣿
                                            ⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
                                            ⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
                                            ⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
                                            ⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀''')
print('''                 
                                =========================================
                                 Welcome to Calorie Tracking Console App 
                                =========================================

                                Hi! Let's turn your meals into insights.

                                - Log every bite from morning till night.
                                - Compare with your daily calorie goal.
                                - Stay on track and crush your health targets.

                                Your path to smarter eating starts now!
                                =========================================
''')

meal_name=[]
calories=[]
meals=int(input('Please enter the number of meals you want to track: '))
print('\n')
for i in range(meals):
    meal=input(f'Enter meal {i+1} name: ')
    cal=int(input(f'Enter calories intake for {meal}: '))
    meal_name.append(meal)
    calories.append(cal)

total_cal=sum(calories)
avg_cal= sum(calories)/len(calories)

cal_limit=int(input('Enter your Daily Calorie Limit: '))
print('\n')

if cal_limit<total_cal:
    print('''Warning: You've exceeded your daily calorie limit!
Time to make your next meals lighter and smarter.''')
elif cal_limit>total_cal:
    print('''Great balance! Your calories are in range.  
Keep fueling your body the smart way.''')
else:
    print('''Bullseye! You've matched your daily goal.  
Keep up this perfect balance.''')

print('\n' + '='*30)
print("      CALORIE SUMMARY")
print('='*30)
print(f'{"Meal Name":<20}{"Calories"}')
print('-'*30)

for i in range(meals):
    print(f'{meal_name[i]:<20}{calories[i]:>5} kcal')

print('-'*30)
print(f'{"Total:":<20}{total_cal:>5} kcal')
print(f'{"Average:":<20}{avg_cal:>5.2f} kcal')
print('='*30 + '\n')

from datetime import datetime

report=input('Do you want to save this summary?: ')

if report=='yes' or report=='Yes':
    now = datetime.now()
    timestamp = now.strftime("%B %d, %Y - %I:%M:%S %p")
    
    with open('calorie_log.txt', 'w') as file:
        file.write(f"====== REPORT SAVED ON: {timestamp} ======\n")
        file.write('\n' + '='*30)
        file.write('\n')
        file.write("      CALORIE SUMMARY\n")
        file.write('='*30)
        file.write('\n')
        file.write(f'{"Meal Name":<20}{"Calories"}\n')
        file.write('-'*30 + '\n')

        for i in range(meals):
            file.write(f'{meal_name[i]:<20}{calories[i]:>5} kcal\n')

        file.write('-'*30 + '\n')
        file.write(f'{"Total:":<20}{total_cal:>5} kcal\n')
        file.write(f'{"Average:":<20}{avg_cal:>5.2f} kcal\n')
        file.write(f'{"Your Limit:":<20}{cal_limit:>5} kcal\n')
        file.write('='*30 + '\n')
        
        if cal_limit<total_cal:
            file.write('''Warning: You've exceeded your daily calorie limit!
Time to make your next meals lighter and smarter.\n''')
        elif cal_limit>total_cal:
            file.write('''Great balance! Your calories are in range.  
Keep fueling your body the smart way.\n''')
        else:
            file.write('''Bullseye! You've matched your daily goal.
Keep up this perfect balance.\n''')

        file.write('\n\n')

    print("\nDone! Your daily summary is saved for the journey ahead!")
else:
    print("\nOkay! Summary not saved this time. Stay on track!")