import tkinter as tk
from tkinter import filedialog

def create_files():
    input_data = entry.get("1.0", tk.END)
    input_file_path = 'jadwal_pelajaran.txt'
    with open(input_file_path, 'w') as input_file:
        input_file.write(input_data)
        input_file.close()
        entry.delete("1.0", tk.END)
    result_label.config(text="Berhasil dibuat!", foreground='white')

def browse_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
        entry.delete("1.0", tk.END)
        entry.insert("1.0", content)
        file.close()
    result_label.config(text="File telah dibuka!", foreground='white')

window = tk.Tk()
window.title("Aplikasi Jadwal Pelajaran")
window['bg'] = 'purple'

entry = tk.Text(window, width=30,height=10)
entry.grid(row=0, column=0, padx=20, pady=20)

frame = tk.Frame(window)
frame.grid(row=0, column=1, padx=10, pady=10)
frame['bg'] = 'purple'

create_button = tk.Button(frame, text="Buat File", command=create_files)
create_button.grid(row=0, column=0, pady=10)

browse_button = tk.Button(frame, text="Buka File", command=browse_file)
browse_button.grid(row=1, column=0, padx=10, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, pady=10)
result_label['bg'] = 'purple'


window.mainloop()
