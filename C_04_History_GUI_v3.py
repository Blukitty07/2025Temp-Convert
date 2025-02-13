from tkinter import *
from functools import partial  # to prevent multiple windows
import all_constants as c
from datetime import date


class Converter:
    """
    Temperature conversion tool
    """

    def __init__(self):
        """temperature converter gui"""

        self.all_calculations_list = ['10.0°F to -12°C', '20.0°F to -7°C',
                                      '30.0°F to -1°C', '40.0°F to 4°C',
                                      '50.0°F to 10°C', "test_file"]

        self.button_frame = Frame(padx=10, pady=10)
        self.button_frame.grid()

        self.history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#af04c9",
                                        fg="#FFFFFF",
                                        font=("Arial", "12", "bold"),
                                        width=12, command=self.to_history)
        self.history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        opens history dialogue box and disables history button
        (so that users can't create multiple windows)
        """

        HistoryExport(self, self.all_calculations_list)


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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
