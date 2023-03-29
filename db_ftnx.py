import sqlite3

conn = sqlite3.connect('my_database.db',check_same_thread=False)

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task TEXT,task_status TEXT,task_due_data DATE)')

def add_task(task,task_status,task_due_data):
    c.execute('INSERT INTO tasktable (task,task_status,task_due_data) VALUES (?,?,?)',(task,task_status,task_due_data))
    conn.commit()

def view_data():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data

def view_unique_task():
    c.execute("SELECT DISTINCT task FROM tasktable")
    data = c.fetchall()
    return data

def get_complete_task(task):
    c.execute('SELECT * FROM tasktable WHERE task="{}"'.format(task))
    data = c.fetchall()
    return data

def update_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_data):
    c.execute('UPDATE tasktable SET task = ?,task_status = ?,task_due_data = ? WHERE task = ? AND task_status = ? AND task_due_data = ?',
              (new_task,new_task_status,new_task_due_date,task,task_status,task_due_data))
    conn.commit()
    data = c.fetchall()
    return data

def delete_task(task):
    c.execute('DELETE FROM tasktable WHERE task = "{}"'.format(task))
    conn.commit()