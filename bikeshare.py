import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def load_data(city, month='all', day='all'):
    """
    Cargar y filtrar los datos
    """
    df = pd.read_csv(CITY_DATA[city])
    
    """
    Convertir la columna 'Start Time' en objetos de fecha
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    """ 
    Extraer el mes de la columna 'Start Time'
    """
    df['Month'] = df['Start Time'].dt.month
    
    """
    Realizar filtrado según mes y día
    """
    if month != 'all':
        valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        df = df[df['Month'] == valid_months.index(month) + 1]

    if day != 'all':
        df = df[df['Start Time'].dt.day_name() == day.title()]

    return df

def get_earliest_year(df):
    earliest_year = df['Birth Year'].min()
    return earliest_year


def get_user_stats(df):
    
    earliest_year_value = earliest_year(df)
    print("Year of birth statistics:")
    print("Earliest year of birth:", get_earliest_year(df))
    print("Most recent year of birth:", most_recent_year(df))
    print("Most common year of birth:", most_common_year(df))
    
    if 'Gender' in df.columns:
        try:
            gender_counts = df['Gender'].value_counts(dropna=False)
            print("Counts of each gender:")
            print(gender_counts)
        except KeyError:
            print("Gender information not available.")

    if 'Birth Year' in df.columns:
        try:
            birth_year_stats = df['Birth Year'].describe()
            print("Birth Year statistics:")
            print(birth_year_stats)
        except KeyError:
            print("Birth Year information not available.")           
    else:
        print("Birth Year information not available.")

    


def display_raw_data(df):
    """
    Ask the user if they want to display the raw data and print 5 lines of raw data at a time if the answer is 'yes'
    Args:
        df: DataFrame. The dataset.
    """
    raw_data = 0
    while True:
        if raw_data == 0:
            answer = input("Hey, Do you want to see the raw data (5 lines)? Enter 'yes' or 'no': ").lower()
        else:
            answer = input("Hey, Do you want to see more raw data (5 lines)? Enter 'yes' or 'no': ").lower()
        if answer not in ['yes', 'no']:
            print("Your input is invalid. Please enter 'yes' or 'no'")
            continue
        if answer == 'yes':
            print(df.iloc[raw_data : raw_data + 5])
            raw_data += 5
        else:
            break

"""
Popular times travel
"""
def most_common_month(df):
    if df.empty:
        return "No data available"
    month_counts = df['Month'].value_counts()
    most_common_month = month_counts.idxmax()
    return most_common_month

def most_common_day(df):
    if df.empty:
        return "No data available"
    day_counts = df['Start Time'].dt.day_name().value_counts()
    most_common_day = day_counts.idxmax()
    return most_common_day

def most_common_hour(df):
    if df.empty:
        return "No data available"
    hour_counts = df['Start Time'].dt.hour.value_counts()
    most_common_hour = hour_counts.idxmax()
    return most_common_hour

"""
Popular stations and trip
"""
def most_common_start_station(df):
    if df.empty:
        return "No data available"
    start_station_counts = df['Start Station'].value_counts()
    most_common_start_station = start_station_counts.idxmax()
    return most_common_start_station

def most_common_end_station(df):
    if df.empty:
        return "No data available"
    end_station_counts = df['End Station'].value_counts()
    most_common_end_station = end_station_counts.idxmax()
    return most_common_end_station

def most_common_trip(df):
    if df.empty:
        return "No data available"
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    trip_counts = df['Trip'].value_counts()
    most_common_trip = trip_counts.idxmax()
    return most_common_trip


"""
Trip duration
"""
def total_travel_time(df):
    if df.empty:
        return "No data available"
    total_time = df['Trip Duration'].sum()
    return f"{round(total_time, 2)} seconds"

def average_travel_time(df):
    if df.empty:
        return "No data available"
    average_time = df['Trip Duration'].mean()
    return f"{round(average_time, 2)} seconds"

"""
User info
"""
def user_type_counts(df):
    if df.empty:
        return "No data available"
    user_type_counts = df['User Type'].value_counts()
    return user_type_counts

def gender_counts(df):
    if df.empty:
        return "No data available"
    try:
        gender_counts = df['Gender'].value_counts(dropna=False)
        return gender_counts
    except KeyError:
        print("Gender information not available.")
        return None



def birth_year_stats(df):
    if df.empty:
        return "No data available"
    try:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        return earliest_year, most_recent_year, most_common_year
    except KeyError:
        print("Birth Year information not available.")
        return "No data available", "No data available", "No data available"


def main():



                
    city = input("Please enter the name of the city (Chicago, New York City, Washington): ").lower()   
    while city not in CITY_DATA:
                city = input("Invalid city name. Please enter a valid city (Chicago, New York City, Washington): ").lower()

    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month = input("Please enter the name of the month (January, February, ..., December) or 'all' for no filter: ").lower()
    while month not in valid_months:
        month = input("Invalid month name. Please enter the name of the month (January, February, ..., December) or 'all' for no filter:  ").lower()

    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("Please enter the name of the day of the week (Monday, Tuesday, ..., Sunday) or 'all' for no filter: ").lower()
    while day not in valid_days:
        day = input("Invalid day. Please enter a valid day of the week or 'all' for no filter: ").lower()


            
    df = load_data(city, month, day)

            
    def get_user_stats(df):
        print("Please select the statistics you would like to view:")
        print("1. Popular times of travel")
        print("2. Popular stations and trips")
        print("3. Trip duration")
        print("4. User info")
        print("Enter the corresponding number(s) separated by commas (e.g., 1,3): ")
        

        while True:  
            selected_stats = input().strip().split(",")
            """ Se comprueba que cada entrada sea un dígito y esté en el rango correcto """
            if all(i.isdigit() and 1 <= int(i) <= 4 for i in selected_stats):
                break
            print("Invalid input. Please enter numbers from 1 to 4 separated by commas.")
  

        if '1' in selected_stats:
            monthx = most_common_month(df)
            print("Popular times of travel:")            
            print("Most common month:", monthx)
            dayx = most_common_day(df)
            print("Most common day of week:", dayx)
            hourx = most_common_hour(df)
            print("Most common hour of day:", hourx)
            print()

        if '2' in selected_stats:
            print("Popular stations and trips:")
            print("Most common start station:", most_common_start_station(df))
            print("Most common end station:", most_common_end_station(df))
            print("Most common trip:", most_common_trip(df))
            print()

        if '3' in selected_stats:
            print("Trip duration:")
            print("Total travel time:", total_travel_time(df))
            print("Average travel time:", average_travel_time(df))
            print()

        if '4' in selected_stats:
            print("User info:")
            print("Counts of each user type:")
            print(user_type_counts(df))
            print()

            gender_data = gender_counts(df)
            if gender_data is not None:
                print("Counts of each gender:")
                print(gender_data)
                print()

            print("Year of birth statistics:")
            earliest_year, most_recent_year, most_common_year = birth_year_stats(df)
            print("Earliest year of birth:", earliest_year)
            print("Most recent year of birth:", most_recent_year)
            print("Most common year of birth:", most_common_year)

            print()

    


    
  
    while True: 
        get_user_stats(df)
        stat_gal = input("Would you like to view another statistic? Enter yes or no: ").lower()
        while stat_gal not in ['yes', 'no']:
            stat_gal = input("Invalid input. Please enter 'yes' or 'no': ").lower()

        if stat_gal == 'no':
            break
            
        """ 
        Mostrar datos sin procesar si el usuario lo solicita
        """
    display_raw_data(df)
   



           
    repeat = input("Would you like to analyze another city? Enter yes or no: ").lower()
    while repeat not in ['yes', 'no']:
        repeat = input("Invalid input. Please enter 'yes' or 'no': ").lower()

    if repeat == 'yes':
        main()

main()