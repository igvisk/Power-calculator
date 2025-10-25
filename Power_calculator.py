import tkinter as tk
from tkinter import ttk                                      #Tk themed widgets (ttk)
import math

version = "1.0"

def calculate_power():
    try:
        current = float(entry_current.get().replace(',', '.'))                        #get data from input + ochrana pred zadanim "," pri float
        voltage = float(entry_voltage.get().replace(',', '.'))
        power_factor = float(entry_pf.get().replace(',', '.'))
        phases = int(combo_phase.get())

        sin_phi = math.sqrt(1 - power_factor**2)

        if phases == 1:
            apparent_power = voltage * current
            active_power = apparent_power * power_factor
            reactive_power = apparent_power * sin_phi
        elif phases == 2:                                                               # Medzifázové jednofazove zapojenie v Európe - 2 fázy = medzi dvoma fázami (napr. L1–L2), 400 V bez nulového vodiča
            apparent_power = voltage * current
            active_power = apparent_power * power_factor
            reactive_power = apparent_power * math.sqrt(1 - power_factor**2)
        elif phases == 3:
            apparent_power = math.sqrt(3) * voltage * current
            active_power = apparent_power * power_factor
            reactive_power = apparent_power * sin_phi
        

        label_result.config(text=(
            f"✅ Činný výkon (P): {active_power:.2f} kW\n"                              #var:.2f -zaokruhli variable na 2 desatinne miesta
            f"⚡ Zdanlivý výkon (S): {apparent_power:.2f} kVA\n"
            f"🔄 Jalový výkon (Q): {reactive_power:.2f} kVAr"
        ))
    except ValueError:
        label_result.config(text="❌ Zadaj platné číselné hodnoty.")

# GUI setup
window = tk.Tk()
window.title(f"Kalkulačka výkonu {version}")

#Rozmery okna a vypocet pozicie na stred obrazovky /pre kazde rozlisenie/
    #Rozmery okna
window_width = 228
window_height = 230
    # Ziska rozlisenie obrazovky
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
    # Vypocet pozicie okna na stred obrazovky
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
    # Nastavenie pozicie okna a veľkosť okna
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


#ttk stylovanie:
style = ttk.Style()
style.theme_use("default")                                                              # alebo "clam"-najviac customizovatelne, "alt", "classic", "default"

font_global = "Segoe UI"
    #input ttk styl:
style.configure("My.TEntry",
    font=(font_global, 10),
    padding=4
)
    #combobox - roletka ttk styl
style.configure("My.TCombobox",
    font=(font_global, 10),
    padding=4,
    foreground="#333",     # farba textu
    background="white"     # farba pozadia (len pre niektoré témy)
)
    #button ttk styl
style.configure("My.TButton",
    font=(font_global, 10, "bold"),
    foreground="black",
    background="#6C7A23",  
    padding=6
)

    #label ttk styl
style.configure("My.TLabel",
    font=(font_global, 10),
    foreground="#333"
)



    # inputs:
ttk.Label(window, text="Prúd (A):").grid(column=0, row=0, sticky="w")
entry_current = ttk.Entry(window, style="My.TEntry")                                #entry (okno, ttk_styl)
entry_current.insert(0, 16)
entry_current.grid(column=1, row=0)


ttk.Label(window, text="Napätie (V):").grid(column=0, row=1, sticky="w")
entry_voltage = ttk.Entry(window, style="My.TEntry")
entry_voltage.insert(0, 230)
entry_voltage.grid(column=1, row=1)

ttk.Label(window, text="Účinník (cos φ):").grid(column=0, row=2, sticky="w")
entry_pf = ttk.Entry(window, style="My.TEntry")
entry_pf.insert(0, 0.9)
entry_pf.grid(column=1, row=2)

    #Combobox - roletka s options
ttk.Label(window, text="Počet fáz:").grid(column=0, row=3, sticky="w")
combo_phase = ttk.Combobox(window, values=["1", "2", "3"], state="readonly", style="My.TCombobox")
combo_phase.set("3")
combo_phase.grid(column=1, row=3)
    
    #Button
ttk.Button(window, text="Vypočítať výkon", style="My.TButton", command=calculate_power).grid(column=0, row=4, columnspan=2, pady=10)

    #Label vysledky
label_result = ttk.Label(window, text="", justify="left", style="My.TLabel")
label_result.grid(column=0, row=5, columnspan=2)

#Mainloop
window.mainloop()
