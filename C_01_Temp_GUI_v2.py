from tkinter import *


class Converter:
    """
    Temperature conversion tool (C to F or Vice versa)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

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
        self.temp_error = Label(self.temp_frame, text=error,
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list ( button text | bg colour | command | row | coloum)
        button_details_list = [
            ["To Celcius", "#de1f8b", "", 0, 0],
            ["To Farenheit", "#0f16f2", "", 0, 1],
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


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
