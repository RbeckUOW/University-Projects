import tkinter as tk
from tkinter import messagebox

# Define the name of the file created for the order summary
filename = "order_summary.txt"

# Window background colours for light and dark modes
window_colours = {
    "darkmode": {"bg": "#15202B"},
    "lightmode": {"bg": "#FAFAFA"}
}

# Frame colours for light and dark modes
frame_colours = {
    "darkmode": {"bg": "#22303C"},
    "lightmode": {"bg": "#E4E5F1"}
}

# Canvas background colours for light and dark mode
canvas_colours = {
    "darkmode": {"bg": "#33314C"},
    "lightmode": {"bg": "#D4D5E1"}
}

# Button colours for light and dark mode including text colours to contrast
button_colours = {
    "darkmode": {"bg": "#4C7E2A", "fg": "white", "active_bg": "#345115", "active_fg": "white"},
    "lightmode": {"bg": "#8BABF1", "fg": "black", "active_bg": "#6AA3E3", "active_fg": "black"}
}

# Dictionary of all choices that the user makes throughout the system

current_selections = {
    "shapes": {
        "Cuboid": 1,
        "Cube": 2,
        "Cylinder": 3,
    },
    "pattern page": {
        "paper": {  # Types of paper for the selection page
            "Standard Paper": 1,
            "Premium Paper": 2
        },
        "price_per_cm": {  # Paper Prices for the cost calculation
            "Standard Paper": 0.4,
            "Premium Paper": 0.75
        }
    },
    "extras": {
        "addons": {
            "gift_bow_selected": False,
            "gift_message_type": "",
            "gift_message_selected": False,
            "gift_message_index": 0
        },
        "gift_messages": {  # List of possible preset gift messages
            "message": {
                0: "Happy Birthday! May your day be filled with laughter and joy",
                1: "Congratulations on your graduation! Your hard work has paid off.",
                2: "Wishing you a Merry Christmas and a Happy New Year filled with love and laughter.",
                3: "Happy anniversary to the perfect couple! Here's to many more years of love and happiness.",
                4: "Congratulations on your new job! You're destined for success.",
                5: "Best wishes on your wedding day!",
                6: "Happy Mother's Day to the most wonderful mum in the world. You're truly appreciated.",
                7: "Wishing you a speedy recovery! Take care and get well soon.",
                8: "Happy retirement! May this new chapter bring you endless relaxation and enjoyment.",
                9: "Sending heartfelt condolences during this difficult time."
            },
            "cost": {  # Cost for each of the preset messages if selected to update the cost
                0: 1.22,
                1: 1.28,
                2: 1.68,
                3: 1.72,
                4: 1.20,
                5: 0.64,
                6: 1.62,
                7: 1.18,
                8: 1.56,
                9: 1.10
            }
        },
    },
    "calendar": {  # Variables ready for the dropoff and collection calendars
        "date_selection": {
            "dropoff_month": None,
            "dropoff_day": None,
            "dropoff_time": None,
            "collection_month": None,
            "collection_day": None,
            "collection_time": None
        },
        "months": {  # Months for the calendar buttons to fill from
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        },
    },
    "colours": {  # Generic colour names and hex codes for the specific colours as detailed in case study
        "Purple": "#A020F0",  # Purple
        "Grey": "#2F4F4F",  # DarkSlateGray4
        "Blue": "#00BFFF",  # DeepSkyBlue
        "Green": "#20B2AA",  # LightSeaGreen
        "Red": "#EE3A8C",  # VioletRed2
        "Gold": "#FFD700"  # Gold
    }
}

darkmode = False  # Always start program in Light Mode
mode = "lightmode"


# Colour and Theme settings for widgets and windows #
def update_theme():
    global mode

    mode = "darkmode" if darkmode else "lightmode"
    main_window.config(bg=window_colours[mode]["bg"])  # Apply theme to outer window

    # Page Colour Themes
    home_page.config(bg=window_colours[mode]["bg"])
    login_page.config(bg=window_colours[mode]["bg"])
    pattern_page.config(bg=window_colours[mode]["bg"])
    shape_page.config(bg=window_colours[mode]["bg"])
    extras_page.config(bg=window_colours[mode]["bg"])
    order_dates_page.config(bg=window_colours[mode]["bg"])
    summary_page.config(bg=window_colours[mode]["bg"])

    # Canvas Background Settings
    cuboid_canvas.config(bg=canvas_colours[mode]["bg"])
    cube_canvas.config(bg=canvas_colours[mode]["bg"])
    cylinder_canvas.config(bg=canvas_colours[mode]["bg"])
    pattern_one_canvas.config(bg=canvas_colours[mode]["bg"])
    pattern_two_canvas.config(bg=canvas_colours[mode]["bg"])
    preset_gift_message_canvas.config(bg=canvas_colours[mode]["bg"])
    custom_message_canvas.config(bg=canvas_colours[mode]["bg"])
    gift_bow_canvas.config(bg=canvas_colours[mode]["bg"])
    logo_canvas.config(bg=window_colours[mode]["bg"])

    # Frame Colour Settings
    header_frame.config(bg=frame_colours[mode]["bg"])
    footer_frame.config(bg=frame_colours[mode]["bg"])
    colour_buttons_frame.config(bg=frame_colours[mode]["bg"])
    pattern_container_frame.config(bg=frame_colours[mode]["bg"])
    shape_container_frame.config(bg=frame_colours[mode]["bg"])
    cube_cuboid_entry_frame.config(bg=frame_colours[mode]["bg"])
    cylinder_entry_frame.config(bg=frame_colours[mode]["bg"])
    additional_extras_frame.config(bg=frame_colours[mode]["bg"])
    preset_gift_message_frame.config(bg=frame_colours[mode]["bg"])
    custom_message_frame.config(bg=frame_colours[mode]["bg"])
    drop_off_month_frame.config(bg=frame_colours[mode]["bg"])
    drop_off_day_frame.config(bg=frame_colours[mode]["bg"])
    collection_day_frame.config(bg=frame_colours[mode]["bg"])
    collection_month_frame.config(bg=frame_colours[mode]["bg"])
    order_summary_frame.config(bg=frame_colours[mode]["bg"])
    confirm_order_frame.config(bg=frame_colours[mode]["bg"])

    # Label colour settings
    login_label.config(bg=window_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    colour_buttons_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    price_display_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    cube_cuboid_entry_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    cylinder_entry_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    cylinder_bottom_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    cube_cuboid_bottom_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    preset_gift_message_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    preset_gift_continue_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    custom_message_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    custom_message_lower_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    drop_off_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    collection_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    order_summary_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    confirm_order_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])

    # Button colour settings #
    # Header and Footer Buttons
    theme_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                        activebackground=button_colours[mode]["active_bg"],
                        activeforeground=button_colours[mode]["active_fg"])

    home_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                       activebackground=button_colours[mode]["active_bg"],
                       activeforeground=button_colours[mode]["active_fg"])

    login_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                        activebackground=button_colours[mode]["active_bg"],
                        activeforeground=button_colours[mode]["active_fg"])

    narrator_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                           activebackground=button_colours[mode]["active_bg"],
                           activeforeground=button_colours[mode]["active_fg"])

    pattern_page_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                               activebackground=button_colours[mode]["active_bg"],
                               activeforeground=button_colours[mode]["active_fg"])

    start_order_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                              activebackground=button_colours[mode]["active_bg"],
                              activeforeground=button_colours[mode]["active_fg"])

    submit_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                         activebackground=button_colours[mode]["active_bg"],
                         activeforeground=button_colours[mode]["active_fg"])

    extras_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                         activebackground=button_colours[mode]["active_bg"],
                         activeforeground=button_colours[mode]["active_fg"])

    order_date_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                             activebackground=button_colours[mode]["active_bg"],
                             activeforeground=button_colours[mode]["active_fg"])

    complete_order_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                                 activebackground=button_colours[mode]["active_bg"],
                                 activeforeground=button_colours[mode]["active_fg"])
    close_window_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                               activebackground=button_colours[mode]["active_bg"],
                               activeforeground=button_colours[mode]["active_fg"])

    # Radiobutton Settings
    standard_paper_button_one.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    premium_paper_button_two.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    colour_choice_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    cuboid_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    cube_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    cylinder_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    gift_bow_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    preset_gift_message_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    custom_message_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    # Radio buttons always have a white background when active, so I set their colours to light mode

    # Shape dimension line and text settings
    cuboid_canvas.itemconfig(cuboid_depth_text, fill=button_colours[mode]["fg"])
    cuboid_canvas.itemconfig(cuboid_width_text, fill=button_colours[mode]["fg"])
    cuboid_canvas.itemconfig(cuboid_depth_line, fill=button_colours[mode]["fg"])
    cuboid_canvas.itemconfig(cuboid_width_line, fill=button_colours[mode]["fg"])
    cylinder_canvas.itemconfig(cylinder_length_line, fill=button_colours[mode]["fg"])
    cylinder_canvas.itemconfig(cylinder_length_text, fill=button_colours[mode]["fg"])
    # Only the lines and text outside the shape boundaries need to change colours for visibility


