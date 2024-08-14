#
# Shawntel Hamilton
# 7/16/24
# Program to calculate grade average and display both the numerical average and associated letter grade
#

import tkinter
import tkinter.messagebox


class GradeCalculator:
    def __init__(self):
        # Create instance of the main window
        self.main_window = tkinter.Tk()

        # Create title of application
        self.main_window.title('Grade Calculator')

        # Set application size
        self.main_window.geometry('260x125')

        # Create five frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create widgets for top frame
        self.top_label = tkinter.Label(self.top_frame, text='Tests Grade: ')
        self.grade_entry = tkinter.Entry(self.top_frame, width=10)

        # Create widgets for middle frame
        self.mid_label = tkinter.Label(self.middle_frame, text='Labs Grade: ')
        self.lab_entry = tkinter.Entry(self.middle_frame, width=10)

        # Create widgets for bottom frame
        self.bot_label = tkinter.Label(self.bottom_frame, text='Exams Grade: ')
        self.exam_entry = tkinter.Entry(self.bottom_frame, width=10)

        # Objects to store a string of blank characters
        self.value = tkinter.StringVar()
        self.letter = tkinter.StringVar()

        # Used to display StringVar objects
        self.average_descr_label = tkinter.Label(self.avg_frame, text='Grade Average: ')
        self.average_label = tkinter.Label(self.avg_frame, textvariable=self.value)
        self.letterGrade_label = tkinter.Label(self.avg_frame, textvariable=self.letter)

        # Pack top frame's widgets
        self.top_label.pack(side='left')
        self.grade_entry.pack(side='left')

        # Pack middle frame's widgets
        self.mid_label.pack(side='left')
        self.lab_entry.pack(side='left')

        # Pack bottom frame's widgets
        self.bot_label.pack(side='left')
        self.exam_entry.pack(side='left')

        # Pack average frame's widgets'
        self.average_descr_label.pack(side='left')
        self.average_label.pack(side='left')
        self.letterGrade_label.pack(side='left')

        # Create widgets for calculate and quit button
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.gradeConverter)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons' widgets
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def gradeConverter(self):
        try:
            # Convert the string value entered by user into a float
            grade = float(self.grade_entry.get())
            lab = float(self.lab_entry.get())
            exam = float(self.exam_entry.get())
            # Calculates the average of the grades
            average = (grade + lab + exam) / 3
            # Determine the grade letter for the average
            if average >= 90:
                letter = '(A)'
            elif average >= 80:
                letter = '(B)'
            elif average >= 70:
                letter = '(C)'
            elif average >= 60:
                letter = '(D)'
            else:
                letter = '(F)'

            # Convert the float average back to string
            average = str(average)
            # Update the average_label
            self.value.set(average)
            # Update the letterGrade_label
            self.letter.set(letter)

        except ValueError:
            # Display error if average cannot be converted to float
            tkinter.messagebox.showinfo('Error', 'One or more grade was not entered correctly.'
                                                 ' Please enter a numerical grade.')


# Create an instance of GradeCalculator class
if __name__ == '__main__':
    my_gui = GradeCalculator()
