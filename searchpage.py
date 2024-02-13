import tkinter as tk
from PIL import Image, ImageTk
import zmq

def show_search_page():
    search_root.deiconify()

def hide_search_page():
    search_root.withdraw()

def main():
    global search_root
    window_width, window_height = 800, 500
    search_root = tk.Tk()
    search_root.title("Search Page")
    search_root.geometry("800x700")

    # initially hide
    search_root.withdraw()

    bg_image = Image.open("background.png")

    image_width, image_height = bg_image.size
    ratio = max(window_width / image_width, window_height / image_height)
    new_size = (int(image_width * ratio), int(image_height * ratio))
    
    bg_image = bg_image.resize(new_size, Image.Resampling.BILINEAR)

    bg_photo = ImageTk.PhotoImage(bg_image)

    # create bg label
    bg_label = tk.Label(search_root, image = bg_photo)
    bg_label.place(x = 0, y = 0, relwidth = 1, relheight= 1)

    # add code for search page

    # zeromq context and socket
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv()
        if message == b"open_search":
            show_search_page()
            break
        elif message != b"open_search":
            pass
    
    search_root.mainloop()
    socket.close()

if __name__ == "__main__":
    main()