# Change theme button function
def toggle_theme():
    global darkmode
    darkmode = not darkmode
    update_theme()  # Apply the updated theme


# Small popup window for narration selection explaining that screen reading function unavailable
def narrator_unavailable():
    narrator_popup = tk.Tk()
    narrator_popup.geometry("300x100+780+170")
    narrator_popup.title("Currently Unavailable!")
    narrator_popup_label = tk.Label(narrator_popup, text="Screen reading/Narration unavailable due to limitations")
    narrator_popup_label.pack(pady=10)
    ok_button = tk.Button(narrator_popup, text="OK", command=narrator_popup.destroy)
    ok_button.pack()
    narrator_popup.config(bg=window_colours[mode]["bg"])
    narrator_popup_label.config(bg=window_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    ok_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                     activebackground=button_colours[mode]["active_bg"],
                     activeforeground=button_colours[mode]["active_fg"])
    narrator_popup.mainloop()


# Class to define the placeholder text entry boxes
class PlaceholderEntry:
    def __init__(self, entry_widget, placeholder_text, placeholder_colour="#22303C", active_colour="#22303C",
                 validate_positive=False):
        self.entry = entry_widget
        self.placeholder_text = placeholder_text
        self.placeholder_colour = placeholder_colour
        self.active_colour = active_colour
        self.validate_positive = validate_positive

        self.is_placeholder_active = True  # Displays the entry box with placeholder text visible
        self.set_placeholder()

        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)
        if self.validate_positive:  # Validate that a positive number is input on key release
            self.entry.bind("<KeyRelease>", self.validate_input)

    # Sets entry box to display placeholder text
    def set_placeholder(self):
        if self.is_placeholder_active:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.placeholder_text)
            self.entry.config(foreground=self.placeholder_colour)

    # Remove the placeholder text when entry box is clicked in
    def clear_placeholder(self, _event):
        if self.is_placeholder_active:
            self.entry.delete(0, tk.END)
            self.entry.config(foreground=self.active_colour)
            self.is_placeholder_active = False

    # Restore the placeholder text when entry box is clicked out
    def restore_placeholder(self, _event):
        if self.entry.get() == "":
            self.is_placeholder_active = True
            self.set_placeholder()

    # Validate the entry is a positive number when each entry box is set to true
    # Turn the text colour red when an incorrect entry is typed
    def validate_input(self, _event=None):
        value = self.entry.get()
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            self.entry.config(foreground=self.active_colour)
            return True
        else:
            self.entry.config(foreground="red")
            return False

    # Get the values entered inside the entry boxes
    def get(self):
        if self.is_placeholder_active:
            return ''  # Return an empty string if the placeholder is shown
        else:
            return self.entry.get()  # Get the text from the embedded Entry widget


# Page switching settings
def switch_to_page(page):
    global current_page, previous_page
    # Set the current page as the previous page before switching
    previous_page = current_page
    current_page.pack_forget()
    page.pack(fill=tk.BOTH, expand=True)
    current_page = page
    update_theme()


# Login button function
def switch_to_login_page():
    switch_to_page(login_page)


# Global window settings #
def switch_to_home_page():
    switch_to_page(home_page)


main_window = tk.Tk()
main_window.title("It's a wrap! - Wrapping Service")
main_window.geometry('1664x936+50+50')  # 50+50 to make sure that the window starts at specific position on the screen
main_window.resizable(True, True)  # Can resize the window if desired

header_frame = tk.Frame(main_window)
header_frame.pack(side="top", fill="x")

home_button = tk.Button(header_frame, text="Home", command=switch_to_home_page)
home_button.pack(side="left", padx=20, pady=5)

theme_button = tk.Button(header_frame, text="Change Theme", command=toggle_theme)
theme_button.pack(side="right", padx=(5, 20), pady=5)

login_button = tk.Button(header_frame, text="Login", command=switch_to_login_page)
login_button.pack(side="right", padx=(5, 5), pady=5)

narrator_button = tk.Button(header_frame, text="Narrator", command=narrator_unavailable)
narrator_button.pack(side="left", padx=5, pady=5)

footer_frame = tk.Frame(main_window)
footer_frame.pack(side="bottom", fill="x")

# End of global window settings #


# Home page #
home_page = tk.Frame(main_window)

logo_canvas = tk.Canvas(home_page, width=350, height=350)
logo_canvas.pack()

logo_canvas.create_rectangle((50, 140), (250, 260), outline="red", fill="#D4D5E1")
logo_canvas.create_polygon((50, 140), (100, 90), (300, 90), (250, 140), outline="red", fill="#D4D5E1")
logo_canvas.create_polygon((250, 140), (300, 90), (300, 210), (250, 260), outline="red", fill="#D4D5E1")
logo_canvas.create_rectangle(50, 190, 250, 210, outline="red", fill="red")
logo_canvas.create_polygon((75, 115), (90, 100), (290, 100), (275, 115), fill="red")
logo_canvas.create_polygon((250, 212), (300, 160), (300, 142), (250, 192), fill="red")
logo_canvas.create_polygon((275, 100), (290, 100), (290, 220), (275, 235), fill="red")
logo_canvas.create_polygon((145, 140), (170, 140), (170, 260), (145, 260), fill="red")
logo_canvas.create_polygon((170, 140), (145, 140), (195, 90), (220, 90), fill="red")

logo_canvas.create_line((50, 270), (175, 300), (300, 270), fill="red", smooth=1, width=2)
logo_canvas.create_line((75, 320), (175, 350), (275, 320), fill="red", smooth=1, width=2)
logo_canvas.create_line((50, 270), (75, 320), fill="red", width=2)
logo_canvas.create_line((300, 270), (275, 320), fill="red", width=2)

logo_text = logo_canvas.create_text((175, 300), fill="#8BABF1", text="It's a wrap!", font=("Times", "30", "bold"))


# Switch to shape page with all frames hidden until a shape is chosen
def switch_to_shape_page():
    cube_cuboid_entry_frame.pack_forget()
    height_entry.entry.pack_forget()
    width_entry.entry.pack_forget()
    depth_entry.entry.pack_forget()
    cylinder_entry_frame.pack_forget()
    length_entry.entry.pack_forget()
    diameter_entry.entry.pack_forget()
    # Change the continue button to point to the pattern page after shapes are chosen
    pattern_page_button.pack(side="right", padx=20, pady=5)
    switch_to_page(shape_page)


start_order_button = tk.Button(home_page, text="Let's get started!", command=switch_to_shape_page)
start_order_button.pack(pady=100)


# End of Home Page #


# Login page #
# Login Popup settings
def submit_login():
    login_popup = tk.Tk()
    login_popup.geometry("300x100+780+170")
    login_popup.title("Coming Soon!")
    login_popup_label = tk.Label(login_popup, text="Feature coming soon!")
    login_popup_label.pack(pady=10)
    ok_button = tk.Button(login_popup, text="OK", command=login_popup.destroy)
    ok_button.pack()
    login_popup.config(bg=window_colours[mode]["bg"])
    login_popup_label.config(bg=window_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    ok_button.config(bg=button_colours[mode]["bg"], fg=button_colours[mode]["fg"],
                     activebackground=button_colours[mode]["active_bg"],
                     activeforeground=button_colours[mode]["active_fg"])
    login_popup.mainloop()


# Login page GUI
login_page = tk.Frame(main_window, padx=10, pady=10)

login_label = tk.Label(login_page, text="Login Page")
login_label.pack()

username_entry = PlaceholderEntry(
    tk.Entry(login_page, foreground="gray"),
    "Username"
)
username_entry.entry.pack()

password_entry = PlaceholderEntry(
    tk.Entry(login_page, foreground="gray"),
    "Password"
)
password_entry.entry.pack()

submit_button = tk.Button(login_page, text="Submit", command=submit_login)
submit_button.pack()

# End of login page #


# Shape selection page #
# Variables
chosen_shape = tk.StringVar()
s = tk.IntVar()
s.set(0)  # Set no shape as default


# Shape page functions
class Cuboid:
    def __init__(self, cuboid_canvas, x1, y1, x2, y2, depth, fcolour="#6AA3E3", bcolour="#5A8CB4",
                 textcolour=None):
        self.canvas = cuboid_canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.depth = depth
        self.fcolour = fcolour
        self.bcolour = bcolour
        self.textcolour = textcolour

    def draw(self):
        # Front face of the cuboid
        self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.bcolour, fill=self.fcolour)

        # Top face of the cuboid
        self.canvas.create_polygon(self.x1, self.y1, self.x1 + self.depth, self.y1 - self.depth,
                                   self.x2 + self.depth, self.y1 - self.depth, self.x2, self.y1,
                                   outline=self.bcolour, fill=self.fcolour)

        # Right face of the cuboid
        self.canvas.create_polygon(self.x2, self.y1, self.x2 + self.depth, self.y1 - self.depth,
                                   self.x2 + self.depth, self.y2 - self.depth, self.x2, self.y2,
                                   outline=self.bcolour, fill=self.fcolour)


