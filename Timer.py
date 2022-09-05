# Setting up the timer. Calculating the remaining time

import time, datetime
from playsound import playsound


# Setting up the work state
work = True
rest = False


# Creating a function that acts as countdown
def pomodoroCountdown(m,s):

    # Opening my log system
    file = open("/home/mohamed/Documents/Adonis Programming/PomodoroTimerProgram/WorkLog.txt", 'a')

    # Getting the current task
    task = input("Enter the task you're gonna work on during this pomodoro : ")
    seconds = time.time()
    local_time = time.ctime(seconds)
    file.write(str(task) + " | Started at " + local_time + " \r")
    file.close()

    #Calculating the number of seconds given
    total_seconds = m * 60 + s

    #While loop checks if the countdown reached zero
    while total_seconds > 0 :

        #Remaining seconds
        # It gives you the differences between the moment you started the program and the final countdown and It changes iT to the form of hours
        timer = datetime.timedelta(seconds= total_seconds)

        # Print the time left
        print(timer, end="\r")

        # Delaying the program by 1 seconds
        time.sleep(1)

        # Reduce 1 second
        total_seconds -= 1
    
    
# Work State
def workState(work_state,rest_state):
   
    if(work_state == True):
        playsound('/home/mohamed/Documents/Adonis Programming/PomodoroTimerProgram/Work.wav')
        print("Start Working")
        pomodoroCountdown(50, 0)
        work_state = False
        rest_state = True

    if(rest_state == True):
        playsound('/home/mohamed/Documents/Adonis Programming/PomodoroTimerProgram/home/mohamed/Documents/Adonis Programming/PomodoroTimerProgram/Rest.wav')
        print("You can rest now")
        pomodoroCountdown(10, 0)
        work_state = True
        rest_state = False


while(True):
    workState(work, rest)

