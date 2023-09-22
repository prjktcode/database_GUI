import tkinter as tk
import re
import sqlite3
import matplotlib.pyplot as plt
from tkinter import messagebox

class AnalysisWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Analysis')
        self.geometry('400x200')

        tk.Button(self, text='Mean Store Size', command=self.mean_store_size).grid(row=0, column=0, pady=5)

        tk.Label(self, text='Store ID:').grid(row=1, column=0, pady=5)
        self.store_id_entry = tk.Entry(self)
        self.store_id_entry.grid(row=1, column=1, pady=5)

        tk.Label(self, text='Department ID:').grid(row=2, column=0, pady=5)
        self.department_id_entry = tk.Entry(self)
        self.department_id_entry.grid(row=2, column=1, pady=5)

        tk.Button(self, text='Time Series', command=self.time_series).grid(row=3, column=1, pady=5)

    def mean_store_size(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT AVG(Size) FROM stores WHERE store_type="A"')
        mean_size_a = cursor.fetchone()[0]
        cursor.execute('SELECT AVG(Size) FROM stores WHERE store_type="B"')
        mean_size_b = cursor.fetchone()[0]
        cursor.execute('SELECT AVG(Size) FROM stores WHERE store_type="C"')
        mean_size_c = cursor.fetchone()[0]

        print(f'Mean size for store type A: {mean_size_a}')
        print(f'Mean size for store type B: {mean_size_b}')
        print(f'Mean size for store type C: {mean_size_c}')

        conn.close()

    def time_series(self):

        store_id = self.store_id_entry.get()
        department_id = self.department_id_entry.get()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(f'SELECT date, weekly_sales FROM sales WHERE store_id={store_id} AND dept_id={department_id}')
        sales_data = cursor.fetchall()

        dates = [row[0] for row in sales_data]
        sales = [row[1] for row in sales_data]

        plt.plot(dates, sales)
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.title(f'Sales for Store {store_id}, Department {department_id}')
        plt.show()

        conn.close()

class UpdateManagerWindow(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Update Manager')
    self.geometry('400x200')

    tk.Label(self, text='Store ID:').grid(row=0, column=0, pady=5)
    self.store_id_entry = tk.Entry(self)
    self.store_id_entry.grid(row=0, column=1, pady=5)

    tk.Label(self, text='Manager Email:').grid(row=1, column=0, pady=5)
    self.manager_email_entry = tk.Entry(self)
    self.manager_email_entry.grid(row=1, column=1, pady=5)

    tk.Button(self, text='Update', command=self.update_manager).grid(row=2, column=1, pady=5)

  def update_manager(self):

    store_id = self.store_id_entry.get()
    manager_email = self.manager_email_entry.get()

    if not re.match(r'[^@]+@[^@]+\.[^@]+', manager_email):
      messagebox.showerror('Error', 'Invalid email')
      return

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE managers SET email=? WHERE store_id=?', (manager_email, store_id))
    conn.commit()
    conn.close()

    messagebox.showinfo('Success', 'Manager updated successfully')

    self.destroy()

class MainWindow(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Main Window')
    self.geometry('400x200')

    tk.Button(self, text='Update Manager', command=self.open_update_manager_window).grid(row=0, column=0, pady=5)

    tk.Button(self, text='Analysis', command=self.open_analysis_window).grid(row=1, column=0, pady=5)

  def open_update_manager_window(self):
    UpdateManagerWindow()

  def open_analysis_window(self):
    AnalysisWindow()

if __name__ == '__main__':
  window = MainWindow()
  window.mainloop()