class Cube:
    def __init__(self, cube_canvas, x1, y1, x2, y2, depth, fcolour="#6AA3E3", bcolour="#5A8CB4"):
        self.canvas = cube_canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.depth = depth
        self.fcolour = fcolour
        self.bcolour = bcolour

    def draw(self):
        # Front face of the cube
        self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.bcolour, fill=self.fcolour)

        # Top face of the cube
        self.canvas.create_polygon(self.x1, self.y1, self.x1 + self.depth, self.y1 - self.depth,
                                   self.x2 + self.depth, self.y1 - self.depth, self.x2, self.y1,
                                   outline=self.bcolour, fill=self.fcolour)

        # Right face of the cube
        self.canvas.create_polygon(self.x2, self.y1, self.x2 + self.depth, self.y1 - self.depth,
                                   self.x2 + self.depth, self.y2 - self.depth, self.x2, self.y2,
                                   outline=self.bcolour, fill=self.fcolour)


# Cylinder
def circles_between_points(cylinder_canvas, x1, y1, x2, y2, num_circles, fcolour=None):
    for i in range(num_circles):
        x_centre = x1 + (x2 - x1) * i / (num_circles - 1)  # Adjusted for the starting and ending points
        y_centre = y1 + (y2 - y1) * i / (num_circles - 1)  # Adjusted for the starting and ending points
        cylinder_canvas.create_oval(x_centre - 50, y_centre - 50, x_centre + 50, y_centre + 50, outline="#5A8CB4",
                                    fill=fcolour)


def cylinder_back_circle(cylinder_canvas, x1, y1, x2, y2, fcolour="#6AA3E3", bcolour="#5A8CB4"):
    cylinder_canvas.create_oval(x1, y1, x2, y2, fill=fcolour, outline=bcolour)


def cylinder_front_circle(cylinder_canvas, x1, y1, x2, y2, fcolour="#6AA3E3", bcolour="#5A8CB4"):
    cylinder_canvas.create_oval(x1, y1, x2, y2, fill=fcolour, outline=bcolour)


def cylinder_lines(cylinder_canvas, x1, y1, x2, y2, bcolour="#5A8CB4"):
    # Upper Line
    cylinder_canvas.create_line(x1, y1, x2, y2, fill=bcolour)
    # Lower Line
    cylinder_canvas.create_line(x1, y1, x2, y2, fill=bcolour)
    # Central Line
    cylinder_canvas.create_line(x1, y1, x2, y2, fill=bcolour)


# Pack the relevant frames and dimension entry boxes depending on which shape is chosen
def cuboid_selected():
    cylinder_entry_frame.pack_forget()
    side_entry.entry.pack_forget()
    cube_cuboid_entry_frame.pack()
    width_entry.entry.pack()
    height_entry.entry.pack()
    depth_entry.entry.pack()

    current_selections["shapes"]["selected_shape"] = "Cuboid"  # Store the selected shape


def cube_selected():
    cylinder_entry_frame.pack_forget()
    height_entry.entry.pack_forget()
    depth_entry.entry.pack_forget()
    width_entry.entry.pack_forget()
    cube_cuboid_entry_frame.pack()
    side_entry.entry.pack()

    current_selections["shapes"]["selected_shape"] = "Cube"  # Store the selected shape


def cylinder_selected():
    cube_cuboid_entry_frame.pack_forget()
    cylinder_entry_frame.pack()
    diameter_entry.entry.pack()
    length_entry.entry.pack()

    current_selections["shapes"]["selected_shape"] = "Cylinder"  # Store the selected shape


# Calculate the net area depending on which shape is chosen
def calculate_area(dimensions):
    selected_shape = current_selections["shapes"]["selected_shape"]

    if selected_shape == "Cuboid":
        depth = dimensions["depth"]
        width = dimensions["width"]
        height = dimensions["height"]

        # Calculate net area for the cuboid
        net_area1 = 2 * height + depth + 6  # Add 6 for the extra paper overlap
        net_area2 = 2 * height + 2 * width + 6
        total_area = net_area1 * net_area2
        return total_area

    elif selected_shape == "Cylinder":
        diameter = dimensions["diameter"]
        length = dimensions["length"]

        # Asking the user to enter diameter and halving it for the calculation
        # To reduce the risk of user error while measuring
        radius = diameter / 2

        # Cylinder net area
        pi = 3.14159
        base_net_area = 2 * pi * (radius + 3) * (radius + 3)
        column_net_area = 2 * pi * radius * length + 6
        total_area = base_net_area + column_net_area
        return total_area

    elif selected_shape == "Cube":
        side = dimensions["side"]

        # Calculate net area for the cube
        total_area = 6 * side * side
        return total_area

    else:
        return None  # Return None if no shape is selected


# Shape page GUI
shape_page = tk.Frame(main_window)

# Frame to contain shape drawings
shape_container_frame = tk.Frame(shape_page, width=1500, height=400)
shape_container_frame.pack(side="top", padx=15, pady=25)

# Frame for cuboid
cuboid_canvas = tk.Canvas(shape_container_frame, width=500, height=400)
cuboid_canvas.grid(row=0, column=0, padx=15, pady=10)
cuboid_button = tk.Radiobutton(shape_container_frame, text="Cuboid", indicatoron=False,
                               variable=s, value=current_selections["shapes"]["Cuboid"],
                               command=cuboid_selected)
cuboid_button.grid(row=1, column=0, padx=25, pady=10)
# Cuboid values
cuboid_x1 = 150
cuboid_y1 = 140
cuboid_x2 = 350
cuboid_y2 = 260
cuboid_depth = 50

the_cuboid = Cuboid(cuboid_canvas, cuboid_x1, cuboid_y1, cuboid_x2, cuboid_y2, cuboid_depth)
the_cuboid.draw()

cuboid_width_line = cuboid_canvas.create_line(150, 260, 350, 260, arrow=tk.BOTH)
cuboid_width_text = cuboid_canvas.create_text(250, 270, text="Width")

cuboid_height_line = cuboid_canvas.create_line(350, 140, 350, 255, arrow=tk.BOTH)
cuboid_height_text = cuboid_canvas.create_text(330, 205, text="Height")

cuboid_depth_line = cuboid_canvas.create_line(352, 258, 400, 210, arrow=tk.BOTH)
cuboid_depth_text = cuboid_canvas.create_text(395, 240, text="Depth")

# Frame for cube
cube_canvas = tk.Canvas(shape_container_frame, width=500, height=400)
cube_canvas.grid(row=0, column=1, padx=15, pady=10)
cube_button = tk.Radiobutton(shape_container_frame, text="Cube", indicatoron=False,
                             variable=s, value=current_selections["shapes"]["Cube"],
                             command=cube_selected)
cube_button.grid(row=1, column=1, padx=25, pady=10)
# Cube values
cube_x1 = 200
cube_y1 = 150
cube_x2 = 300
cube_y2 = 250
cube_depth = 50

the_cube = Cube(cube_canvas, cube_x1, cube_y1, cube_x2, cube_y2, cube_depth)
the_cube.draw()

cube_width_line = cube_canvas.create_line(200, 200, 300, 200, arrow=tk.BOTH, fill="black")
cube_width_text = cube_canvas.create_text(250, 190, text="Width", fill="black")

