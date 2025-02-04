from tkinter import *
import all_constants as c


class Converter:
    """
    Temperature conversion tool (C to F or Vice versa)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        # set up gui frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        # Application Heading
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        # instructions at the top of the page
        instructions = ("Please enter a temperature below and then press "
                        "one of the buttons to convert it from Celcius to Fahrenheit")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        # entry box to input the number you wish to convert
        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # error message that will pop up when the input is invalid
        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#004c99", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list ( button text | bg colour | command | row | coloum)
        button_details_list = [
            ["To Celsius", "#de1f8b", lambda: self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#0f16f2", lambda: self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / Info", "#16f053", "", 1, 0],
            ["History / Export", "#af04c9", "", 1, 1]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history and export' button and disable it at the start
        self.history_button = self.button_ref_list[3].config(state=DISABLED)

    # Check Temperature is valid and either invokes a calculation function or shows a custom error
    def check_temp(self, min_temp):
        print("Min Temp: ", min_temp)

        # Retrieve temperature to be converted
        to_convert = self.temp_entry.get()
        print("to convert", to_convert)

        # reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004c99")
        self.temp_entry.config(bg="#FFFFFF")

        # checks that amount to be converted is above absolute 0
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp)
            else:
                error = "Too Low"

        except ValueError:
            print("Please enter a number!")

        # display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

# alerts to what it is being converted to
    def convert(self, min_temp):

        if min_temp == c.ABS_ZERO_CELSIUS:
            self.answer_error.config(text="Converting to F")
        else:
            self.answer_error.config(text="Converting to C")

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
