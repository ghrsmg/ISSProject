import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class CafeManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cafe Management System")
        self.master.geometry("800x600")
        self.current_page = None
        self.bartender_tasks = []
        self.current_bartender = None

        self.show_main_page()

    def show_main_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text="Welcome to Cafe Management System", font=("Arial", 20)).pack(pady=20)

        manager_button = tk.Button(self.current_page, text="Manager", font=("Arial", 14), width=15, height=2, command=self.show_manager_page)
        manager_button.pack(pady=20)
        bartender_button = tk.Button(self.current_page, text="Bartender", font=("Arial", 14), width=15, height=2, command=self.show_bartender_selector)
        bartender_button.pack(pady=20)

    def show_manager_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text="Manager Page", font=("Arial", 20)).pack(pady=20)

        home_button = tk.Button(self.current_page, text="Home", font=("Arial", 14), width=15,
                                command=self.show_main_page)
        home_button.pack(pady=10)

        assign_button = tk.Button(self.current_page, text="Assign Task", font=("Arial", 14), width=15,
                                  command=self.assign_task)
        assign_button.pack(pady=5)

        add_bartender_button = tk.Button(self.current_page, text="Add Bartender", font=("Arial", 14), width=15,
                                         command=self.add_bartender)
        add_bartender_button.pack(pady=5)

        delete_button = tk.Button(self.current_page, text="Delete Task", font=("Arial", 14), width=15,
                                  command=self.delete_task)
        delete_button.pack(pady=5)

        view_button = tk.Button(self.current_page, text="View Tasks", font=("Arial", 14), width=15,
                                command=self.view_tasks)
        view_button.pack(pady=5)

        view_checkins_button = tk.Button(self.current_page, text="View Check-Ins", font=("Arial", 14), width=15,
                                         command=self.view_checkins)
        view_checkins_button.pack(pady=5)

        delete_bartender_button = tk.Button(self.current_page, text="Delete Bartender", font=("Arial", 14), width=15,
                                            command=self.delete_bartender)
        delete_bartender_button.pack(pady=5)

    def add_bartender(self):
        bartender_window = tk.Toplevel(self.master)
        tk.Label(bartender_window, text="Add Bartender", font=("Arial", 16)).pack(pady=10)
        bartender_entry = tk.Entry(bartender_window, width=30)
        bartender_entry.pack(pady=5)

        def add():
            bartender = bartender_entry.get().strip()  # Strip leading/trailing whitespace
            if not bartender:
                messagebox.showwarning("Empty Bartender", "Please enter the full name of the bartender.")
                return

            with open("bartenders.txt", "a") as file:
                file.write(f"{bartender}\n")
            messagebox.showinfo("Bartender Added", f"Bartender '{bartender}' added successfully.")
            bartender_window.destroy()

        tk.Button(bartender_window, text="Add", font=("Arial", 14), command=add).pack(pady=5)

    def show_bartender_selector(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text="Select Bartender", font=("Arial", 20)).pack(pady=20)

        with open("bartenders.txt", "r") as file:
            bartenders = [bartender.strip() for bartender in file.readlines()]

        bartender_var = tk.StringVar(self.current_page)
        bartender_var.set(bartenders[0])
        bartender_dropdown = tk.OptionMenu(self.current_page, bartender_var, *bartenders)
        bartender_dropdown.pack(pady=10)

        def select_bartender():
            self.current_bartender = bartender_var.get()
            self.show_bartender_page()

        tk.Button(self.current_page, text="Select", font=("Arial", 14), command=select_bartender).pack(pady=10)

    def show_bartender_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.master)
        self.current_page.pack()

        tk.Label(self.current_page, text=f"Bartender: {self.current_bartender}", font=("Arial", 20)).pack(pady=20)

        home_button = tk.Button(self.current_page, text="Home", font=("Arial", 14), width=15, command=self.show_main_page)
        home_button.pack(pady=10)

        view_tasks_button = tk.Button(self.current_page, text="View All Tasks", font=("Arial", 14), width=15, command=self.view_all_tasks)
        view_tasks_button.pack(pady=5)

        mark_completed_button = tk.Button(self.current_page, text="Mark Task Completed", font=("Arial", 14), width=20, command=self.mark_task_completed)
        mark_completed_button.pack(pady=5)

        checkin_button = tk.Button(self.current_page, text="Check-In", font=("Arial", 14), width=15, command=self.check_in)
        checkin_button.pack(pady=5)

    def assign_task(self):
        task_window = tk.Toplevel(self.master)
        tk.Label(task_window, text="Assign Task", font=("Arial", 16)).pack(pady=10)
        task_entry = tk.Entry(task_window, width=30)
        task_entry.pack(pady=5)

        with open("bartenders.txt", "r") as file:
            bartenders = file.readlines()

        bartender_var = tk.StringVar(task_window)
        bartender_var.set(bartenders[0].strip())
        bartender_dropdown = tk.OptionMenu(task_window, bartender_var, *bartenders)
        bartender_dropdown.pack(pady=5)

        def assign():
            task = task_entry.get().strip()  # Strip leading/trailing whitespace
            bartender = bartender_var.get().strip()  # Strip leading/trailing whitespace
            if not task:
                messagebox.showwarning("Empty Task", "Please enter a task.")
                return
            with open("tasks.txt", "a") as file:
                file.write(f"{task} (Bartender: {bartender}) (Pending)\n")
            task_window.destroy()

        tk.Button(task_window, text="Assign", font=("Arial", 14), command=assign).pack(pady=5)

    def delete_task(self):
        task_window = tk.Toplevel(self.master)
        tk.Label(task_window, text="Delete Task", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(task_window, width=50, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
        task_listbox.pack(pady=5)

        def delete():
            selected_task = task_listbox.curselection()
            if selected_task:
                task = task_listbox.get(selected_task)
                with open("tasks.txt", "r") as file:
                    lines = file.readlines()
                with open("tasks.txt", "w") as file:
                    for line in lines:
                        if task not in line:
                            file.write(line)
                messagebox.showinfo("Task Deleted", "Task deleted successfully.")
                task_window.destroy()
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to delete.")

        tk.Button(task_window, text="Delete", font=("Arial", 14), command=delete).pack(pady=5)

    def view_tasks(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="All Pending Tasks", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(view_window, width=50, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if "(Pending)" in task:
                    task_listbox.insert(tk.END, task.strip())
        task_listbox.pack(pady=5)

    def view_checkins(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="Check-Ins", font=("Arial", 16)).pack(pady=10)
        checkins_listbox = tk.Listbox(view_window, width=50, font=("Arial", 12))
        with open("checkins.txt", "r") as file:
            checkins = file.readlines()
            for checkin in checkins:
                checkins_listbox.insert(tk.END, checkin.strip())
        checkins_listbox.pack(pady=5)

    def delete_bartender(self):
        bartender_window = tk.Toplevel(self.master)
        tk.Label(bartender_window, text="Delete Bartender", font=("Arial", 16)).pack(pady=10)
        bartender_listbox = tk.Listbox(bartender_window, width=50, font=("Arial", 12))
        with open("bartenders.txt", "r") as file:
            bartenders = file.readlines()
            for bartender in bartenders:
                bartender_listbox.insert(tk.END, bartender.strip())
        bartender_listbox.pack(pady=5)

        def delete():
            selected_bartender = bartender_listbox.curselection()
            if selected_bartender:
                bartender = bartender_listbox.get(selected_bartender)
                with open("bartenders.txt", "r") as file:
                    lines = file.readlines()
                with open("bartenders.txt", "w") as file:
                    for line in lines:
                        if bartender not in line:
                            file.write(line)
                messagebox.showinfo("Bartender Deleted", f"Bartender '{bartender}' deleted successfully.")
                bartender_window.destroy()
            else:
                messagebox.showwarning("No Bartender Selected", "Please select a bartender to delete.")

        tk.Button(bartender_window, text="Delete", font=("Arial", 14), command=delete).pack(pady=5)
    def view_all_tasks(self):
        view_window = tk.Toplevel(self.master)
        tk.Label(view_window, text="All Tasks", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(view_window, width=70, font=("Arial", 12))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if "(Completed)" in task:
                    task_listbox.insert(tk.END, task.strip())
                else:
                    task_listbox.insert(tk.END, task.strip())
        task_listbox.pack(pady=5)

    def mark_task_completed(self):
        task_window = tk.Toplevel(self.master)
        tk.Label(task_window, text="Mark Task Completed", font=("Arial", 16)).pack(pady=10)
        task_listbox = tk.Listbox(task_window, width=50, font=("Arial", 12))

        # Filter tasks to only show pending tasks assigned to the current bartender
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                if "(Pending)" in task and task.split("(Bartender:")[1].strip().startswith(self.current_bartender):
                    task_listbox.insert(tk.END,
                                        task.strip())  # Add only pending tasks assigned to the current bartender

        task_listbox.pack(pady=5)

        def mark_completed():
            selected_task = task_listbox.curselection()
            if selected_task:
                task_index = selected_task[0]  # Get the index of the selected task
                task = task_listbox.get(task_index)  # Get the selected task
                updated_task = task.replace("(Pending)", "(Completed)")  # Mark the task as completed
                task_listbox.delete(task_index)  # Remove the task from the listbox
                task_listbox.insert(task_index, updated_task)  # Insert the updated task into the listbox
                with open("tasks.txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    for line in lines:
                        if task in line:
                            file.write(line.replace("(Pending)", "(Completed)"))
                        else:
                            file.write(line)
                    file.truncate()
                messagebox.showinfo("Task Completed", "Task marked as completed successfully.")
                task_window.destroy()
            else:
                messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

        tk.Button(task_window, text="Mark Completed", font=("Arial", 14), command=mark_completed).pack(pady=5)

    def check_in(self):
        checkin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("checkins.txt", "a") as file:
            file.write(f"\n{self.current_bartender} checked in at {checkin_time}")
        messagebox.showinfo("Check-In", f"Checked in at {checkin_time}")

def main():
    root = tk.Tk()
    app = CafeManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