# Frame for cylinder
cylinder_canvas = tk.Canvas(shape_container_frame, width=500, height=400)
cylinder_canvas.grid(row=0, column=2, padx=15, pady=0)
cylinder_button = tk.Radiobutton(shape_container_frame, text="Cylinder", indicatoron=False,
                                 variable=s, value=current_selections["shapes"]["Cylinder"],
                                 command=cylinder_selected)
cylinder_button.grid(row=1, column=2, padx=15, pady=0)

cylinder_back_circle(cylinder_canvas, 300, 50, 400, 150)
circles_between_points(cylinder_canvas, 250, 200, 350, 100, 5)
cylinder_front_circle(cylinder_canvas, 200, 150, 300, 250)
# Top Line
cylinder_lines(cylinder_canvas, 210, 170, 320, 60)
# Middle Lines
cylinder_lines(cylinder_canvas, 255, 150, 355, 50)
cylinder_lines(cylinder_canvas, 280, 160, 385, 60)
cylinder_lines(cylinder_canvas, 295, 180, 395, 80)
cylinder_lines(cylinder_canvas, 300, 200, 400, 100)
# Bottom Line
cylinder_lines(cylinder_canvas, 285, 235, 395, 120)
# Diameter Line
cylinder_diameter_line = cylinder_canvas.create_line(200, 200, 300, 200, arrow=tk.BOTH)
cylinder_diameter_text = cylinder_canvas.create_text(250, 190, text="Diameter", fill="black")
# Length Line
cylinder_length_line = cylinder_canvas.create_line(285, 236, 395, 125, arrow=tk.BOTH)
cylinder_length_text = cylinder_canvas.create_text(355, 190, text="Length", fill="black")

# Dimension entry frame for cube and cuboid
cube_cuboid_entry_frame = tk.Frame(shape_page, width=500, height=400)
cube_cuboid_entry_frame.pack(side="top", pady=25, fill=tk.BOTH, expand=False)
cube_cuboid_entry_label = tk.Label(cube_cuboid_entry_frame, text="Enter present dimensions below")
cube_cuboid_entry_label.pack(side="top", padx=2)
cube_cuboid_bottom_label = tk.Label(cube_cuboid_entry_frame, text="Press 'Continue' to continue")
cube_cuboid_bottom_label.pack(side="bottom", padx=2)

# Dimension entry frame for cylinder
cylinder_entry_frame = tk.Frame(shape_page, width=500, height=400)
cylinder_entry_frame.pack(side="top", pady=25, fill=tk.BOTH, expand=False)
cylinder_entry_label = tk.Label(cylinder_entry_frame, text="Enter present dimensions below")
cylinder_entry_label.pack(side="top", padx=2)
cylinder_bottom_label = tk.Label(cylinder_entry_frame, text="Press 'Continue' to continue")
cylinder_bottom_label.pack(side="bottom", padx=2)

# Entry Boxes for dimensions
height_entry = PlaceholderEntry(
    tk.Entry(cube_cuboid_entry_frame, foreground="gray"),
    "Height (cm)", validate_positive=True
)
height_entry.entry.pack(side="top", padx=2)

width_entry = PlaceholderEntry(
    tk.Entry(cube_cuboid_entry_frame, foreground="gray"),
    "Width (cm)", validate_positive=True
)
width_entry.entry.pack()

depth_entry = PlaceholderEntry(
    tk.Entry(cube_cuboid_entry_frame, foreground="gray"),
    "Depth (cm)", validate_positive=True
)
depth_entry.entry.pack()

length_entry = PlaceholderEntry(
    tk.Entry(cylinder_entry_frame, foreground="gray"),
    "Length (cm)", validate_positive=True
)
length_entry.entry.pack()

diameter_entry = PlaceholderEntry(
    tk.Entry(cylinder_entry_frame, foreground="gray"),
    "Diameter (cm)", validate_positive=True
)
diameter_entry.entry.pack()

side_entry = PlaceholderEntry(
    tk.Entry(cube_cuboid_entry_frame, foreground="gray"),
    "Side (cm)", validate_positive=True
)
side_entry.entry.pack()


# Move to pattern/paper selection page and write shape values to file
def proceed_to_pattern_page():
    try:
        selected_shape = current_selections["shapes"]["selected_shape"]

        entry_instances = []  # List containing the dimension entry instances
        # Using .extend to ensure that the correct entry boxes are checked based on shape choice
        if selected_shape == "Cuboid":
            entry_instances.extend([height_entry, width_entry, depth_entry])
        elif selected_shape == "Cylinder":
            entry_instances.extend([length_entry, diameter_entry])
        elif selected_shape == "Cube":
            entry_instances.extend([side_entry])
        # If an invalid entry is detected, display the popup warning
        for entry_instance in entry_instances:
            if not entry_instance.validate_input():
                messagebox.showerror("Oops!", "That's not ideal. Please enter a positive number!.")
                return
        # Write the chosen shape to file
        with open(filename, "w") as output_file:
            output_file.write("Present Shape: {}\n".format(selected_shape))
            # Write dimensions to file based on which shape is chosen
            if selected_shape == "Cylinder":
                diameter = float(diameter_entry.get())
                length = float(length_entry.get())

                output_file.write("Diameter: {}{}\n".format(diameter, "cm"))
                output_file.write("Length: {}{}\n".format(length, "cm"))

                dimensions = {"diameter": diameter, "length": length}

            elif selected_shape == "Cuboid":
                depth = float(depth_entry.get())
                width = float(width_entry.get())
                height = float(height_entry.get())

                output_file.write("Width: {}{}\n".format(width, "cm"))
                output_file.write("Height: {}{}\n".format(height, "cm"))
                output_file.write("Depth: {}{}\n".format(depth, "cm"))

                dimensions = {"depth": depth, "width": width, "height": height}

            elif selected_shape == "Cube":
                side = float(side_entry.get())
                dimensions = {"side": side}

                output_file.write("Side: {}{}\n".format(side, "cm"))
            # The area is calculated here and written to file, also passed to the paper page for a price calculation
            area = calculate_area(dimensions)
            current_selections["shapes"]["package_area"] = area
            output_file.write(f"Package Net Area: {area:.2f} cm\u00B2\n")
            # {area: .2f} is to write the area to 2 decimal points and keep the system neat

    except (IOError, ValueError):
        print("Error opening or writing to file, or invalid input")

    pattern_page_button.pack_forget()
    extras_button.pack(side="right", padx=20, pady=5)
    update_pattern_colours()  # Updates the colours of the pattern before it loads so that purple is shown as default
    switch_to_page(pattern_page)


pattern_page_button = tk.Button(footer_frame, text="Continue", command=proceed_to_pattern_page)

# End of Shape/Dimensions Page #


# Pattern and Paper Selection Page #
# Variables
selected_paper = tk.StringVar()
c = tk.StringVar()


# Page functions
# Paper and Pattern Colour Selection
def update_pattern_colours():
    pattern_one_canvas.delete("all")  # Clear previous colour before redrawing with the new colour
    pattern_two_canvas.delete("all")
    selected_colour = c.get()

    # Pattern One (Standard Paper)
    canvas_width = 500
    box_size = canvas_width // 5  # Size of each box: 100

    for row in range(5):
        for col in range(5):
            x1 = col * box_size
            y1 = row * box_size
            x2 = x1 + box_size
            y2 = y1 + box_size

            if (row + col) % 2 == 0:
                fill_colour = selected_colour
            else:
                fill_colour = "white"

            pattern_one_canvas.create_rectangle(x1, y1, x2, y2, fill=fill_colour, outline="black")

    # Pattern Two (Premium Paper)
    # Upper Right Squares
    pattern_two_canvas.create_rectangle((250, 250), (500, 0), fill="white", outline="black")
    pattern_two_canvas.create_rectangle((300, 200), (500, 0), fill=selected_colour, outline="black")
    pattern_two_canvas.create_rectangle((350, 150), (500, 0), fill="white", outline="black")
    pattern_two_canvas.create_rectangle((400, 100), (500, 0), fill=selected_colour, outline="black")
    pattern_two_canvas.create_rectangle((450, 50), (500, 0), fill="white", outline="black")
    # Lower Left Squares
    pattern_two_canvas.create_rectangle((0, 500), (250, 250), fill="white", outline="black")
    pattern_two_canvas.create_rectangle((0, 500), (200, 300), fill=selected_colour, outline="black")
    pattern_two_canvas.create_rectangle((0, 500), (150, 350), fill="white", outline="black")
    pattern_two_canvas.create_rectangle((0, 500), (100, 400), fill=selected_colour, outline="black")
    pattern_two_canvas.create_rectangle((0, 500), (50, 450), fill="white", outline="black")
    # Upper Left and Lower Right Squares
    pattern_two_canvas.create_rectangle((0, 250), (250, 0), fill=selected_colour, outline="black")
    pattern_two_canvas.create_rectangle((250, 250), (500, 500), fill=selected_colour, outline="black")


