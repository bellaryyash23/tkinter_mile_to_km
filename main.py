from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=150)
window.config(padx=70, pady=25)

mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

label_mile = Label(text="Miles")
label_mile.grid(row=0, column=2)

label_equal = Label(text="is equal to:")
label_equal.grid(row=1, column=0)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

label_answer = Label(text="0")
label_answer.grid(row=1, column=1)


def convert_mile_to_km():
    mile = float(mile_input.get())
    km_value = round((mile * 1.60934), 2)
    label_answer.config(text=f"{km_value}")


button = Button(text="Calculate", command=convert_mile_to_km)
button.grid(row=2, column=1)

window.mainloop()
