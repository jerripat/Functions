# This is a sample Python script that factors a number.
def calculate(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

calculate(13)
#______________________________________________________________________________
# This function creates a dictionary from os.path.join() results.
# It then puts each die ina list then returns the list
def load_dice_images(self):
    """Load dice images into a dictionary."""
    images = {}
    for i in range(1, 7):
        images[i] = PhotoImage(file=os.path.join("images", f"dice-{i}.png"))
    return images
#______________________________________________________________________________

# This function creates a simple menu.
    def create_menu(self):
        """Create a File menu with New Game and Exit options."""
        menu_bar = Menu(self.root)  # Create a menu bar

        # Create a File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Game", command=self.reset_game)  # New Game option
        file_menu.add_separator()  # Add a separator
        file_menu.add_command(label="Exit", command=self.root.quit)  # Exit option

        # Add the File menu to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Configure the root window to use the menu bar
        self.root.config(menu=menu_bar)
#______________________________________________________________________________