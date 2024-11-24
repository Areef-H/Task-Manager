#tasklist.py
import task
from datetime import datetime 

class Tasklist:
  """Attributes:
    tasklist: a list of Task objects"""

  def __init__(self):
    """Reads in the list of task from the file and stores them in a list. Append the list and sorts time"""
    self._tasklist = []
    with open("tasklist.txt", 'r') as file:
      todo = file.readlines()
      for name in todo:
        desc, date, time = name.strip().split(',')
        t = task.Task(desc, date, time)
        self._tasklist.append(t)
      self._tasklist.sort()

  def add_task(self, desc, date, time):
    """Contructs a new task using the parameters and appending it to the list"""
    # task =
    #self._tasklist.sort()
    self._tasklist.append(task.Task(desc, date, time))
    self._tasklist.sort()
    print(f"before sort = {self._tasklist}")
    
    print(f"after sort = {self._tasklist}")

  def mark_complete(self):
    """Removes the current task from the list"""
    del self._tasklist[0]

  def save_file(self):
    """Writes the contents of the tasklist back to the file"""
    with open("tasklist.txt", 'w') as file:
      for task in self._tasklist:
        file.write(repr(task) + '\n')
    
  def __getitem__(self, index):
    """Returns a Task from the list at a specified index"""
    return self._tasklist[index]

  def __len__(self):
    """Returns how many tasks there are in the list"""
    return len(self._tasklist)

  def get_current_task(self):
    """Returns the current task"""
    return self._tasklist[0]

  def __iter__(self):
    self._n = -1
    return self

  def __next__(self):
    self._n += 1
    if self._n >= len(self._tasklist):
        raise StopIteration
    return self._tasklist[self._n]