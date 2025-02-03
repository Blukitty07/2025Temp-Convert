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

        # Press button to convert input to Celcius
        self.to_celcius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#de1f8b",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.to_celcius_button.grid(row=0, column=0, padx=5, pady=5)

        # Press button to convert input to Farenheit
        self.to_farenheit_button = Button(self.button_frame,
                                        text="To Farenheit",
                                        bg="#0f16f2",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        # Press button to get Help and information
        self.help_button = Button(self.button_frame,
                                        text="Help/Info",
                                        bg="#16f053",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        # Press button to see your recent conversion history and to export them
        self.history_button = Button(self.button_frame,
                                        text="History/Export",
                                        bg="#af04c9",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.history_button.grid(row=1, column=1, padx=5, pady=5)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
