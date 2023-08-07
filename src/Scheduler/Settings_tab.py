from tkinter import ttk, messagebox
import pyodbc

def create_tab(parent, app):
    tab = ttk.Frame(parent)
    tab.pack(fill='both', expand=True)
      
    conn_label = ttk.Label(tab, text="Connection string:")
    conn_label.pack()

    conn_entry = ttk.Entry(tab)
    # TEMPORARY
    conn_entry.insert(0, "Driver={ODBC Driver 17 for SQL Server};Server=SRVSQLHOTEL03;Database=MKB-ITK-RPA;Trusted_Connection=yes;")
    conn_entry.pack(fill='x')

    conn_button = ttk.Button(tab, text="Connect", command=lambda: connect(app, conn_entry, conn_button))
    conn_button.pack()

    # TEMPORARY
    connect(app, conn_entry, conn_button)

    return tab

def connect(app, conn_entry: ttk.Entry, conn_button: ttk.Button):
    conn_string = conn_entry.get()
    try:
        pyodbc.connect(conn_string).close()
        app._connection_string = conn_string
        conn_button.configure(text="Connected!")
    except Exception as e:
        conn_button.configure(text="Connect")
        messagebox.showerror("Connection failed", str(e))