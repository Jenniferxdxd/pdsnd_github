import time
import pandas as pd
import numpy as np


#Here is the change
#Here is the refactoring change
# data source files start

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# end

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
    city = ""
    month = ""
    day = ""
    
    while True:
        
        city = input("Please input the city (chicago, new york city, washington): ").lower()
        
        if city == "chicago" or city == "new york city" or city == "washington":
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        
        month = input("Please input month:")
        
        if month == "january" or month=="february" or month=="march" or month=="april" or month=="may" or month=="june" or month=="all":
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
        day = input("Please input week:")
        
        if day == "monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday" or day=="saturday" or day=="sunday" or day=="all":
            break
    
    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print(day)
    ##display(df.to_string())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    common_month = df['month'].mode()[0]

    print('Most Common Month:', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('Most Common Day Of Week:', common_day_of_week)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most Common Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most Common End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station','End Station'])
    print('Most frequent combination of Start Station and End Station trip:\n', group_field.size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:\n', df['User Type'].value_counts(), sep="")
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:\n',df['Gender'].value_counts(), sep="")
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        print('Most Common Year:', df['Birth Year'].mode()[0])
        print('Most Recent Year:',df['Birth Year'].max())
        print('Earliest Year:', df['Birth Year'].min())
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def display_data(df):
    """Displays 5 rows of raw data."""
    
    while True:
        view_data= input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n").lower()
        answer=['yes','no']
        if view_data in answer:
            if view_data=='yes':
                start_loc=0
                end_loc=5
                display = df.iloc[start_loc:end_loc]
                print(display)
            break     
        
            
    if  view_data=='yes':       
            while True:
                view_data= input("Do you wish to continue? Enter yes or no: ").lower()
                if view_data in answer:
                    if view_data=='yes':
                        start_loc+=5
                        end_loc+=5
                        display = df.iloc[start_loc:end_loc]
                        print(display)
                    else:
                        break
                          


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
