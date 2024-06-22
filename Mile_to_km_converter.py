from tkinter import *      #import the all liabrary using the 

def miles_to_km():  #here we define a function to convert the miles to kilometer

    miles = float(miles_input.get())  #taking input and adding into the miles input widget 
    km = miles * 1.609               #formula of miles to Km

    kilometer_result_label.config(text=f"{km}")  #Adding the result into the result label

window = Tk()

window.title("Miles to Kilometer Converter")  # window welcome message 
window.config(padx=50,pady=50)    #window size

miles_input = Entry()    #making it for the input from the user 

miles_input.grid(column= 1, row= 0)  #setting its position using the grid function

miles_label =Label(text= "Miles")
miles_label.grid(column= 2, row= 0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column= 0, row= 1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column= 1, row= 1)

kilometer_label =Label(text="KM")
kilometer_label.grid(column= 2, row= 1)

calculate_button =Button(text="Calcualte", command= miles_to_km)   #creating the final buttion for use to calculate
calculate_button.grid(column= 1, row= 2)






window.mainloop()