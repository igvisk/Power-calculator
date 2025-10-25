# import tkinter as tk
from tkinter import *
from tkinter import ttk                                      #Tk themed widgets (ttk)
import math

version = "v1.2a"

def calculate_power():
    try:
        current = float(entry_current.get().replace(',', '.'))                        #get data from input + ochrana pred zadanim "," pri float
        voltage = float(entry_voltage.get().replace(',', '.'))
        power_factor = float(entry_pf.get().replace(',', '.'))
        phases = int(combo_phase.get())

        sin_phi = math.sqrt(1 - power_factor**2)

        if phases == 1:
            if voltage not in range(220, 241):                                          #ochrana pri zadani netypickeho napatial, zmeni sa styl entry okna tak aby upozornil uzivatela
                entry_voltage.configure(style="Error.TEntry")
            else:
                entry_voltage.configure(style="My.TEntry")
                
            apparent_power = voltage * current
            active_power = apparent_power * power_factor
            reactive_power = apparent_power * sin_phi
        
        elif phases == 2:                                                               # Medzifázové jednofazove zapojenie v Európe - 2 fázy = medzi dvoma fázami (napr. L1–L2), 400 V bez nulového vodiča
            entry_voltage.delete(0, tk.END)                                             # vymaže obsah vstupu
            entry_voltage.insert(0, 400)
            voltage = float(entry_voltage.get().replace(',', '.'))                      #nacitanie hodnoty 400 ktora vznikne pri L1,L2 (nemoze byt zadane 230V)
            apparent_power = math.sqrt(3) * voltage * current
            active_power = apparent_power * power_factor
            reactive_power = apparent_power * math.sqrt(1 - power_factor**2)
        
        elif phases == 3:                                                          
            if not (210 <= voltage <=250):                                              # if voltage not in range(210, 251): #ochrana pri zadani netypickeho napatial, zmeni sa styl entry okna tak aby upozornil uzivatela
                entry_voltage.configure(style="Error.TEntry")
            else:
                entry_voltage.configure(style="My.TEntry")

            apparent_power = math.sqrt(3) * voltage * current
            active_power = apparent_power * power_factor
            reactive_power = apparent_power * sin_phi
        

        label_result.config(text=(
            f"Činný výkon (P):     {active_power:.2f}  kW\n"                             #var:.2f -zaokruhli variable na 2 desatinne miesta #✅ 
            f"Zdanlivý výkon (S): {apparent_power:.2f} kVA\n"                            #⚡  
            f"Jalový výkon (Q):    {reactive_power:.2f} kVAr"                            #🔄 
        ))
    except ValueError:
        label_result.config(text="❌ Zadaj platné číselné hodnoty.")

# GUI setup
window = Tk()
window.title(f"Výkon {version}")
window.resizable(False,False)

#Rozmery okna a vypocet pozicie na stred obrazovky /pre kazde rozlisenie/
    #Rozmery okna
window_width = 250
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
#Colors and fonts
color_background = "#1778F2"               #origin gray
color_foreground = "#F0F2F5"               #origin white
color_input_bg = "#14B898"                 #origin "#8CA63F" -zelena

font_global = "Helvetica Neue"                      #origin "Segoe UI", "Helvetica Neue", "Roboto"


window.configure(background= color_background)
style = ttk.Style()
style.theme_use("clam")                                                              # pouziva sa ak nieje stanovene background "clam"-najviac customizovatelne, "alt", "classic", "default"


    #input okno ttk styl:
style.configure("My.TEntry",
    font=(font_global, 10),
    foreground= "black",
    fieldbackground= color_input_bg,    
    padding=4
)

    #input okno ttk styl -nevhodny vstup zmena vzhladu:
style.configure("Error.TEntry",
    font=(font_global, 10),
    foreground="black",
    fieldbackground="#FF2A00",  # svetločervené pozadie
    padding=4
)
 
    #combobox - roletka ttk styl
style.configure("My.TCombobox",
    font=(font_global, 10),
    padding=4,
    foreground= "black",                 # farba textu
    background= "#14B898",                   # farba znaku rolletky (len pre niektoré témy)
    # fieldbackground= 'green'
)
    #button ttk styl - pouziva sa style map
style.configure("My.TButton",
    font=(font_global, 8, "bold"),
    padding=6
)

style.map("My.TButton",
    background=[
        ("active", color_input_bg),         # farba pri hovernutí "#8CA63F"
        ("!disabled", color_background)
    ],
    foreground=[
        ("active", "black"),
        ("!disabled", color_foreground)
    ]
)
    #input-label ttk styl
style.configure("My.TLabel",
    font=(font_global, 10),
    foreground= color_foreground,
    background= color_background
)

    #output-label ttk styl
style.configure("MyOutput.TLabel",
    font=(font_global, 10, "bold"),
    foreground= color_foreground,
    background= color_background
)


