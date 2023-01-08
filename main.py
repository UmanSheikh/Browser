import tkinter as tk
from googlesearch import search
import tkinterweb as web

def callback(url):
    new_window = tk.Tk()
    new_window.title("Website")
    new_window.geometry("800x600")
    frame = web.HtmlFrame(new_window, horizontal_scrollbar="auto")
    frame.load_website(url)
    frame.pack(expand=1, fill="both")
    new_window.mainloop()
    


def search_google():
    box = tk.Listbox(frame2, width=100, height=20)
    box.pack(pady=5)
    query = entry.get()
    for url in search(query, num=10, stop=10, pause=2):
        box.insert(tk.END, url)
        box.bind("<Button-1>", lambda e:
            callback(url))


root = tk.Tk()
root.title("Uman's Browser")
root.geometry("800x600")
frame = tk.Frame(root)
frame.pack()
label = tk.Label(frame, text="Enter your search query", font=("Arial", 24, "bold"))
label.pack(pady=50)
entry = tk.Entry(frame, width=50)
entry.pack(pady=5)
btn = tk.Button(frame, text="Search", command=search_google)
btn.pack(pady=1)

frame2 = tk.Frame(root)
frame2.pack()
label2 = tk.Label(frame2, text="Results", font=("Arial", 24, "bold"))
label2.pack(pady=50)


root.mainloop()

