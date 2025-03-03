import hou
import random as r
import getpass
from datetime import datetime

time_now= datetime.now()
current_time= time_now.strftime("%H:%M:%S")

user = getpass.getuser().capitalize()

def choose_time_of_day(current_time):
    hour = int(current_time[0:2])
    if hour > 5 and hour <12:
        return "morning"
    elif hour >=12 and hour < 18:
        return "afternoon"
    elif hour >=18 and hour < 23:
        return "evening"
    else:
        return "night"
    
time_of_day = choose_time_of_day(current_time)


# print(f"hello it's {time_of_day}")

messages = [
    f"Good {time_of_day}, {user}! It's {current_time}. I hope you have a wonderful and productive {time_of_day} ahead.",
    f"{time_of_day.capitalize()}, {user}! It's {current_time}. Wishing you a {time_of_day} filled with joy and success.",
    f"Good {time_of_day}, {user}! It's {current_time}. May your {time_of_day} be as bright and cheerful as your smile.",
    f"Hello, good {time_of_day}, {user}! It's {current_time}. I trust you had a restful night and are ready to conquer the {time_of_day}.",
    f"Hi, good {time_of_day}, {user}! It's {current_time}. May your {time_of_day} be filled with positive energy and great achievements.",
    f"Good {time_of_day} to you, {user}! It's {current_time}. I hope your {time_of_day} is off to a fantastic start.",
    f"Wishing you a good {time_of_day}, {user}! It's {current_time}. May your {time_of_day} be filled with happiness and prosperity.",
    f"Have a great {time_of_day}, {user}! It's {current_time}. May you find joy and satisfaction in all your endeavors today.",
    f"A very good {time_of_day} to you, {user}! It's {current_time}. I hope your {time_of_day} is as wonderful as you are.",
    f"Good {time_of_day}, sunshine, {user}! It's {current_time}. May your {time_of_day} be as bright and beautiful as the morning sun."
]

message = r.choice(messages)


hou.ui.displayMessage(message, buttons=('Thanks',),title=("Morning greeting!"))
