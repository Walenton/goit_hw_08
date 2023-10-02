from datetime import date, timedelta


def get_peiod(start_day, days = 7):
    result = {}
    for _ in range(days):
        result[start_day.day, start_day.month] = start_day.year
        start_day += timedelta(1)

    return result


def get_birthdays_per_week(users): 
    start_day = date.today()
    dict_of_births = {}   

    if len(users) == 0:
        return dict_of_births
    
    period = get_peiod(start_day)
    for i in users:      
        name = i['name'].split(' ')[0]
        day_of_birth = i['birthday'].day, i['birthday'].month

        if day_of_birth in period:
            birth = i['birthday'].replace(year=period.get(day_of_birth))            
            weekday = 'Monday' if birth.weekday() >= 5 else birth.strftime('%A')           
            
            if weekday not in dict_of_births:
                dict_of_births.update({weekday:[name]})
            else:
                dict_of_births[weekday].append(name)        

    return dict_of_births


if __name__ == '__main__':   
    users = [{"name": "Bill Gates", "birthday": date(1955, 10, 28)},
           {"name": "Antony Cheeper", "birthday": date(1955, 12, 12)},
           {"name": "Antony3112 Cheeper", "birthday": date(1955, 12, 31)},           
           {"name": "Jose Nolan", "birthday": date(1975, 11, 19)},
           {"name": "John Past", "birthday": date(1975, 1, 2)},  
           {"name": "John1-1 Past", "birthday": date(1975, 1, 1)},                       
           {"name": "Jose today Nickname", "birthday": date(1975, 9, 30)},
           {"name": "Jose Also Today", "birthday": date(1975, 9, 30)},
           {"name": "JoseSun Sunday", "birthday": date(1975, 10, 1)},
           {"name": "JoseMon Monday", "birthday": date(1975, 10, 2)},
           {"name": "NotBillTue Gates", "birthday": date(1955, 10, 3)},             
           {"name": "NextWed Week", "birthday": date(1975, 10, 4)},
           {"name": "NextThu Week", "birthday": date(1975, 10, 5)},                                                                                          
           {"name": "JoseFri Futureweek", "birthday": date(1975, 10, 6)}]

    
    print (get_birthdays_per_week(users))


    