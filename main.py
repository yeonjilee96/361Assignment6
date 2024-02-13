import tkinter as tk
from PIL import Image, ImageTk
import gallerypage

def show_gallery():
    # open gallery and remove main page
    for widget in home_frame.winfo_children():
        widget.destroy()
    gallerypage.setup_gallery(root, show_main)

def show_main():
    # open main page and remove gallery
    for widget in root.winfo_children():
        widget.destroy()
    
    global home_frame
    home_frame = tk.Frame(root)
    home_frame.pack(expand=True)

    title = tk.Label(home_frame, text="Villager Database", font=("Arial", 16))
    title.pack(pady=20)

    gallery_button = tk.Button(home_frame, text="See all villagers", command=show_gallery)
    gallery_button.pack(pady=10)

def main():
    global root, home_frame
    root = tk.Tk()
    root.title("Animal Crossing Villager Database")
    root.geometry("800x600")

    show_main()

    root.mainloop()

if __name__ == "__main__":
    main()