from tkinter import *
from functools import partial  # To prevent unwanted windows
import all_constants as c
import conversion_rounding as cr
from datetime import date


class Converter:
    """
    Temperature conversion tool (C to F or Vice versa)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = []

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
                        "one of the buttons to convert it from Celsius to Fahrenheit")
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

        # button list ( button text | bg colour | command | row | column)
        button_details_list = [
            ["To Celsius", "#de1f8b", lambda: self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#0f16f2", lambda: self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / Info", "#16f053", self.to_help, 1, 0],
            ["History / Export", "#af04c9", self.to_history, 1, 1]
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

        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history and export' button and disable it at the start
        self.history_button = self.button_ref_list[3]
        self.history_button.config(state=DISABLED)

    # Check Temperature is valid and either invokes a calculation function or shows a custom error
    def check_temp(self, min_temp):

        # Retrieve temperature to be converted
        to_convert = self.temp_entry.get()

        # reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004c99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_temp}"
        has_errors = "no"

        # checks that amount to be converted is above absolute 0
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp, to_convert)
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
    def convert(self, min_temp, to_convert):

        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert}°C is {answer}°F"
        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert}°F to {answer}°C"

        # enable history export button as soon as a valid calculation is made
        self.history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        """
        Opens help dialogue box and disables help button
        (so that users can't create multiple help boxes)
        :return:
        """
        DisplayHelp(self)

    def to_history(self):
        """
        opens history dialogue box and disables history button
        (so that users can't create multiple windows)
        """

        HistoryExport(self, self.all_calculations_list)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialog box and background colour
        background = "#caffce"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit . . \n\n" \
                    " Note that -273 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible temperature)." \
                    " If you try to convert a temperature that is less " \
                    "than -273 C, you will get an error message. " \
                    "To see your calculation history and export it " \
                    "to a text file, please click the 'History / Export' button."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#16f053",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()

        # disable history button
        partner.history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # background colour and text for calculation area
        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {c.MAX_CALCS} / {len(calculations)}")

        # strings for long labels
        recent_intro_text = (f"Below are {calc_amount} calculations.  "
                             "(shown to the nearest degree)")

        # Create string from circulations list (newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        # Last item added in outside the for loop so that spacing is correct
        if len(newest_first_list) <= c.MAX_CALCS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        # If there are more than five items
        else:
            for item in newest_first_list[:c.MAX_CALCS - 1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.MAX_CALCS - 1]

        export_instructions_txt = ("Please push <Export> to save your calculations "
                                   "in a txt file. If the filename already exists")

        # calculations = ""

        # Label List (Label text / format / bg)
        history_labels_list = [
            ["History /  Export", ("Arial", "16", "bold"), None],
            [recent_intro_text, ("Arial", "11"), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instructions_txt, ("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=10)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # Retrieve export instruction label so that we can configure it to
        # show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons two columns
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        button_ref_list = []

        print("calculations before they are sent", calculations)

        # button list (button text / bg / command / row / column)
        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def export_data(self, calculations):
        # **** Get current date for heading and filename ****
        today = date.today()

        # Get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"temperatures_{year}_{month}_{day}"

        success_string = ("Export Successful! The file is called "
                          f"{file_name}.txt")
        self.export_filename_label.config(fg="#009900", text=success_string,
                                          font=("Arial", "12", "bold"))

        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("**** Temperature Calculations ****\n")
            text_file.write(f"Generated on: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldest to newest). . . \n")

            # write the items to file
            print("calculations", calculations)
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")

    def close_history(self, partner):
        """closes history dialogue box (and enables the button)"""

        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
