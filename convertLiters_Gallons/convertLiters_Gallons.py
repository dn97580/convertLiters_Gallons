# This program converts liters to gallons.
# The result is displayed in a label on the main window
import tkinter

class LiterConverterGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter liters: ')
        self.liters_entry = tkinter.Entry(self.top_frame, width = 10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side = 'left')
        self.liters_entry.pack(side = 'left')

        # Create the widgets for the middle frame.
        self.descr_label = tkinter.Label(self.mid_frame, text = 'Converted to gallons: ')
        
        # We need a StringVar object to asociate with 
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        # Create a label and ascociate it with the
        # StringVar object. Any value stored in the 
        # StringVar object will automatically be displayed 
        # in the label.
        self.gallons_label = tkinter.Label(self.mid_frame, textvariable = self.value)

        # Pack the middle frame's widgets.
        self.descr_label.pack(side = 'left')
        self.gallons_label.pack(side = 'left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)


        # Pack the buttons.
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.
    def convert(self):
        # Get the value entered by the user into the
        # kilo_entry widget.
        liters = float(self.liters_entry.get())

        # Convert kilometers to miles.
        gallons = liters * 0.264172

        # Convert gallons to a string and store it
        # in the StringVar object. This will automatically
        # update the miles_label widget.
        self.value.set(gallons)

# Create an instance of the KiloConverterGUI class.
if __name__ == '__main__':
    liter_conv = LiterConverterGUI()