# Function for each paper selected to update the price calculation
def paper_button_selection():
    selected_paper_type = selected_paper.get()
    current_selections["pattern page"]["paper"]["selected_paper"] = selected_paper_type

    # Calculate the price of the paper using the area calculation
    area = current_selections["shapes"]["package_area"]
    price_per_cm = current_selections["pattern page"]["price_per_cm"][selected_paper_type]

    total_price = area * price_per_cm
    price_in_pounds = total_price / 100  # Convert to appear as a decimal for clarity

    # Display the price
    price_display_label.config(text=f"Price: £{price_in_pounds:.2f}")

    update_pattern_colours()

    # Returns the price again for writing to file
    return price_in_pounds


# Update the pattern colour based on which is chosen
def colour_button_selection():
    selected_colour = c.get()
    current_selections["colours"]["selected_colour"] = selected_colour
    update_pattern_colours()


# Pattern page GUI
pattern_page = tk.Frame(main_window)

# Pattern and colour preview container
pattern_container_frame = tk.Frame(pattern_page, width=1500, height=400)
pattern_container_frame.pack(side="top", padx=15, pady=25)
# Standard Paper (Pattern One)
pattern_one_canvas = tk.Canvas(pattern_container_frame, height=500, width=500, background="white")
pattern_one_canvas.grid(row=0, column=0, padx=10, pady=10)
standard_paper_button_one = tk.Radiobutton(pattern_container_frame, text="Standard Paper\n 40p Per cm\u00B2",
                                           indicatoron=False, variable=selected_paper, value="Standard Paper",
                                           command=paper_button_selection)
standard_paper_button_one.grid(row=1, column=0, padx=10, pady=(0, 5))

# Premium Paper (Pattern Two)
pattern_two_canvas = tk.Canvas(pattern_container_frame, height=500, width=500, background="white")
pattern_two_canvas.grid(row=0, column=1, padx=10, pady=10)
premium_paper_button_two = tk.Radiobutton(pattern_container_frame, text="Premium Paper\n 75p Per cm\u00B2",
                                          indicatoron=False, variable=selected_paper, value="Premium Paper",
                                          command=paper_button_selection)
premium_paper_button_two.grid(row=1, column=1, padx=10, pady=(0, 5))

# Container and buttons to update colour selection
colour_buttons_frame = tk.Frame(pattern_page, width=500, height=250)
colour_buttons_frame.pack(side="top", expand=True)
colour_buttons_label = tk.Label(colour_buttons_frame, text="Select a colour to update the preview")
colour_buttons_label.pack(side="top", padx=2)
price_display_label = tk.Label(colour_buttons_frame)
price_display_label.pack(side="bottom")

colour_buttons = []
# Colour buttons take names from the dictionary and pass the hex code to the paper pattern for display
for colour_name, hex_code in current_selections["colours"].items():
    button_frame = tk.Frame(colour_buttons_frame)
    button_frame.pack(side="left", padx=5)

    colour_choice_button = tk.Radiobutton(button_frame, text=colour_name, indicatoron=False, padx=5,
                                          variable=c, value=hex_code, command=update_pattern_colours)
    colour_choice_button.pack()

    colour_choice_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
    colour_buttons.append(colour_choice_button)

    # Setting the default colour displayed to Purple by using the dictionary position
    if colour_name == list(current_selections["colours"].keys())[0]:
        c.set(hex_code)


# Continue to extras page
def proceed_to_extras_page():
    global colour_name
    try:
        output_file = open(filename, "a")

        # Get the selected paper type
        selected_paper_type = selected_paper.get()

        # Get the selected colour hex code
        selected_hex_code = c.get()

        # Find the colour name from the hex code
        colour_name = next(name for name, hex_code in current_selections["colours"].items()
                           if hex_code == selected_hex_code)

        # Get the price as worked out in the paper button selection function
        price_in_pounds = paper_button_selection()

        # Write to file and print for clarity
        output_file.write("Chosen Paper: {}\n".format(selected_paper_type))
        output_file.write(f"Paper Price: £{price_in_pounds:.2f}\n")

        if selected_hex_code is not None:
            output_file.write("Selected colour: {}\n".format(colour_name))
        else:
            print("No colour selected.\n")

        output_file.close()

    except IOError:
        print("Error opening or writing to file")

    extras_button.pack_forget()
    preset_gift_message_frame.pack_forget()
    preset_gift_message_label.pack_forget()
    preset_message_list.pack_forget()
    preset_gift_continue_label.pack_forget()
    custom_message_label.pack_forget()
    custom_message_frame.pack_forget()
    line_one_entry.entry.pack_forget()
    line_two_entry.entry.pack_forget()
    line_three_entry.entry.pack_forget()
    # Start the extras page with no entry or selection frames visible
    order_date_button.pack(side="right", padx=20, pady=5)
    switch_to_page(extras_page)


extras_button = tk.Button(footer_frame, text="Continue", command=proceed_to_extras_page)

# End of Pattern and Paper Selection Page #


# Additional Extras page #
# Extra options variables
gift_bow_var = tk.BooleanVar(value=False)
gift_message_var = tk.IntVar()
custom_message_text = tk.StringVar()


# Extra page functions
def show_preset_message_options():
    # Show preset message options
    preset_gift_message_frame.pack()
    preset_gift_message_label.pack()
    preset_message_list.pack()
    preset_gift_continue_label.pack()
    # Hide custom entry lines
    custom_message_label.pack_forget()
    custom_message_frame.pack_forget()
    line_one_entry.entry.pack_forget()
    line_two_entry.entry.pack_forget()
    line_three_entry.entry.pack_forget()


def show_custom_message_options():
    # Hide the preset message options
    preset_gift_message_frame.pack_forget()
    preset_gift_message_label.pack_forget()
    preset_message_list.pack_forget()
    preset_gift_continue_label.pack_forget()
    # Show custom entry lines
    custom_message_frame.pack()
    custom_message_label.pack()
    custom_message_lower_label.pack()
    line_one_entry.entry.pack()
    line_two_entry.entry.pack()
    line_three_entry.entry.pack()


def get_selected_message_info(listbox):  # Find the selected preset message in the dictionary
    selected__preset_message = listbox.curselection()
    if selected__preset_message:  # If a message is selected
        selected_index = selected__preset_message[0]
        # Find the number of the message that was chosen
        all_message_numbers = list(current_selections["extras"]["gift_messages"]["message"].keys())
        selected_message_number = all_message_numbers[selected_index]

        try:  # Find the same number in the list of prices
            selected_message_cost = current_selections["extras"]["gift_messages"]["cost"][selected_message_number]
        except KeyError:
            selected_message_cost = 0.0  # Assign a default cost if no number key is found
            print("Warning: Message cost not found for index", selected_message_number)

        return selected_message_number, selected_message_cost
    else:
        return None, None  # Return None for both if nothing is selected.


# Function to hold the extra addon choices until writing to file
def update_extras_selections(selection_type):
    current_selections["extras"]["addons"]["gift_bow_selected"] = gift_bow_var.get()

    if selection_type == "preset":
        current_selections["extras"]["addons"]["gift_message_type"] = "Preset"

        selected_option = gift_message_var.get()
        if selected_option == 1:
            selected_message_number, selected_message_cost = get_selected_message_info(preset_message_list)

            current_selections["extras"]["addons"]["preset_message_selected"] = True
            current_selections["extras"]["addons"]["gift_message_index"] = selected_message_number

        else:
            current_selections["extras"]["addons"]["preset_message_selected"] = False

        show_preset_message_options()

    elif selection_type == "custom":
        current_selections["extras"]["addons"]["gift_message_type"] = "Custom"
        current_selections["extras"]["addons"]["preset_message_selected"] = False
        show_custom_message_options()

    else:  # If no tag is selected
        current_selections["extras"]["addons"]["preset_message_selected"] = False

    # Additional Extras Cost Calculation
    # Defining the prices of each extra
    total_cost = 0
    custom_message_cost = 0  # Set to 0 until an entry is made
    gift_tag_price = 0.50
    gift_bow_price = 1.50

    extras = current_selections["extras"]["addons"]

    if extras["gift_bow_selected"]:
        total_cost += gift_bow_price

    gift_message_type = extras["gift_message_type"]
    if gift_message_type in ["preset", "custom"]:  # Only add gift tag cost if preset or custom message are selected
        total_cost += gift_tag_price

    if gift_message_type == "preset" and extras["preset_message_selected"]:
        message_index = extras["gift_message_index"]
        selected_message_cost = current_selections["extras"]["gift_messages"]["cost"][message_index]
        total_cost += selected_message_cost  # Add the cost of the tag and the selected message to the cost
    elif gift_message_type == "custom":
        line_one_text = line_one_entry.entry.get()
        line_two_text = line_two_entry.entry.get()
        line_three_text = line_three_entry.entry.get()  # Get the input for the custom message entry boxes

        total_characters = len(line_one_text) + len(line_two_text) + len(line_three_text)
        custom_message_cost = total_characters * 0.02  # 2p per character
        total_cost += custom_message_cost  # Count total letters and multiply by 2p for each

    return total_cost, custom_message_cost


