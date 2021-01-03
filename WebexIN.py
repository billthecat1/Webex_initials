import tkinter as tk


def increase():
    value = int(lbl_value['bg'][4:6])
    lbl_value['bg'] = 'gray' + str(value +1)

def decrease():
    value = int(lbl_value['bg'][4:6])
    lbl_value['bg'] = 'gray' + str(value - 1)

def grab_initials():
    pulled = ent_initials.get()
    lbl_value['text'] = pulled

window = tk.Tk()


window.rowconfigure([0, 1, 2], minsize=20, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text='-', command = decrease)
btn_decrease.grid(row=1, column=0, sticky='nsew')
#
# lbl_value = tk.Label(master=window, text=)
# lbl_value.grid(row=0, column=1)
#
btn_increase = tk.Button(master=window, text='+', command = increase)
btn_increase.grid(row=1, column=1, sticky = 'nsew')

b_color = 'gray'



back_color = b_color + str(b_number)

lbl_value = tk.Label(master=window, bg = 'gray78', width =12, height = 6)
lbl_value.configure(font=('Calibri', 32))
lbl_value.grid(row=0, column=3, rowspan=5)


lbl_ligh = tk.Label(master=window, text='Lighter', bg='red')
lbl_ligh.grid(row=0, column = 0, sticky='s')

lbl_dark = tk.Label(master = window, text='Darker')
lbl_dark.grid(row=0, column=1, sticky='s')

lbl_initials = tk.Label(master=window, text = 'Enter your initials')
lbl_initials.grid(row=2, column =0)

ent_initials = tk.Entry(master=window, width =5)
ent_initials.grid(row=2, column =1)

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=grab_initials)
btn_convert.grid(row=2, column =2)



window.mainloop()