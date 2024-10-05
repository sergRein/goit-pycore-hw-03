from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    #get today
    today = datetime.today().date()
    #init empty list
    congratulation_list = []
    for user in users:
        #get user birthday from list
        user_birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        
        #set date in current year
        user_birthday = user_birthday.replace(year = today.year)  

        #if user birthday in past - lets add one more year to make all birhtdays in the future relative to today 
        if today > user_birthday:
            user_birthday = user_birthday.replace(year = today.year + 1)

        #get days to birthday
        days_to_user_birthdate = (user_birthday - today).days

        #check if in next 7 days
        if days_to_user_birthdate >=0 and days_to_user_birthdate <=7:
            #set congratulation date
            congratulate_date = today + timedelta(days = days_to_user_birthdate)

            #check if its saturday or sunday, if so lets set monday
            if congratulate_date.weekday() in [5, 6]:
                congratulate_date += timedelta(days = (7-congratulate_date.weekday()))
            
            #append to our list
            congratulation_list.append({'name': user['name'], 'congratulation_date': congratulate_date.strftime('%Y.%m.%d')})


    return congratulation_list


users = [
    {"name": "John Doe", "birthday": "1985.12.30"},
    {"name": "Jane Smith", "birthday": "1990.01.03"}
]

print(f"{get_upcoming_birthdays(users)}")