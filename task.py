#task.py
class Task:
  """Attributes:
    description: string description of the task
    date: due date of the task
    time: time the task is due
  """

  def __init__(self, desc, date, time):
    """Sets values for description, time and date"""
    self._desc = desc
    self._date = date
    self._time = time

  @property
  def date(self):
    """Accesses the date property"""
    return self._date

  def __str__(self):
    """Returns the string representation of the task"""
    return (f"{self._desc}\n- Due: {self._date} at {self._time}")

  def __repr__(self):
    """Retuns a string representation of the passed object"""
    return (f"{self._desc},{self._date},{self._time}")

  def __lt__(self, other):
    """Compares the two tasks to see if self's date and time is less than to other's date and time"""
    month, day, year = self._date.strip().split('/')
    
    month2, day2, year2 = other._date.strip().split('/')

    if year < year2:
      return self._date > other._date

    if year == year2:
      if month < month2:
          return self._date > other._date

      if month > month2:
          return self._date < other._date

      if month == month2:
          if day < day2:
              return self._date > other._date

          if day > day2:
              return self._date < other._date

          if day == day2:
              if self._time > other._time:
                  return self._time < other._time

              elif self._time < other._time:
                  return self._time > other._time
