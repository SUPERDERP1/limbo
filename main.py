from tkinter import *
import random as r
import time as t
from tkinter import messagebox  # For displaying win/lose messages

correct = r.randint(1, 8)
win = Tk()
win.geometry("1440x900")

# Define the patterns
patterns = [
    {"toprow": [2, 3, 4, 8], "bottomrow": [1, 5, 6, 7]},
    {"toprow": [4, 3, 2, 1], "bottomrow": [8, 7, 6, 5]},
    {"toprow": [5, 6, 7, 8], "bottomrow": [1, 2, 3, 4]},
    {"toprow": [8, 1, 2, 3], "bottomrow": [4, 5, 6, 7]},
    {"toprow": [8, 7, 6, 5], "bottomrow": [4, 3, 2, 1]},
    {"toprow": [7, 6, 5, 4], "bottomrow": [8, 1, 2, 3]},
    {"toprow": [1, 4, 7, 8], "bottomrow": [2, 3, 5, 6]},
    {"toprow": [5, 8, 7, 6], "bottomrow": [1, 2, 3, 4]},
    {"toprow": [1, 5, 3, 7], "bottomrow": [2, 4, 6, 8]},
    {"toprow": [8, 5, 6, 7], "bottomrow": [1, 2, 3, 4]},
    {"toprow": [6, 7, 8, 1], "bottomrow": [2, 3, 4, 5]},
    {"toprow": [6, 5, 4, 3], "bottomrow": [8, 7, 2, 1]},
    {"toprow": [1, 2, 3, 4], "bottomrow": [8, 7, 6, 5]},
    {"toprow": [4, 5, 6, 7], "bottomrow": [1, 2, 3, 8]},
    {"toprow": [2, 1, 8, 7], "bottomrow": [3, 4, 5, 6]},
    {"toprow": [3, 2, 1, 8], "bottomrow": [4, 5, 6, 7]},
    {"toprow": [3, 4, 5, 6], "bottomrow": [1, 2, 7, 8]},
    {"toprow": [7, 8, 1, 2], "bottomrow": [3, 4, 5, 6]},
    {"toprow": [1, 3, 5, 7], "bottomrow": [2, 4, 6, 8]},
    {"toprow": [2, 4, 6, 8], "bottomrow": [1, 3, 5, 7]},
]

# Store initial positions
positions = {
    1: (172, 150),
    2: (472, 150),
    3: (772, 150),
    4: (1072, 150),
    5: (172, 450),
    6: (472, 450),
    7: (772, 450),
    8: (1072, 450),
}

def move_key(key, target_x, target_y, step=300, delay=0.005):
    current_x = key.winfo_x()
    current_y = key.winfo_y()

    while abs(current_x - target_x) >= step or abs(current_y - target_y) >= step:
        # Calculate the next position
        if abs(current_x - target_x) >= step:
            current_x += step if current_x < target_x else -step
        if abs(current_y - target_y) >= step:
            current_y += step if current_y < target_y else -step

        # Move the key to the new position
        key.geometry(f"+{current_x}+{current_y}")
        key.update()
        t.sleep(delay)  # Small delay for smooth animation

    # Ensure the key is exactly at the target position
    key.geometry(f"+{target_x}+{target_y}")
    key.update()

def move_keys_simultaneously(keys, target_positions, step=10, delay=0.01):
    # Get the current positions of all keys
    current_positions = [(key.winfo_x(), key.winfo_y()) for key in keys]

    # Continue moving until all keys reach their target positions
    while any(
        abs(current_x - target_x) >= step or abs(current_y - target_y) >= step
        for (current_x, current_y), (target_x, target_y) in zip(current_positions, target_positions)
    ):
        for i, key in enumerate(keys):
            current_x, current_y = current_positions[i]
            target_x, target_y = target_positions[i]

            # Calculate the next position for the key
            if abs(current_x - target_x) >= step:
                current_x += step if current_x < target_x else -step
            if abs(current_y - target_y) >= step:
                current_y += step if current_y < target_y else -step

            # Update the key's position
            key.geometry(f"+{current_x}+{current_y}")
            key.update()

            # Update the current position
            current_positions[i] = (current_x, current_y)

        # Small delay for smooth animation
        t.sleep(delay)

    # Ensure all keys are exactly at their target positions
    for i, key in enumerate(keys):
        target_x, target_y = target_positions[i]
        key.geometry(f"+{target_x}+{target_y}")
        key.update()

