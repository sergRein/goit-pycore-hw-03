from datetime import datetime

def get_days_from_today(date):
    #use try\catch to proper get errors
    try:
        # parse date, get only date without time to get proper values of days
        given_date  = datetime.strptime(date, '%Y-%m-%d').date() 
        #count days between
        days_between = (datetime.today().date() - given_date).days 
        return days_between
    except ValueError: #when input string is not proper date
        print('Wrong date format')
        return None