# Extra page GUI
extras_page = tk.Frame(main_window)

additional_extras_frame = tk.Frame(extras_page, width=1500, height=400)
additional_extras_frame.pack(side="top", padx=15, pady=25)

# Frame for gift bow
gift_bow_canvas = tk.Canvas(additional_extras_frame, width=500, height=400)
gift_bow_canvas.grid(row=0, column=0, padx=15, pady=10)
gift_bow_button = tk.Checkbutton(additional_extras_frame, text="Gift Bow\n £1.50",
                                 indicatoron=False, variable=gift_bow_var,
                                 command=lambda: update_extras_selections("Gift Bow"))

gift_bow_button.grid(row=1, column=0, padx=25, pady=10)

# Bow Drawing
gift_bow_canvas.create_rectangle(0, 200, 500, 250, fill="red", outline="white", width=2)
gift_bow_canvas.create_polygon((180, 120), (120, 180), (380, 275), (320, 335), fill="red", outline="white", width=2)
gift_bow_canvas.create_polygon((320, 120), (380, 180), (120, 275), (180, 335), fill="red", outline="white", width=2)
gift_bow_canvas.create_rectangle(200, 190, 300, 260, fill="red", outline="white", width=2)

# Frame for preset gift message
preset_gift_message_canvas = tk.Canvas(additional_extras_frame, width=500, height=400)
preset_gift_message_canvas.grid(row=0, column=1, padx=15, pady=10)
preset_gift_message_button = tk.Radiobutton(additional_extras_frame, text="Preset Gift Message\n 50p \n 2p per "
                                                                          "character", indicatoron=False,
                                            variable=gift_message_var, value=1,
                                            command=lambda: update_extras_selections("preset"))

preset_gift_message_button.grid(row=1, column=1, padx=25, pady=10)
# Gift tag drawing
preset_gift_message_canvas.create_polygon((300, 30), (350, 30), (400, 80), (400, 130), (200, 395),
                                          (100, 305), (300, 30), fill="red", width=2, outline="white")
preset_gift_message_canvas.create_oval((330, 65), (365, 100), fill="#D4D5E1", outline="white", width=2)

example_text = preset_gift_message_canvas.create_text((240, 225), fill="black", text="Happy Birthday!",
                                                      font=("default", 30))
preset_gift_message_canvas.itemconfig(example_text, angle=52)

# Frame for custom message
custom_message_canvas = tk.Canvas(additional_extras_frame, width=500, height=400)
custom_message_canvas.grid(row=0, column=2, padx=15, pady=0)
custom_message_button = tk.Radiobutton(additional_extras_frame, text="Custom Gift Message\n 2p Per Character",
                                       indicatoron=False, variable=gift_message_var, value=2,
                                       command=lambda: update_extras_selections("custom"))
custom_message_button.grid(row=1, column=2, padx=15, pady=0)

# Custom message tag drawing
custom_message_canvas.create_polygon((300, 30), (350, 30), (400, 80), (400, 130), (200, 395),
                                     (100, 305), (300, 30), fill="red", width=2, outline="white")
custom_message_canvas.create_oval((330, 65), (365, 100), fill="#D4D5E1", outline="white", width=2)

example_text = custom_message_canvas.create_text((240, 225), fill="black", text="Sample Text", font=("default", 30))
custom_message_canvas.itemconfig(example_text, angle=52)
# Selection frame for preset gift messages
preset_gift_message_frame = tk.Frame(extras_page, width=500)
preset_gift_message_frame.pack(side="top", pady=25, fill=tk.BOTH, expand=True)

preset_gift_message_label = tk.Label(preset_gift_message_frame, text="Please select a message below")
preset_gift_message_label.pack(side="top", padx=2)

# List box settings
max_message_length = max(len(str(message)) for message in
                         current_selections["extras"]["gift_messages"]["message"].keys())
# Get the integer key from the dictionary
# Convert the integer into the string of the message
# Calculate the length of the message
# Find the maximum length of messages to adjust the listbox width to fit all messages

average_char_width = 100
listbox_width = average_char_width * max_message_length

preset_message_list = tk.Listbox(preset_gift_message_frame, width=listbox_width)
preset_message_list.pack(fill=tk.BOTH, expand=True)

preset_message_list.config(selectbackground="#6AA3E3", selectforeground="Black")

message_numbers = list(current_selections["extras"]["gift_messages"]["message"].keys())
# .keys is to find the number linked to each message in the dictionary to populate the listbox properly

for message_number in message_numbers:
    message_text = current_selections["extras"]["gift_messages"]["message"][message_number]
    message_cost = current_selections["extras"]["gift_messages"]["cost"][message_number]
    preset_message_list.insert(tk.END, f"{message_text} - £{message_cost:.2f}")

# Listbox selection linking to "gift_message_var"
preset_message_list.bind("<<ListboxSelect>>",  # Access the selected message number when it's returned by the function
                         lambda event: gift_message_var.set(get_selected_message_info(preset_message_list)[0]))

preset_gift_continue_label = tk.Label(preset_gift_message_frame, text="Press 'Continue' to continue")
preset_gift_continue_label.pack(side="bottom", padx=2)

# Frame for custom message entry
custom_message_frame = tk.Frame(extras_page, width=500, height=400)
custom_message_frame.pack(side="top", pady=25, fill=tk.BOTH, expand=False)
custom_message_label = tk.Label(custom_message_frame, text="Enter custom message below")
custom_message_label.pack(side="top", padx=2)
custom_message_lower_label = tk.Label(custom_message_frame, text="Press 'Continue' to continue")
custom_message_lower_label.pack(side="bottom", padx=2)

# Entry Boxes using PlaceholderEntry
# Custom Line Message Entries
line_one_entry = PlaceholderEntry(
    tk.Entry(custom_message_frame, foreground="gray"),
    "Line 1"
)
line_one_entry.entry.pack(side="top", padx=2)

line_two_entry = PlaceholderEntry(
    tk.Entry(custom_message_frame, foreground="gray"),
    "Line 2"
)
line_two_entry.entry.pack()

line_three_entry = PlaceholderEntry(
    tk.Entry(custom_message_frame, foreground="gray"),
    "Line 3"
)
line_three_entry.entry.pack()


