"""
What is needed:
- File search (basic)
- File search by filetype
- Google something - done
- Calculations - done
- Quick to-do done
"""
import numexpr
import webbrowser
import urllib.parse
import json

def do_google_search(query):
    q = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={q}"
    webbrowser.open(url)


def calculate(expression):
    result = numexpr.evaluate(expression)
    print(f"= {result}")


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks():
     with open("tasks.json", "r") as f:
        return json.load(f)
     return []


def show_tasks():
    tasks = load_tasks()
    x = 1
    for task in tasks:
        print(f"{x}. {task}")
        x += 1

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks) 

def delete_task(number):
    tasks = load_tasks()
    tasks.pop(number-1)


def detect_command(data):
    x = []
    z = data
    z = z.split()
    for y in data:
        x.append(y)
    if x[0] == "?":
        x.reverse()
        x.pop()
        x.pop()
        x.reverse()
        x = "".join(x)
        do_google_search(x)
    if x[0] == "+":
         x.reverse()
         x.pop()
         x.pop()
         x.reverse()
         x = "".join(x)
         calculate(x)
    if z[0] == "todo":
        if z[1] == "add":
            z.pop()
            z.pop()
            z = " ".join(z)
            add_task(z)
            show_tasks()
        elif z[1] == "delete":
            z.pop()
            z.pop()
            delete_task(int(z[0]))
            show_tasks()
        elif z[1] == "show":
            show_tasks()
    

data = "todo add eat breakfast at 10"
detect_command(data)
