from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
miles = Label(text="Miles", font=("Arial", 16, "bold"))
miles.grid(column=2, row=0)
is_equal = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal.grid(column=0, row=1)
value = Label(text="", font=("Arial", 16, "bold"))
value.grid(column=1, row=1)
km = Label(text="Km", font=("Arial", 16, "bold"))
km.grid(column=2, row=1)


def mile_to_km():
    mile = float(input_mile.get())
    value.config(text=round(mile * 1.609, 2))


input_mile = Entry()
input_mile.grid(column=1, row=0)
get = Button(text="convert", command=mile_to_km)
get.grid(column=1, row=2)

window.mainloop()
