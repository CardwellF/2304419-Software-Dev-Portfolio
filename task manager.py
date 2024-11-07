#task manager
'''
overview
1. login system
2. task adding
3. task editing
4. task delete
5. saving
6. view tasks
'''
#imports
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime
from functools import partial

#contructor class for tasks
class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date

#main class
class TaskManagerApp:
    #class initialisation
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []
        self.tnv = tk.StringVar()
        self.pv = tk.StringVar()
        self.ddv = tk.StringVar()
        self.tdv = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Task Name Label and Entry
        tk.Label(self.root, text="Task Name:").grid(row=0, column=0, sticky="w")
        tne = tk.Entry(self.root, textvariable=self.tnv)
        tne.grid(row=0, column=1, padx=10, pady=5)

        #description
        tk.Label(self.root, text="task description").grid(row=1, column=0, sticky="w")
        tde = tk.Entry(self.root, textvariable=self.tdv)
        tde.grid(row=1, column=1, padx=10, pady=5)

        # Priority Label and Dropdown
        tk.Label(self.root, text="Priority:").grid(row=2, column=0, sticky="w")
        po = ["Low", "Medium", "High"]
        pd = ttk.Combobox(self.root, textvariable=self.pv, values=po)
        pd.grid(row=2, column=1, padx=10, pady=5)

        # Due Date Label and Calendar
        tk.Label(self.root, text="Due Date:").grid(row=3, column=0, sticky="w")
        dde = DateEntry(self.root, textvariable=self.ddv, date_pattern="yyyy-mm-dd")
        dde.grid(row=3, column=1, padx=10, pady=5)

        # Add Task Button
        atb = tk.Button(self.root, text="Add Task", command=self.at)
        atb.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Task List Treeview
        self.tlt = ttk.Treeview(self.root, columns=("description", "Priority", "Due Date"))
        self.tlt.grid(row=5, column=0, columnspan=2, padx=9, pady=5)
        self.tlt.heading("#0", text="Task Name")
        self.tlt.heading("description", text="description")
        self.tlt.heading("Priority", text="Priority")
        self.tlt.heading("Due Date", text="Due Date")

        # Delete Task Button
        dtb = tk.Button(self.root, text="Delete Task", command=self.dt)
        dtb.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        # Clear Task Button
        ctb = tk.Button(self.root, text="Clear Task", command=self.ct)
        ctb.grid(row=6, column=1, padx=10, pady=5, sticky="e")

    def at(self):
        #get data (name, priority, due_date)
        name = self.tnv.get()
        priority = self.pv.get()
        due_date = self.ddv.get()
        #if data not empty
        if name and priority and due_date:
            #call Task constructor class
            task = Task(name, priority, due_date)
            #append list
            self.tasks.append(task)
            #insert into treeview
            self.tlt.insert("", tk.END, text=task.name, values=(task.priority, task.due_date))
            #set inputs to blank
            self.tnv.set("")
            self.pv.set("")
            self.ddv.set("")
        #if data empty
        else:
            #create error message box
            messagebox.showerror("Error", "Please fill in all fields.")

    def dt(self):
        #gets task list tree
        si = self.tlt.selection()
        #if variable not empty
        if si:
            #sets tn to the text line tree line
            tn = self.tlt.item(si)["text"]
            #for every task in list of tasks
            for task in self.tasks:
                #if name in task is exactly tn
                if task.name == tn:
                    #remove task from self.tasks
                    self.tasks.remove(task)
                    #remove task from task list treeview
                    self.tlt.delete(si)
                    #break code
                    break

    def ct(self):
        #set inputs to blank
        self.tnv.set("")
        self.pv.set("")
        self.ddv.set("")

#while loop
start=True
while start:
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
    break
