import tkinter as tk

# Set initial count values for each person
count_dict = {"Prat": 0, "Arjun": 0, "Parth": 0, "Kush": 0, "Ant": 0, "Ran": 0}

# Define function to increment count for a given person
def add_count(person):
    count_dict[person] += 1
    count_label_dict[person].config(text=f"{person}: {count_dict[person]} unalive")

# Define function to reset counts for a given person
def reset_count(person):
    count_dict[person] = 0
    count_label_dict[person].config(text=f"{person}: {count_dict[person]} unalive")

# Create Tkinter window
window = tk.Tk()

# Set window size and title
window.geometry("600x400")
window.title("Unalive Count")

# Set background image
bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create labels and buttons for each person
count_label_dict = {}
for i, person in enumerate(count_dict):
    # Create label to display count for person
    count_label_dict[person] = tk.Label(window, text=f"{person}: 0 unalive", font=("Arial", 16), bg="#FFFFFF", padx=20, pady=10)
    count_label_dict[person].grid(row=i, column=0, padx=20, pady=10)
    
    # Create add button for person
    add_button = tk.Button(window, text="Add", font=("Arial", 14), bg="#CCCCCC", command=lambda p=person: add_count(p))
    add_button.grid(row=i, column=1, padx=20, pady=10)
    
    # Create reset button for person
    reset_button = tk.Button(window, text="Reset", font=("Arial", 14), bg="#CCCCCC", command=lambda p=person: reset_count(p))
    reset_button.grid(row=i, column=2, padx=20, pady=10)

# Start Tkinter event loop
window.mainloop()
