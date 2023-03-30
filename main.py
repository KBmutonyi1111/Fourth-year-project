import tkinter as tk

# Create main window
root = tk.Tk()
root.title('CONTENT SIEVER')
root.geometry('500x300')
root.configure(bg='pink')

# Create title label
title_label = tk.Label(root, text='CONTENT SIEVER', bg='pink', fg='white', font=('Blackadder ITC', 30))
title_label.pack(pady=20)

# Create username and password fields
username_label = tk.Label(root, text='Username:', bg='pink', font=('Arial', 14))
username_entry = tk.Entry(root, bg='white', font=('Arial', 14))

password_label = tk.Label(root, text='Password:', bg='pink', font=('Arial', 14))
password_entry = tk.Entry(root, bg='white', show='*', font=('Arial', 14))

username_label.place(relx=0.25, rely=0.5, anchor='center', x=-70)
username_entry.place(relx=0.25, rely=0.5, anchor='center', x=70)

password_label.place(relx=0.25, rely=0.5, anchor='center', x=-70, y=30)
password_entry.place(relx=0.25, rely=0.5, anchor='center', x=70, y=30)

# Create login button
login_button = tk.Button(root, text='Log in', bg='pink', fg='black', font=('Arial', 14))
login_button.place(relx=0.75, rely=0.5, anchor='center')

# Create create account and forgot password button
create_account_button = tk.Button(root, text='Create Account', bg='light blue', fg='white', font=('Arial', 12))
forgot_password_button = tk.Button(root, text='Forgot Password', bg='light blue', fg='white', font=('Arial', 12))
create_account_button.place(relx=0, rely=1.0, anchor='sw', x=20, y=-20)
forgot_password_button.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

# Run main loop
root.mainloop()

#Database
import sqlite3

# create a connection to the database
conn = sqlite3.connect('user_accounts.db')

# create a cursor object
cursor = conn.cursor()

# create a table to store user accounts
cursor.execute('''CREATE TABLE IF NOT EXISTS user_accounts (
                    id INTEGER PRIMARY KEY,
                    email TEXT NOT NULL UNIQUE,
                    phone_number TEXT NOT NULL UNIQUE,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    age INTEGER NOT NULL
                )''')

# function to insert a new user account into the table
def create_account(email, phone_number, username, password, age):
    cursor.execute('''INSERT INTO user_accounts (email, phone_number, username, password, age)
                    VALUES (?, ?, ?, ?, ?)''', (email, phone_number, username, password, age))
    conn.commit()
    print("User account created successfully")

# function to retrieve a user account by their username
def get_account_by_username(username):
    cursor.execute('''SELECT * FROM user_accounts WHERE username = ?''', (username,))
    return cursor.fetchone()

# close the connection to the database
conn.close()

# Age registration and name of child.
def create_user(self):
    # Get name and age from entries
    name = self.name_entry.get()
    age = int(self.age_entry.get())

    # Create user and add to tracker
    user = User(name, age)
    self.tracker.add_user(user)

# Self-timer and app restriction code.
def update_screen_time_label(self):
    # Get current user and update screen time label
    user = self.tracker.users[-1]
    if user.age <= 10:
        max_screen_time = datetime.timedelta(hours=2)
    elif user.age <= 15:
        max_screen_time = datetime.timedelta(hours=3)
    else:
        max_screen_time = datetime.timedelta.max
    screen_time_remaining = max_screen_time - user.screen_time
    if screen_time_remaining < datetime.timedelta(0):
        screen_time_remaining = datetime.timedelta(0)
    self.screen_time_label.config(text="Screen Time Remaining: {}".format(screen_time_remaining))


def update_restricted_apps_label(self):
    # Restrict certain apps based on the user's age category
    restricted_apps = []
    if age_category == "Under 5":
        restricted_apps = ["Candy Crush", "Words With Friends", "Solitaire", "Netflix"]
    elif age_category == "Under 10":
        restricted_apps = ["Tiktok", "Instagram", "Facebook", "Twitter", "LinkedIn", "Netflix"]
    elif age_category == "Under 13":
        restricted_apps = ["Facebook", "Twitter", "LinkedIn", "Instagram"]
    elif age_category == "Under 18":
        restricted_apps = ["Tinder", "Reddit", "Bumble"]

root.mainloop()
