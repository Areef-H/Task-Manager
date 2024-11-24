from tasklist import Tasklist
from task import Task
import check_input

def main_menu():
  #prints out the menu
  print("1. Display current task")
  print("2. Display all tasks")
  print("3. Mark current task complete")
  print("4. Add new task")
  print("5. Search by Date")
  print("6. Save and quit")
  #prompts the user to enter a choice
  user_choice = check_input.get_int_range("Enter choice: ", 1, 6)
  return user_choice
  
def get_date():
  #prompts the user to enter a month, date and year
  print("Enter due date:")
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 3000)
  return f"{str(month).zfill(2)}/{str(day).zfill(2)}/{year}"

def get_time():
  #prompts the user to enter an hour and a minute
  print("Enter time:")
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)  
  return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"
  
def main():
  print("""
  
  ______           __                       
 /_  __/___ ______/ /__                     
  / / / __ `/ ___/ //_/                     
 / / / /_/ (__  ) ,<                        
/_/  \__,_/____/_/|_|                       
    __  ___                                 
   /  |/  /___ _____  ____ _____ ____  _____
  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                         /____/             

  
  """)
  tasklist = Tasklist()

  
  #loops the entire program
  while True:
    
    print("-Tasklist-")
    print(f"Tasks to complete: {len(tasklist)}")
    choice = main_menu()

    if choice == 1:
      #shows the current task 
      if len(tasklist) == 0:
        print("All tasks completed!")
      else:
        print(f"Current task is:\n{tasklist.get_current_task()}")

    elif choice == 2:
      #shows all of the task 
      if len(tasklist) == 0:
        print("All tasks completed!")
      else:
        for n, task in enumerate(tasklist):
          print(f"{n+1}. {task}")
          
    elif choice == 3:
      #deletes the current completed task
      if len(tasklist) == 0:
        print("No tasks left!")
      else:
        print(f"Marking current task as complete:\n{tasklist.get_current_task()}")
        tasklist.mark_complete()
        if len(tasklist) > 0:
            print(f"New current task is:\n{tasklist.get_current_task()}")
        else:
            print("No more tasks left!")

    elif choice == 4:
      #asks the user to input a new task
      desc = input("Enter a task: ")
      date = get_date()
      time = get_time()
      tasklist.add_task(desc, date, time)
      
    elif choice == 5:
      print("Enter date to search:")
      month = check_input.get_int_range("Enter month: ", 1, 12)
      day = check_input.get_int_range("Enter day: ", 1, 31)
      year = check_input.get_int_range("Enter year: ", 2000, 3000)
      print(f"Tasks due on: {month}/{day}/{year}:\n")

      task_count = iter(tasklist)
      counter = 1
      for task in task_count:
        if task._date == f"{month}/{day}/{year}":
          print(f"{counter}. {task}")
          counter += 1 

      
    elif choice == 6:
      #saves the file 
      tasklist.save_file()
      print("File has been saved!\nQuitting program...")
      break

main()