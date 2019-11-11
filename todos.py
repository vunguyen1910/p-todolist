import os  # sử lý thư mục
import sqlite3
from datetime import datetime
from termcolor import colored
from tabulate import tabulate
# tạo file database theo path hiện tại
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()
def create_todos():
    sql = """
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY,
            user_id INTEGER DEFAULT 0,
            body TEXT NOT NULL,
            due_date DATETIME,
            status TEXT DEFAULT "incomplete"
        )
    """
    # chạy sql
    cur.execute(sql)
    # update lại database
    conn.commit()
def create_users():
    sql = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT
        )
    """
    cur.execute(sql)
    conn.commit()
create_todos()
create_users()
def add():
    sql = """ 
        INSERT INTO todos
            (body, due_date)
        VALUES (?,?)
    """
    print('What are you want to add?')
    body = input()
    due_date = datetime.now()
    print(body, due_date)
    cur.execute(sql, (body, due_date))
    conn.commit()
def add_user_id():
    sql = """
        UPDATE todos
        SET user_id = ?
        WHERE id = ?
    """
    print("Which project you wanna add?")
    id_project = int(input())
    list_all_user()
    print("Which user you wanna add?")
    id_user = int(input())
    cur.execute(sql, (id_user, id_project))
    conn.commit()
def add_user():
    sql="""
        INSERT INTO users
            (name, email)
        VALUES(?,?)
    """
    print("What is your name?")
    name = input()
    print("What is your email?")
    email = input()
    cur.execute(sql, (name, email,))
    conn.commit()
def show_list():
    sql = """ 
        SELECT * FROM todos
    """
    cur.execute(sql)
    # lấy toàn bộ data từ cur và render ra
    result = cur.fetchall()
    print(tabulate(result, headers=["id","User_id","body", "due_date", "status"], tablefmt='orgtbl'))
def show_project_id():
    sql = """
        SELECT * FROM todos
        WHERE id = ?
    """
    print("Which project you wanna see?")
    id = input()
    cur.execute(sql, (id,))
    result = cur.fetchall()
    print(tabulate(result, headers=["project_id", "body", "due_date", "status"], tablefmt='orgtbl'))    
def show_date_reverser():
    sql = """ 
        SELECT * FROM todos
        ORDER BY due_date DESC;
    """
    cur.execute(sql)
    result = cur.fetchall()
    print(tabulate(result, headers=["project_id", "body", "due_date", "status"], tablefmt='orgtbl'))
def list_done():
    sql = """
        SELECT * FROM todos
        WHERE status = "completed"
    """
    cur.execute(sql)
    result = cur.fetchall()
    print(tabulate(result, headers=["project_id", "body", "due_date", "status"], tablefmt='orgtbl'))
def list_all_user():
    sql = """ 
        SELECT * FROM users
    """
    cur.execute(sql)
    # lấy toàn bộ data từ cur và render ra
    result = cur.fetchall()
    print(tabulate(result, headers=["user_id", "name", "email"], tablefmt='orgtbl'))
def mark():
    show_list()
    print("What project id you wanna change?")
    id = int(input())
    print("(1) complete or (2) incomplete?")
    status = int(input())
    if status == 1:
        sql = """
            UPDATE todos
            SET status = "completed"
            WHERE id = ?
        """
        cur.execute(sql, (id,))
        conn.commit()
    if status == 2:
        sql = """ 
            UPDATE todos
            SET status = "incomplete"
            WHERE id = ?
        """
        cur.execute(sql, (id,))
        conn.commit()
    show_list()
def staff():
    sql="""
        SELECT body, status, name
        FROM todos
        LEFT JOIN users
            ON todos.user_id = users.id
    """
    cur.execute(sql)
    result = cur.fetchall()
    print(tabulate(result, headers=["body", "status", "name"], tablefmt='orgtbl'))
def show_help_menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(colored('Todo List Options:', 'green'))
  print(colored('*' * 50, 'green'))
  print(colored('1. List all todos:', 'green'))
  print(colored('\t list', 'white'))
  print(colored('2. Add a new todo:', 'green'))
  print(colored('\t add', 'white'))
  print(colored('4. Mark a todo complete or incomplete:', 'green'))
  print(colored('\t mark', 'white'))
  print(colored('5. Show project by id:', 'green'))
  print(colored('\t show project only', 'white'))
  print(colored('6. Show project by time up to down:', 'green'))
  print(colored('\t show date reverser', 'white'))
  print(colored('7. Add user_id to project:', 'green'))
  print(colored('\t add user_id', 'white'))
  print(colored('-' * 100, 'green'))
  print(colored('Users List Options:', 'blue'))
  print(colored('*' * 50, 'blue'))
  print(colored('1. List all user:', 'blue'))
  print(colored('\t list users', 'white'))
  print(colored('2. add user:', 'blue'))
  print(colored('\t add user', 'white'))
  print(colored('3. shows each project, combined with each of the users working on that project:', 'blue'))
  print(colored('\t staff', 'white'))
if __name__ == '__main__':
    try:
        while True:
            print('What do you want to do?')
            choice = input()
            if choice == 'help':
                show_help_menu()
            elif choice == 'add':
                add()
            elif choice == 'add user_id':
                add_user_id()
            elif choice == 'list':
                show_list()
            elif choice == 'mark':
                mark()
            elif choice == 'list done':
                list_done()
            elif choice == 'show project only':
                show_project_id()
            elif choice == 'show date reverser':
                show_date_reverser()
            elif choice == 'list users':
                list_all_user()
            elif choice == 'add user':
                add_user()
            elif choice == 'staff':
                staff()
            elif choice == ''
            else: show_help_menu()
    except:
        show_help_menu()