# Labels + Entries - inputs okienka:
ttk.Label(window, text="Prúd (A):", style="My.TLabel").grid(column=0, row=0, sticky="w")            # Label!
entry_current = ttk.Entry(window, justify="center", style="My.TEntry")                                                # Entry (okno, ttk_styl)!
entry_current.insert(0, 16)                                                                         # default value
entry_current.grid(column=1, row=0)


ttk.Label(window, text="Napätie (V/ph):", style="My.TLabel").grid(column=0, row=1, sticky="w")
entry_voltage = ttk.Entry(window, justify="center", style="My.TEntry")
entry_voltage.insert(0, 230)
entry_voltage.grid(column=1, row=1)

ttk.Label(window, text="Účinník (cos φ):", style="My.TLabel").grid(column=0, row=2, sticky="w")
entry_pf = ttk.Entry(window, justify="center", style="My.TEntry")
entry_pf.insert(0, 0.9)
entry_pf.grid(column=1, row=2)

    #Combobox - roletka s options
ttk.Label(window, text="Počet fáz:", style="My.TLabel").grid(column=0, row=3, sticky="w")
combo_phase = ttk.Combobox(window, values=["1", "2", "3"], state="readonly", style="My.TCombobox")
combo_phase.set("3")
combo_phase.grid(column=1, row=3)
    
    #Button
ttk.Button(window, text="Vypočítať výkon", style="My.TButton", command=calculate_power).grid(column=0, row=4, columnspan=2, pady=10)

    #Label-Output, vysledky
label_result = ttk.Label(window, text="", justify="left", style="MyOutput.TLabel")
label_result.grid(column=0, row=5, columnspan=2)

#Menu
#Menu funkcie
def quit_app():
    window.quit()

def show_about():
    about_window = Tk()
    about_window.title('About')
    # about_window.iconbitmap(ico_path)                 dopln ikonu
    #Rozmery okna a vypocet pozicie na stred obrazovky /pre kazde rozlisenie/
    #Rozmery okna
    about_window_width = 200
    about_window_height = 120
    # Ziska rozlisenie obrazovky
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Vypocet pozicie okna na stred obrazovky
    x = (screen_width // 2) - (about_window_width // 2)
    y = (screen_height // 2) - (about_window_height // 2)
    # Nastavenie pozicie okna a veľkosť okna
    about_window.geometry(f"{about_window_width}x{about_window_height}+{x}+{y}")

    
    
    
    about_window.resizable(False,False)
    about_window.config(bg= color_background)
    about_window_label = Label(about_window, text=
    f"Aplikácia: Výkon\n"
    f"Verzia: {version}\n"
    f"\n\nAutor:     Igor Vitovský\n"
    f"e-mail:    igvisk.pro@gmail.com\n"
    f"GitHub:  github.com/igvisk\n"
    f"Copyright © 2025 Igor Vitovský", 
    bg=color_background, 
    fg="white", justify=LEFT,
    font=(font_global, 10), 
    )
    about_window_label.grid()
    about_window.bind("<Escape>", lambda e: about_window.destroy())                   #shortcut - ESC - close about_window       

  
# Vytvorenie hlavného menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# --- 1 Súbor ---
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nový výpočet  Ctrl+N", command=calculate_power)          #Stlacenie vypoctu -funkcia distance
file_menu.add_separator()
file_menu.add_command(label="Ukončiť             Ctrl+Q", command=window.quit)
menu_bar.add_cascade(label="Súbor", menu=file_menu)

# --- 2 Help/Pomocník ---
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="O programe  F1", command=show_about)          
menu_bar.add_cascade(label="Pomoc", menu=help_menu)

# --- Klávesové skratky (bind) ---
window.bind("<Control-n>", lambda event: calculate_power())                # .bind("<Key-combination>", lambda event: run_function())
window.bind("<Control-q>", lambda event: quit_app())
window.bind("<F1>", lambda event: show_about())








#Mainloop
window.mainloop()


# Do helpu:

# ⚡ Čo je účinník (cos φ)?
# - Účinník vyjadruje, aký podiel z celkového výkonu je „činný“ (užitočný).
# - Hodnota je medzi 0 a 1:
# - 1.0 = ideálny stav (čisto činný výkon, žiadna jalová zložka)
# - 0.9 – 0.95 = bežné hodnoty pre moderné spotrebiče
# - 0.8 – 0.9 = staršie motory, transformátory
# - < 0.8 = výrazne induktívne alebo kapacitné zariadenia

# ✅ Odporúčané hodnoty podľa typu záťaže

# Typ záťaže                   Príklad zariadenia          Typický účinník
# Rezistívna (čistá)           Žiarovky, ohrievače         1.0
# Induktívna (motorická)       Elektromotory, kompresory   0.8 – 0.95
# Kapacitná (kompenzácia)      Kondenzátorové batérie      >1.0 (teoreticky)
# Zmiešaná (reálna prevádzka)  Domáce spotrebiče, PC, LED  0.9 – 0.98