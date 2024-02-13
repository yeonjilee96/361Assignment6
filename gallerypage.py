import os
import tkinter as tk
from PIL import Image, ImageTk

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.png'):
            villager_name = filename[:-4]  # removing png to get villager names
            path = os.path.join(folder, filename)

            image = Image.open(path)
            image.thumbnail((100, 100))  # resize to fit in grid
            images.append((ImageTk.PhotoImage(image), villager_name))

    return images

def create_gallery(frame, images, page, images_per_page):
    # populate the gallery of images
    for widget in frame.winfo_children():
        widget.destroy()

    start = page * images_per_page
    end = start + images_per_page
    for i, (img, name) in enumerate(images[start:end]):
        column = i % 5
        row = 2 * (i // 5)  
        img_label = tk.Label(frame, image=img)
        img_label.image = img  # ref to image
        img_label.grid(row=row, column=column, padx=10, pady=3)

        name_label = tk.Label(frame, text=name)
        name_label.grid(row=row+1, column=column, padx=10, pady=3)
        
def setup_gallery(root, go_home):
    home_button = tk.Button(root, text="RETURN HOME", command=go_home)
    home_button.pack(side="top", pady=0)

    root.title("Animal Crossing Villager Gallery")

    title_label = tk.Label(root, text="Animal Crossing Villager Database", font=("Arial", 24))
    title_label.pack(side="top", pady=10)

    frame = tk.Frame(root)
    frame.pack(expand=True)

    images = load_images('villagerfolder')

    # Pagination setup
    images_per_page = 10
    total_pages = len(images) // images_per_page
    current_page = 0

    def update_gallery(page):
        create_gallery(frame, images, page, images_per_page)

    def next_page():
        nonlocal current_page
        if current_page < total_pages:
            current_page += 1
            update_gallery(current_page)

    def prev_page():
        nonlocal current_page
        if current_page > 0:
            current_page -= 1
            update_gallery(current_page)

    # Initial display
    update_gallery(current_page)

    # Navigation buttons
    navigation_frame = tk.Frame(root)
    navigation_frame.pack(side="bottom", pady=10)

    prev_button = tk.Button(navigation_frame, text="<< Prev", command=prev_page)
    next_button = tk.Button(navigation_frame, text="Next >>", command=next_page)

    prev_button.pack(side="left", padx=10)
    next_button.pack(side="right", padx=10)

    root.mainloop()


