import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

# Función para hacer web scraping
def scrape_website():
    url = url_entry.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Aquí puedes personalizar qué datos extraer
    titles = soup.find_all('h1')
    result_text = "\n".join([title.get_text() for title in titles])

    # Mostrar resultados en la interfaz gráfica
    result_label.config(text=result_text)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Web Scraping con Python")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(mainframe, text="Ingresa la URL:")
url_label.grid(column=1, row=1, sticky=tk.W)

url_entry = ttk.Entry(mainframe, width=50)
url_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

scrape_button = ttk.Button(mainframe, text="Iniciar", command=scrape_website)
scrape_button.grid(column=3, row=1, sticky=tk.W)

result_label = ttk.Label(mainframe, text="", wraplength=400)
result_label.grid(column=1, row=2, columnspan=3, sticky=tk.W)

root.mainloop()
