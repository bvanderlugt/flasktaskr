# project/db_create.py


from views import db
from models import Task
from datetime import date

db.create_all()

db.session.add(Task("Finish this tutorial", date(2015, 2, 13), 10, 1))
db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10, 1))

db.session.commit()

# with sqlite3.connect(DATABASE_PATH) as connection:

#     # get a cursor object used to execute SQL commands
#     c = connection.cursor()

#     # create the table
#     c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
#         status INTEGER NOT NULL)""")

#     # insert dummy data into the table
#     c.execute(
#         'INSERT INTO tasks (name, due_date, priority, status)'
#         'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
#     )
#     c.execute(
#         'INSERT INTO tasks (name, due_date, priority, status)'
#         'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
#     )