def apply_pattern(pattern):
    # Map keys to their new positions
    new_positions = [
        positions[pattern["toprow"][0]],
        positions[pattern["toprow"][1]],
        positions[pattern["toprow"][2]],
        positions[pattern["toprow"][3]],
        positions[pattern["bottomrow"][0]],
        positions[pattern["bottomrow"][1]],
        positions[pattern["bottomrow"][2]],
        positions[pattern["bottomrow"][3]],
    ]

    # Move all keys simultaneously
    move_keys_simultaneously(
        [key1, key2, key3, key4, key5, key6, key7, key8],
        new_positions
    )

def on_key_click(key_number):
    """Handle the click event for a key."""
    if key_number == correct:
        messagebox.showinfo("Result", "You Win!")
    else:
        messagebox.showinfo("Result", "You Lose!")
    win.destroy()  # Close the game window after the result

def highlight_correct_key():
    """Highlight the correct key in green, wait for 1 second, then turn it back to red."""
    if correct == 1:
        key1.config(bg="green")
        win.after(1000, lambda: key1.config(bg="red"))
    elif correct == 2:
        key2.config(bg="green")
        win.after(1000, lambda: key2.config(bg="red"))
    elif correct == 3:
        key3.config(bg="green")
        win.after(1000, lambda: key3.config(bg="red"))
    elif correct == 4:
        key4.config(bg="green")
        win.after(1000, lambda: key4.config(bg="red"))
    elif correct == 5:
        key5.config(bg="green")
        win.after(1000, lambda: key5.config(bg="red"))
    elif correct == 6:
        key6.config(bg="green")
        win.after(1000, lambda: key6.config(bg="red"))
    elif correct == 7:
        key7.config(bg="green")
        win.after(1000, lambda: key7.config(bg="red"))
    elif correct == 8:
        key8.config(bg="green")
        win.after(1000, lambda: key8.config(bg="red"))

def gstart():
    global key1, key2, key3, key4, key5, key6, key7, key8
    key1 = Toplevel(win, bg="red")
    key2 = Toplevel(win, bg="red")
    key3 = Toplevel(win, bg="red")
    key4 = Toplevel(win, bg="red")
    key5 = Toplevel(win, bg="red")
    key6 = Toplevel(win, bg="red")
    key7 = Toplevel(win, bg="red")
    key8 = Toplevel(win, bg="red")
    key1.geometry("+172+150")
    key2.geometry("+472+150")
    key3.geometry("+772+150")
    key4.geometry("+1072+150")
    key5.geometry("+172+450")
    key6.geometry("+472+450")
    key7.geometry("+772+450")
    key8.geometry("+1072+450")

    # Bind click events to each key
    key1.bind("<Button-1>", lambda e: on_key_click(1))
    key2.bind("<Button-1>", lambda e: on_key_click(2))
    key3.bind("<Button-1>", lambda e: on_key_click(3))
    key4.bind("<Button-1>", lambda e: on_key_click(4))
    key5.bind("<Button-1>", lambda e: on_key_click(5))
    key6.bind("<Button-1>", lambda e: on_key_click(6))
    key7.bind("<Button-1>", lambda e: on_key_click(7))
    key8.bind("<Button-1>", lambda e: on_key_click(8))

    win.iconify()

    # Highlight the correct key and start the movement after 1 second
    highlight_correct_key()
    win.after(1500, start_movement)

def start_movement():
    """Start applying random patterns."""
    for _ in range(10):
        pattern = r.choice(patterns)
        apply_pattern(pattern)
        win.update()  # Ensure the GUI updates smoothly

start = Button(
    text="start",
    command=gstart
)
start.pack()
win.mainloop()