def proceed_to_order_date():
    gift_tag_price = 0.50
    gift_bow_price = 1.50

    try:
        output_file = open(filename, "a")

        # Initialize total cost
        total_cost = 0

        # Write Gift Bow Selection
        gift_bow_selected = current_selections["extras"]["addons"]["gift_bow_selected"]
        output_file.write("Gift Bow: {}\n".format("Yes" if gift_bow_selected else "No"))

        # Write the selected gift message type
        gift_message_type = current_selections["extras"]["addons"]["gift_message_type"]
        output_file.write("Gift Message: {}\n".format(gift_message_type))

        # Process Preset Message
        if gift_message_type.lower() == "preset":
            _, selected_message_cost = get_selected_message_info(preset_message_list)

            selected_index = preset_message_list.curselection()
            selected_message = current_selections["extras"]["gift_messages"]["message"][
                selected_index[0]] if selected_index else "None Selected"

            output_file.write("Selected Message: {}\n".format(selected_message))  # Write message to file

            # Include the preset message cost in total cost
            total_cost += selected_message_cost

        # Checks and write to file for custom message
        elif gift_message_type.lower() == "custom":
            output_file.write("Custom Message:\n")
            line_one_text = line_one_entry.entry.get()
            line_two_text = line_two_entry.entry.get()
            line_three_text = line_three_entry.entry.get()

            # Calculate total characters excluding placeholder text
            total_characters = 0
            if line_one_text != line_one_entry.placeholder_text:
                total_characters += len(line_one_text)
            if line_two_text != line_two_entry.placeholder_text:
                total_characters += len(line_two_text)
            if line_three_text != line_three_entry.placeholder_text:
                total_characters += len(line_three_text)
            custom_message_cost = total_characters * 0.02  # 2p per character

            # Write custom message lines to file
            if total_characters:
                if line_one_text != line_one_entry.placeholder_text:
                    output_file.write(f"Message: {line_one_text}\n")
                if line_two_text != line_two_entry.placeholder_text:
                    output_file.write(f"Message Line 2: {line_two_text}\n")
                if line_three_text != line_three_entry.placeholder_text:
                    output_file.write(f"Message Line 3: {line_three_text}\n")

            # Include custom message cost in total cost
            total_cost, _ = update_extras_selections("custom")
            total_cost += custom_message_cost

        # Write Costs to File
        if gift_bow_selected:
            output_file.write(f"Gift Bow Cost: £{gift_bow_price:.2f}\n")

        if gift_message_type.lower() == "preset":
            output_file.write(f"Gift Tag Cost: £{gift_tag_price:.2f}\n")
            output_file.write(f"Message Cost: £{selected_message_cost:.2f}\n")
        elif gift_message_type.lower() == "custom":
            output_file.write(f"Gift Tag Cost: £{gift_tag_price:.2f}\n")
            output_file.write(f"Message Cost: £{custom_message_cost:.2f}\n")

        total_extras_cost = total_cost  # Total extras cost includes all costs

        if gift_bow_selected:
            total_extras_cost += gift_bow_price  # Include gift bow cost
        if gift_message_type.lower() in ["preset", "custom"]:
            total_extras_cost += gift_tag_price  # Include gift tag cost only if a message is selected
        else:
            output_file.write("No Gift Message Selected\n")

        output_file.write(f"Total Extras Cost: £{total_extras_cost:.2f}\n")

        output_file.close()

    except (IOError, PermissionError) as e:
        print("File Error", "Error opening or writing to file: {}".format(e))

    order_date_button.pack_forget()
    complete_order_button.pack(side="right", padx=20, pady=5)
    switch_to_page(order_dates_page)


order_date_button = tk.Button(footer_frame, text="Continue", command=proceed_to_order_date)


# End of Extras Page #


# Order drop off and collection page #
# Calendar Functions #
def days_per_month(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        return 28
    else:
        return 30


# Function above calculates how many days a month has.
# This is needed to know how many radio buttons to create for dates in selected months.


# Functions are set to clear their frames when a button is pressed to avoid issues
def dropoff_month_selection():
    for widget in drop_off_month_frame.winfo_children():
        widget.destroy()

    # Set variables for storage
    selected_month = tk.StringVar()
    dropoff_date_var = tk.IntVar()

    column = 0  # Buttons to display the months
    for month_name, month_num in current_selections["calendar"]["months"].items():
        dropoff_month_button = tk.Radiobutton(drop_off_month_frame, text=month_name, font=("Arial", 20),
                                              variable=selected_month, value=month_name, indicatoron=False,
                                              command=lambda name=month_name, num=month_num: dropoff_day_selection(name,
                                                                                                                   num))
        dropoff_month_button.pack(side="left", padx=10, pady=5)
        dropoff_month_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3", activeforeground="Black")
        column += 1

    def dropoff_day_selection(month_name, month_num):
        for widget in drop_off_day_frame.winfo_children():
            widget.destroy()

        days_in_month = days_per_month(month_num)  # Use the day per month function to find how many days to display

        dropoff_select_date_label = tk.Label(drop_off_day_frame, text=f"Select a date for {month_name}:",
                                             font=("Arial", 15))
        dropoff_select_date_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
        dropoff_select_date_label.pack(side="top")

        buttons_per_row = (days_in_month + 2) // 3  # Divide the day buttons into 3 rows

        dropoff_day_rows_frame = tk.Frame(drop_off_day_frame)
        dropoff_day_rows_frame.config(bg=frame_colours[mode]["bg"])
        dropoff_day_rows_frame.pack()  # Individual frame for each row of buttons

        for row in range(3):
            dropoff_button_row_frame = tk.Frame(dropoff_day_rows_frame)
            dropoff_button_row_frame.config(bg=frame_colours[mode]["bg"])
            dropoff_button_row_frame.pack()  # Individual frames for each button for spacing

            start_day = row * buttons_per_row + 1
            end_day = min(start_day + buttons_per_row - 1, days_in_month)

            for day in range(start_day, end_day + 1):  # Display the days of the month buttons
                dropoff_date_button = tk.Radiobutton(dropoff_button_row_frame, text=str(day),
                                                     font=("Arial", 20), padx=10, pady=5, indicatoron=False,
                                                     variable=dropoff_date_var, value=day,
                                                     command=lambda d=day, m=month_name: dropoff_time_slots(d, m))
                dropoff_date_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3",
                                           activeforeground="Black")
                dropoff_date_button.pack(side="left", padx=5, pady=5)

        def dropoff_time_slots(selected_day, month_name):
            for widget in drop_off_day_frame.winfo_children():
                widget.destroy()

            dropoff_time_label = tk.Label(drop_off_day_frame,
                                          text=f"Available time slots for {month_name} {selected_day}th:",
                                          font=("Arial", 15))
            dropoff_time_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
            dropoff_time_label.pack()

            time_slots = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"]

            for slot in time_slots:
                dropoff_time_slot_button = tk.Button(drop_off_day_frame, text=slot, font=("Arial", 12),
                                                     command=lambda d=selected_day, m=month_name,
                                                     t=slot: completed_dropoff_dates(f"{m} {d} {t}"))
                dropoff_time_slot_button.config(bg="#8BABF1", fg="Black", activebackground="#6AA3E3",
                                                activeforeground="Black")
                dropoff_time_slot_button.pack()


def completed_dropoff_dates(s):  # S for selection
    # Split the input string to extract selected month, day, and time
    selected_month, selected_day, selected_time = s.split()

    # Update current_selections
    current_selections["calendar"]["date_selection"]["dropoff_month"] = selected_month
    current_selections["calendar"]["date_selection"]["dropoff_day"] = selected_day
    current_selections["calendar"]["date_selection"]["dropoff_time"] = selected_time

    try:
        with open(filename, "a") as output_file:
            # Get values from current_selections
            dropoff_month = current_selections["calendar"]["date_selection"].get("dropoff_month", "None")
            dropoff_day = current_selections["calendar"]["date_selection"].get("dropoff_day", "None")

            # Write drop-off date and time to the output file
            output_file.write("Drop Off Date: {} {}\n".format(dropoff_month, dropoff_day))
            output_file.write("Drop Off Time: {}\n".format(selected_time))

    except IOError:
        print("Error opening or writing to file")

    # Hide drop-off-related widgets
    drop_off_label.pack_forget()
    drop_off_month_frame.pack_forget()
    drop_off_day_frame.pack_forget()

    # Show the collection calendar
    collection_label.pack(side="top")
    collection_month_frame.pack(side="top", padx=15, pady=25, fill="both", expand=False, anchor="center")
    collection_day_frame.pack(side="top", padx=15, pady=25, fill="both", expand=False, anchor="center")
    collection_selection()


