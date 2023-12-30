import tkinter

window = tkinter.Tk()
window.title("BMI QUİZ")
window.config(padx=30, pady=30)

def hesapla():
    weight = entry_weight.get()
    height = entry_height.get()

    if weight.isdigit() or height.isdigit():
        bmi = (float(weight)/((int(height)/100)**2))
        if(bmi < 18.5):
            bilgi_label = tkinter.Label(text=f"Çok zayıfsınız. Vücut kilo indeksiniz : {bmi}", font=('Arial', 15))
        elif(bmi>= 18.5 and bmi<24.9):
            bilgi_label = tkinter.Label(text=f"Zayıfsınız. Vücut kilo indeksiniz : {bmi}", font=('Arial', 15))
        elif(bmi >= 24.9 and bmi<29.9):
            bilgi_label = tkinter.Label(text=f"Normal kilodasınız. Vücut kilo indeksiniz : {bmi}", font=('Arial', 15))
        elif(bmi >= 29.9 and bmi<34.9):
            bilgi_label = tkinter.Label(text=f"Hafif obezsiniz. Vücut kilo indeksiniz : {bmi}", font=('Arial', 15))
        else:
            bilgi_label = tkinter.Label(text=f"Ağır obezsiniz. Vücut kilo indeksiniz : {bmi}", font=('Arial', 15))
        bilgi_label.pack()
    else:
        uyarı_label = tkinter.Label(text="Lütfen geçerli bir işlem girin !!", font=('Arial', 15))
        uyarı_label.pack()

weight_label = tkinter.Label(text="Lütfen kilonuzu girin (kg) : ", font=('Arial', 15))
weight_label.pack(side="top")

entry_weight = tkinter.Entry(width=20)
entry_weight.pack()

height_label = tkinter.Label(text="Lütfen boyunuzu girin (cm) : ", font=('Arial', 15))
height_label.pack(side="top")

entry_height = tkinter.Entry(width=20)
entry_height.pack()

button = tkinter.Button(text="Hesapla", command=hesapla)
button.pack()

window.mainloop()