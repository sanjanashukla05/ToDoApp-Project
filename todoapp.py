import tkinter as tk
from tkinter import messagebox

def add_task():
    task=task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END,task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input error", "Task cannot be empty")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task to delete")

def clear_task():
    if messagebox.askyesno("Confirm" , "Are you sure you want to clear all the tasks?"):
        task_listbox.delete(0 , tk.END)

def edit_task():
    try:
        selected_task_index=task_listbox.curselection()[0]
        new_task=task_entry.get().strip()
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input error", "Task cannot be empty")

    except IndexError:
        messagebox.showwarning("Selection error","No task selected to edit!")  

def populate_task_entry():
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(selected_task_index)
        task_entry.delete(0 , tk.END)
        task_entry.insert(0, selected_task)
    
    except IndexError:
        messagebox.showwarning("Selection error", "No task selected to edit")

#main window

app=tk.Tk()
app.title("TO DO APP")
app.geometry("450x500")

task_label=tk.Label(app, text="Enter your task: ", font="Arial, 12")
task_label.pack(pady=10)

task_entry=tk.Entry(app, width=30 , font="Arial, 13")
task_entry.pack(pady=5)

add_button=tk.Button(app , text="Add Task" , width=15, command=add_task)
delete_button=tk.Button(app , text="Delete Task" , width=15, command=delete_task)
clear_button=tk.Button(app, text="Clear Tasks", width=15, command=clear_task)

edit_button=tk.Button(app, text="Edit Task", width=15, command=edit_task)
populate_button=tk.Button(app, text="Select task", width=15, command=populate_task_entry)

add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)
populate_button.pack(pady=5)
edit_button.pack(pady=5)

#listbox

task_listbox=tk.Listbox(app ,width=50,height=15,font="Arial, 12", )
task_listbox.pack(pady=10)

app.mainloop()