# Collection Calendar, exactly identical to drop-off calendar but renamed for collection
def collection_selection():
    for widget in collection_month_frame.winfo_children():
        widget.destroy()

    # Set variables for storage
    selected_month = tk.StringVar()
    collection_date_var = tk.IntVar()

    column = 0  # Buttons to display the months
    for month_name, month_num in current_selections["calendar"]["months"].items():
        collection_month_button = tk.Radiobutton(collection_month_frame, text=month_name, font=("Arial", 20),
                                                 variable=selected_month, value=month_name, indicatoron=False,
                                                 command=lambda name=month_name,
                                                 num=month_num: collection_day_selection(name, num))
        collection_month_button.config(bg="#67AC39", fg="Black", activebackground="#345115",
                                       activeforeground="Black", )
        collection_month_button.pack(side="left", padx=10, pady=5)
        column += 1

    def collection_day_selection(month_name, month_num):
        for widget in collection_day_frame.winfo_children():
            widget.destroy()

        days_in_month = days_per_month(month_num)

        collection_day_label = tk.Label(collection_day_frame,
                                        text=f"Select a date for collecting your package - {month_name}:",
                                        font=("Arial", 15))
        collection_day_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
        collection_day_label.pack(side="top")

        buttons_per_row = (days_in_month + 2) // 3  # Divide the buttons into 3 rows

        collection_day_rows_frame = tk.Frame(collection_day_frame)
        collection_day_rows_frame.config(bg=frame_colours[mode]["bg"])
        collection_day_rows_frame.pack()

        for row in range(3):
            collection_button_row_frame = tk.Frame(collection_day_rows_frame)
            collection_button_row_frame.config(bg=frame_colours[mode]["bg"])
            collection_button_row_frame.pack()

            start_day = row * buttons_per_row + 1
            end_day = min(start_day + buttons_per_row - 1, days_in_month)

            for day in range(start_day, end_day + 1):
                collection_date_button = tk.Radiobutton(collection_button_row_frame, text=str(day),
                                                        font=("Arial", 20), padx=10, pady=5, indicatoron=False,
                                                        variable=collection_date_var, value=day,
                                                        command=lambda d=day: collection_time_slots(d))
                collection_date_button.config(bg="#67AC39", fg="Black", activebackground="#345115",
                                              activeforeground="Black", )
                collection_date_button.pack(side="left", padx=5, pady=5)

        def collection_time_slots(selected_day, month_name=selected_month.get()):
            for widget in collection_day_frame.winfo_children():
                widget.destroy()

            collection_time_slots_label = tk.Label(collection_day_frame,
                                                   text=f"Available time slots for {month_name} {selected_day}th:",
                                                   font=("Arial", 15))
            collection_time_slots_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
            collection_time_slots_label.pack()

            time_slots = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"]

            for slot in time_slots:
                collection_time_slot_button = tk.Button(collection_day_frame, text=slot, font=("Arial", 20),
                                                        command=lambda m=month_name, d=selected_day,
                                                        t=slot: completed_collection_dates(f"{m} {d} {t}"))
                collection_time_slot_button.config(bg="#67AC39", fg="Black", activebackground="#345115",
                                                   activeforeground="Black", font=("Arial", 12))
                collection_time_slot_button.pack()


def completed_collection_dates(s):
    # Split the input string to extract selected month, day, and time
    selected_month, selected_day, selected_time = s.split()

    # Update current_selections
    current_selections["calendar"]["date_selection"]["collection_month"] = selected_month
    current_selections["calendar"]["date_selection"]["collection_day"] = selected_day
    current_selections["calendar"]["date_selection"]["collection_time"] = selected_time

    try:
        with open(filename, "a") as output_file:
            # Get values from current_selections
            collection_month = current_selections["calendar"]["date_selection"].get("collection_month", "None")
            collection_day = current_selections["calendar"]["date_selection"].get("collection_day", "None")

            # Write collection date and time to the output file
            output_file.write("Collection Date: {} {}\n".format(collection_month, collection_day))
            output_file.write("Collection Time: {}\n".format(selected_time))

    except IOError:
        print("Error opening or writing to file")

    # Hide collection-related widgets
    collection_label.pack_forget()
    collection_month_frame.pack_forget()
    collection_day_frame.pack_forget()
    complete_order()


order_dates_page = tk.Frame(main_window)

drop_off_label = tk.Label(order_dates_page, text="Please select a month to drop off your package: ", font=("Arial", 15))
drop_off_label.pack(side="top")
drop_off_month_frame = tk.Frame(order_dates_page, width=1500, height=200)  # Starts hidden
drop_off_month_frame.pack(side="top", padx=15, pady=25, fill="both", expand=False, anchor="center")
drop_off_day_frame = tk.Frame(order_dates_page, width=1500, height=245)
drop_off_day_frame.pack(side="top", padx=15, pady=25, fill="both", expand=False, anchor="center")

# Create a frame for the collection
collection_label = tk.Label(order_dates_page, text="Great! Now please select a month to collect your package: ",
                            font=("Arial", 15))
collection_month_frame = tk.Frame(order_dates_page, width=1500, height=200)
collection_day_frame = tk.Frame(order_dates_page, width=1500, height=245)


def complete_order():
    complete_order_button.pack_forget()
    display_summary()
    switch_to_page(summary_page)


complete_order_button = tk.Button(footer_frame, text="Complete order", command=complete_order)


# End of date selection page #


# Order summary page #
def display_summary():
    try:
        with open("order_summary.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        no_file_label = (tk.Label(order_summary_frame, text="Order summary file not found."))
        no_file_label.pack()
        return  # Exit the function if no file found

    # Clear existing content in the frame
    for widget in order_summary_frame.winfo_children():
        widget.destroy()

    row = 0
    total_cost = 0
    custom_message_flag = False
    for line in lines:
        # Split the line into key and value if it contains a colon
        if ": " in line:
            key, value = line.strip().split(": ", 1)
            if key == "Gift Message":
                # Check if the value is "Custom" and set the flag accordingly
                if value == "Custom":
                    custom_message_flag = True
                # Display Custom on the Gift Message line if a custom message is selected
                message_divider_label = (tk.Label(order_summary_frame, text=key + ":"))
                message_divider_label.grid(row=row, column=0, sticky="w")
                message_divider_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
                message_type_label = (tk.Label(order_summary_frame, text=("Custom" if custom_message_flag else value)))
                message_type_label.grid(row=row, column=1, sticky="w")
                message_type_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
                row += 1
            elif key in ['Paper Price', 'Gift Tag Cost', 'Gift Bow Cost', 'Message Cost']:
                # Find the paper cost and add it to the total cost
                cost = float(value.strip('£'))  # Remove the £ symbol and take the value of the line
                total_cost += cost
                # Lines for Paper Price and Additional Extras Costs to combine as total cost
                extras_divider_label = (tk.Label(order_summary_frame, text=key + ":"))
                extras_divider_label.grid(row=row, column=0, sticky="w")
                extras_divider_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
                extras_selected_label = (tk.Label(order_summary_frame, text=value))
                extras_selected_label.grid(row=row, column=1, sticky="w")
                extras_selected_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])

                row += 1
            else:
                # Lines for Shape, Area, Colour, Bow(Y/N), Preset message(if chosen), Extras Cost, Calendar Dates
                calendar_divider_label = (tk.Label(order_summary_frame, text=key + ":", bg=frame_colours[mode]["bg"],
                                                   fg=button_colours[mode]["fg"]))
                calendar_divider_label.grid(row=row, column=0, sticky="w")
                calendar_divider_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
                calendar_selections_label = (tk.Label(order_summary_frame, text=value))
                calendar_selections_label.grid(row=row, column=1, sticky="w")
                calendar_selections_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
                row += 1
                # These lines are grouped together as they have not been specifically selected above
                # The label displays what is left in the file

    # Display the total cost
    total_cost_label = (tk.Label(order_summary_frame, text="Total Cost:"))
    total_cost_label.grid(row=row, column=0, sticky="w")
    total_cost_label.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    total_cost_pounds = (tk.Label(order_summary_frame, text="£{:.2f}".format(total_cost)))
    total_cost_pounds.grid(row=row, column=1, sticky="w")
    total_cost_pounds.config(bg=frame_colours[mode]["bg"], fg=button_colours[mode]["fg"])
    # Display the summary frame
    order_summary_frame.pack(side="top", padx=15, pady=25)

    return total_cost


summary_page = tk.Frame(main_window)

order_summary_label = tk.Label(summary_page, text="Please check your selected options below")
order_summary_label.pack(side="top", anchor="center")
order_summary_frame = tk.Frame(summary_page, width=1500, height=400)
order_summary_frame.pack(side="top")
order_summary_entries = tk.Text(order_summary_frame)
order_summary_entries.pack(side="top")
confirm_order_frame = tk.Frame(summary_page, width=1500, height=100)
confirm_order_frame.pack(side="top", pady=150)
confirm_order_label = tk.Label(confirm_order_frame, text="Please press the button below to confirm your order and "
                                                         "end the program")
confirm_order_label.pack(side="top")


# Closes the window/end the program when the final button is pressed
def end_program():
    total_cost = display_summary()
    with open(filename, "a") as output_file:
        output_file.write("Total Cost: £{:.2f}".format(total_cost))  # Write the total cost to the file
    main_window.destroy()


close_window_button = tk.Button(confirm_order_frame, text="Confirm Order ", command=end_program)
close_window_button.pack(side="bottom", padx=20, pady=5)
previous_page = home_page
current_page = home_page

update_theme()  # Set to follow theme settings when program is run
switch_to_page(home_page)  # Set the home page as the starting page when program is run
dropoff_month_selection()
main_window.mainloop()
