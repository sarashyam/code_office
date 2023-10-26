
 #  ------ This is a code that will remind you , but we have to give it in terminal and the output will be also in terminal

# import time
# print("What shall I remind you about?")
# text = str(input())
# print("In how many minutes?")
# local_time = float(input())
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)


#==================  to give a notifier when the time comes    ====================

# from win10toast import ToastNotifier
# import time

# toaster = ToastNotifier()

# print("What shall I remind you about?")
# text = str(input())

# print("In how many minutes?")
# local_time = float(input())
# local_time = local_time * 60

# time.sleep(local_time)

# toaster.show_toast("Reminder", text, duration=10)


#--------- it directs you to a particular link when time hits       ------------

# import datetime
# import time
# import webbrowser

# def remind():
#     # Open a web browser with a break time website or any other reminder
#     webbrowser.open("https://parade.com/1045449/marynliles/smile-quotes/")

# # Set the specific time for the break reminder (24-hour format)
# break_time = datetime.time(17, 57, 10)
# break_time1 = datetime.time(17, 57, 40)

# while True:
#     # Get the current time
#     current_time = datetime.datetime.now().time()

#     # Check if the current time matches the break time
#     if current_time.hour == break_time.hour and current_time.minute == break_time.minute and current_time.second == break_time.second:
#         remind()
#         break

#     # time.sleep(1)

#     if current_time.hour == break_time1.hour and current_time.minute == break_time1.minute and current_time.second == break_time1.second:
#         remind()
#         break
#     # Sleep for 1 second before checking the time again
#     time.sleep(1)

#------------ it displays random quotes  --------------------
import random
import time
from plyer import notification

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    # Add more quotes as needed
]

# Function to display a random quote notification
def display_quote():
    random_quote = random.choice(quotes)
    notification.notify(
        title="Motivational Quote",
        message=random_quote,
        app_icon=None,
        timeout=10
    )

# Set the specific time for the quote reminder (24-hour format)   #  when specific time hits
#quote_time = "09:23:00"

# while True:
#     # Get the current time
#     current_time = time.strftime("%H:%M:%S")

#     # Check if the current time matches the quote time
#     if current_time == quote_time:
#         display_quote()
#         break

#     # Sleep for 1 second before checking the time again
#     time.sleep(1)
interval_time = 30 * 60  # 30 minutes

while True: # reminds in every 30 minutes
    display_quote()
    time.sleep(interval_time)

