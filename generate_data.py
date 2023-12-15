
import csv 
from random import randint, randrange
from datetime import timedelta
from datetime import datetime
import random

input_file_path_bought = 'bought.txt'
input_file_path_clicked = 'clicked.txt'
d1 = datetime.strptime('1/12/2023 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('12/12/2023 4:50 AM', '%m/%d/%Y %I:%M %p')


def random_date(start, end): #source: https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def overwrite_rows(input_file_path=input_file_path_clicked): # there is the bug that both of the datasets shoud have same number of rows
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i in range(99999, min(199999, len(lines))):
        lines[i] = "@gmail.com\n"

    with open(input_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def read_emails(input):
    with open(input, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def create_clicked(file_name):
    with open(file_name, 'w', newline = '') as file:
        writer = csv.writer(file)
        emails = read_emails(input_file_path_clicked)
     #   fields = ['email','date_time','addID','time_looking']
     #   writer.writerow(fields)
        for email in emails:
            date = random_date(d1,d2)
            addID = random.randint(1,42)
            time_looking = random.uniform(0.05, 11)
            writer.writerow([email,date,addID,time_looking])

def create_bought(file_name):
    with open(file_name, 'w', newline = '') as file:
        writer = csv.writer(file)
        emails = read_emails(input_file_path_bought)
      #  fields = ['email','date_time','Price','NumberOfProducts']
      #  writer.writerow(fields)
        for email in emails:
            date = random_date(d1,d2)
            price = random.randint(42,199) +random.random()
            NumberOfProducts = randint(1,8)
            writer.writerow([email,date,price,NumberOfProducts])


input_file_path_bought_csv = 'bought.csv'
input_file_path_clicked_csv = 'clicked.csv'
create_clicked(input_file_path_clicked_csv)
create_bought(input_file_path_bought_csv)
#overwrite_rows()
