import pandas as pd
import pickle
import tkinter as tk

passname = {}  # name : password

def storing():
    global window
    window = tk.Toplevel()
    window.title("password storing system")
    window.geometry('1500x250')  # width , height
    labelstrname = tk.Label(window, text='name')
    labelstrname.pack()
    labelstrpass = tk.Label(window, text='pass')
    labelstrpass.pack()

    inputname = tk.Text(window, height=1, width=10)
    inputname.pack()

    inputpass = tk.Text(window, height=1, width=10)
    inputpass.pack()

    def readdes():
        reading()
        window.destroy()

    def confirm():
        inpname = inputname.get(1.0, tk.END).strip()  # remove spaces
        inppass = inputpass.get(1.0, tk.END).strip()
        with open("data.pkl", "rb") as f:
            passname = pickle.load(f)  # rb to read
        passname[inpname] = inppass

        with open("data.pkl", "wb") as f:  # f represent the fileS
            pickle.dump(passname, f)  # wb is override ab to add
        print(passname)

    buttoncon = tk.Button(window, text="confirm", command=confirm)
    buttoncon.pack()

    buttontest = tk.Button(window, text='test', command=readdes)
    buttontest.pack()

def reading():
    with open("data.pkl", "rb") as f:
        file = pickle.load(f)
    loaded = pd.DataFrame.from_dict(file, orient='index', columns=['password'])
    print(loaded)
    
    windowread = tk.Tk()
    label = tk.Label(windowread , text = loaded)
    label.pack()
    window.title("password storing system")
    window.geometry("1000x600")
def stori():
    global window
    window.withdraw()
    storing()
    
def start():
    global window
    window = tk.Tk()
    buttonstor = tk.Button(window, text="storing system", command=stori)
    buttonstor.pack()
    window.mainloop()

start()