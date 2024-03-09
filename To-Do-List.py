import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_var = tk.StringVar()

        self.task_entry = tk.Entry(master, textvariable=self.task_var)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack(expand=True, fill=tk.BOTH)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.refresh_tasks()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_var.set("")
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_as_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] = f"{self.tasks[task_index]} - Completed"
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
