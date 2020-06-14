import time

import pandas as pd

import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',

'new york city': 'new_york_city.csv',

'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:

    (str) city - name of the city to analyze

    (str) month - name of the month to filter by, or "all" to apply no month filter

    (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    print('Hello! Let\'s explore some US bikeshare data!')

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    '''This while loop asks for user input regarding city location.'''

    while True:

        city = input("What city would you like data for? (Chicago, New York City, Washington)\n--> ").lower()

        if city not in cities:

            print('Please choose one of the following cities: Chicago, New York City, or Washington.')

            continue

        else:

            break

# TO DO: get user input for month (all, january, february, ... , june)

# '''This while loop asks for user input regarding a particular month of data.'''

    while True:

        month_u = input("Type a month for a specifc time frame of data. For all months type 'all'\n--> ").lower()

        if month_u not in months:

                print("***Please choose months between January and June***")

        else:

            break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:

        day_u = input("Type a day of the week for a specific time frame of data. For all days of the week type 'all'\n-->").lower()

        if day_u not in days:

            print("Please type a day of the week. If you want all days, type 'all'.")

            continue
        else:
            break

            print('-'*40)

            return city, month_u, day_u

def load_data(city, month_u, day_u):

    """

    Loads data for the specified city and filters by month and day if applicable.

    Args:

    (str) city - name of the city to analyze

    (str) month - name of the month to filter by, or "all" to apply no month filter

    (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:

    df - Pandas DataFrame containing city data filtered by month and day

    """

    df = pd.read_csv(CITY_DATA[city])

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel by using the 'Start Time' column of selected city."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    df['Start Time']= pd.to_datetime(df['Start Time'])

        # TO DO: display the most common month

    df['month']= df['Start Time'].dt.month

    month_comm = df['month'].mode()[0]

    print("The most usage occurs during the month of {}.\n".format(month_comm))

        # TO DO: display the most common day of week

    df['day']= df['Start Time'].dt.weekday_name

    day_comm = df['day'].mode()[0]

    print("The most common day of travel is {}.\n".format(day_comm))

    return

# TO DO: display the most common start hour

    df['hour']= df['Start Time'].dt.hour

    hour_comm = df['hour'].mode()[0]

    return print("The most common hour of travel is at {}.\n".format(hour_comm))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # TO DO: display most commonly used start station

    # TO DO: display most commonly used end station

    start_comm = df['Start Station'].size().mode()

    end_comm = df['End Station'].size().nlargest(1)

    print("The most commonly used starting and ending stations are {} and {}.\n".format(start_comm, end_comm))

    # TO DO: display most frequent combination of start station and end station trip

    se_combo = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    print("The most frequent start station to end station combination is {}.\n".format(se_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # TO DO: display total travel time

    # TO DO: display mean travel time

    total = df['Trip Duration'].sum()

    avg = df['Trip Duration'].mean()

    print("The total travel time is {}.\nThe average travel time is {}.\n".format(total,avg))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types

    if 'User Type' in df.columns:

        user_types = df['User Type'].value_counts()

        print("Here are the counts of user types: {}\n".format(user_types))

    # TO DO: Display counts of gender

    try:

        gender = df['Gender'].value_counts()

        print("Here are the counts for gender types: {}\n".format(gender))

    except:

        print("Sorry. No data available!")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:

        earliest = min(df['Birth Year'])

        most_recent = max(df['Birth Year'])

        most_common = df['Birth Year'].mode()

        print("The earliest year of birth is {}, while the most recent year of birth is {}.\n".format(earliest,most_recent))

        print("The most common year of birth shared between users is {}.\n".format(most_common))

    except:

        print("Sorry. No data available!")

        print("\nThis took %s seconds." % (time.time() - start_time))

        print('-'*40)

def main():

    while True:

        city, month_u, day_u = get_filters()

        df = load_data(city, month_u, day_u)

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        user_input = input('\nWhat would you like to do next?\nPlease enter yes or no\n').lower()
        if user_input in ('yes', 'y'):
            i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
        more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
        if more_data not in ('yes', 'y'):
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break

        if __name__ == "__main__":

            main()
