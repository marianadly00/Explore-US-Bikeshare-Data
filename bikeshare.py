#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
import calendar


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list=["chicago","new york","washington"]
month_list=["all","january","february","march","april","may","june"]
day_list = ["all","monday", "tuesday", "wednesday", 
        "thursday", "friday", "saturday", "sunday"] 


# In[3]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (Chicago, New york, washington). HINT: Use a while loop to handle invalid inputs
    
    
    while True:
        
            city=input("Please enter the City name that you ask for Chicago,New york or Washington\n").lower()
            if city not in city_list:
                print("The City:{} is not in the list. Try again ".format(city))
                continue
            else:
                break
               
    while True:
        
            month=input("Please enter the month from range (all, january, february, ... , june): ").lower()
            if month not in month_list:
                print("{} is not in the list. Try again".format(month))
                continue
            else:
                break
                
    while True:
        
            day=input("Enter the Weekday: ").lower()
            if day not in day_list:
                print("The day is :{} not in the list. Try again".format(day))
                continue
            else:
                break
    print("Thanks you, Data will be loaded soon")                     
    print('-'*40)            
    return city,month,day       
    
                      
                      
         


# In[4]:


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
    #convert the stsrt time to datetime
    df=pd.read_csv(CITY_DATA[city])
    #convert the stsrt time to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract month and week day
    df['Month']=df['Start Time'].dt.month
    df['Week Day']=df['Start Time'].dt.day_name()
    df['Hour'] =df['Start Time'].dt.hour
    
    if month!='all': 
         # filter by month to create the new dataframe
        df = df[df['Month'] == month_list.index(month)]
    if day!='all':
        # filter by day of week to create the new dataframe
        df = df[df['Week Day'] == day.title()]
    
    return df



# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_moth=df['Month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day=df['Week Day'].mode()[0]

    # TO DO: display the most common start hour
    most_common_hour=df['Hour'].mode()[0]
    print("The most common month is: {}\nThe most common week day is: {}\nThe most start hour is: {}:00"
          .format(calendar.month_name[most_common_moth],most_common_day,most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
   
    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_common_conbination=  df[['Start Station', 'End Station']].mode().loc[0]
    
    print("The most popular start staion is: {}\nThe most popular end station is: {}\nThe most frequent combination of start station , end station trip is: {} and {}"
          .format(common_start_station,common_end_station,most_common_conbination[0],most_common_conbination[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
   


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()/60
    print("Total time is {} minutes".format(round(total_time,1)))

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print("The average time is {} minutes".format(round(mean_time/60,2)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 


# In[8]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usrs=df['User Type'].value_counts()
    print("The counts of user type are: \n",count_usrs.to_string(header=None))
    # TO DO: Display counts of gender
    
    try:
        count_gender=df['Gender'].value_counts()
        print("The counts of gender are: \n",count_gender.to_string(header=None))
    except :
        
        print("No informartion for gender in this city\n")
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        early_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        common_birth=df['Birth Year'].mode()[0]
        print("The most earliest year is: {}\nThe most recent year is: {}\nThe most common year is: {}".
              format(int(early_birth),int(recent_birth),int(common_birth)))
    except:
        print("No inforartion for birth year in this city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  


# In[14]:


def disply_row_data(df):
    i=0
    while True:
        ans=input("Do you want see {}:{} rows? Please enter Yes or No: ".format(i+1,i+5))
        if ans!='yes':
            break
        else:
            print(df[i:i+5].to_string(index=False))
            
            i+=5
            
    
        


# In[15]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disply_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




