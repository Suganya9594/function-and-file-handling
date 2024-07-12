
#importing the modules
from datetime import datetime
import time

#getting current time
curr_date_time = datetime.now()
curr_time = time.strftime("%H-%M-%S")
# print(curr_time)


#function to create  new text file
def create_text_file():
    with open(curr_time + ".txt", "w") as f:
        f.write(curr_time)

#function to read the created text file
def read_text_file():
    with open(curr_time + ".txt", "r") as file:
        contents = file.read()
        print(contents)

create_text_file()
read_text_file()
