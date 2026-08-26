import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2

# Funciones de las Fases
def show_black_image():
    # Actividad 1: Crear imagen en negro
    img = np.zeros((100, 100))
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(img, cmap='gray', vmin=0, vmax=255)
    ax.set_title("Imagen Negra")
    
    top = tk.Toplevel(root)
    top.title("Fase 1: Actividad 1")
    top.configure(bg='#F0F4F8')
    
    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    frame = tk.Frame(top, bg='#F0F4F8')
    frame.pack(pady=10, padx=20, fill='x')
    
    tk.Label(frame, text="Concepto: Una imagen es una matriz de valores.", font=('Segoe UI', 10, 'italic'), bg='#F0F4F8').pack()
    tk.Label(frame, text="Pregunta: ¿Qué representa el valor 0 en la imagen?", font=('Segoe UI', 11, 'bold'), bg='#F0F4F8').pack(pady=10)
    
    respuesta = "El valor 0 representa el nivel mínimo de intensidad de luz, es decir, el color negro absoluto (ausencia de luz)."
    ttk.Button(frame, text="💡 Ver Respuesta", command=lambda: messagebox.showinfo("Respuesta", respuesta)).pack()

def show_gradient(use_i=False):
    # Actividad 2: Gradiente
    img = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            if use_i:
                img[i, j] = i
            else:
                img[i, j] = j
                
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(img, cmap='gray')
    title = "Gradiente Vertical (usando i)" if use_i else "Gradiente Horizontal (usando j)"
    ax.set_title(title)
    
    top = tk.Toplevel(root)
    top.title("Fase 2: Actividad 2")
    top.configure(bg='#F0F4F8')
    
    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    frame = tk.Frame(top, bg='#F0F4F8')
    frame.pack(pady=10, padx=20, fill='x')
    
    if not use_i:
        tk.Label(frame, text="Análisis:", font=('Segoe UI', 11, 'bold'), bg='#F0F4F8').pack(anchor='w')
        tk.Label(frame, text="• ¿Por qué cambia la intensidad?\n• ¿Qué pasa si usamos 'i' en lugar de 'j'?", justify='left', bg='#F0F4F8', font=('Segoe UI', 10)).pack(anchor='w', pady=5)
        
        respuestas = (
            "1. Cambia la intensidad porque los valores numéricos aumentan progresivamente (de 0 a 99), "
            "lo que se traduce visualmente en un cambio desde el negro hacia colores más claros (grises/blanco).\n\n"
            "2. Si usamos 'i' (filas) en lugar de 'j' (columnas), el gradiente se aplicará verticalmente "
            "(el valor cambiará de arriba hacia abajo en lugar de izquierda a derecha)."
        )
        
        btn_frame = tk.Frame(frame, bg='#F0F4F8')
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="💡 Ver Respuestas", command=lambda: messagebox.showinfo("Análisis", respuestas)).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="▶️ Probar con 'i'", command=lambda: show_gradient(use_i=True)).pack(side='left', padx=5)

def show_math_pattern(div=10):
    # Fase 3: Patrones matemáticos
    img = np.zeros((200, 200))
    for x in range(200):
        for y in range(200):
            img[x, y] = np.sin(x/div) + np.cos(y/div)
            
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(img, cmap='gray')
    ax.set_title(f"Patrón Ondulatorio (Div={div})")
    
    top = tk.Toplevel(root)
    top.title("Fase 3: Patrones matemáticos")
    top.configure(bg='#F0F4F8')
    
    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    frame = tk.Frame(top, bg='#F0F4F8')
    frame.pack(pady=10, padx=20, fill='x')
    
    tk.Label(frame, text="Objetivo: Entender cómo funciones matemáticas generan imágenes.", font=('Segoe UI', 10, 'italic'), bg='#F0F4F8', wraplength=350).pack()
    tk.Label(frame, text="Tarea: Modificar la frecuencia cambiando /10 por /5", font=('Segoe UI', 11, 'bold'), bg='#F0F4F8').pack(pady=10)
    
    btn_frame = tk.Frame(frame, bg='#F0F4F8')
    btn_frame.pack(pady=5)
    
    ttk.Button(btn_frame, text="▶️ Probar con /10", command=lambda: [top.destroy(), show_math_pattern(div=10)]).pack(side='left', padx=5)
    ttk.Button(btn_frame, text="▶️ Probar con /5", command=lambda: [top.destroy(), show_math_pattern(div=5)]).pack(side='left', padx=5)

def show_rgb_image():
    # Fase 4: Imágenes en color 
    img = np.zeros((200, 200, 3))
    for i in range(200):
        for j in range(200):
            img[i, j, 0] = i / 200  # rojo
            img[i, j, 1] = j / 200  # verde
            img[i, j, 2] = 0.5      # azul fijo
            
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(img)
    ax.set_title("Imagen RGB")
    
    top = tk.Toplevel(root)
    top.title("Fase 4: Imágenes en color")
    top.configure(bg='#F0F4F8')
    
    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    frame = tk.Frame(top, bg='#F0F4F8')
    frame.pack(pady=10, padx=20, fill='x')
    
    tk.Label(frame, text="Pregunta: ¿Qué pasa si cambias el canal azul?", font=('Segoe UI', 11, 'bold'), bg='#F0F4F8').pack(pady=10)
    
    respuesta = "El componente azul de todos los píxeles cambiará uniformemente. Si lo subes a 1.0, la imagen será más azulada/clara; si lo bajas a 0.0, el azul desaparecerá y verás tonos más amarillos (combinación de rojo y verde)."
    ttk.Button(frame, text="💡 Ver Respuesta", command=lambda: messagebox.showinfo("Respuesta", respuesta)).pack()

def show_opencv_shapes():
    # Fase 5: Generación con OpenCV
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    # Dibujar círculo
    cv2.circle(img, (150,150), 50, (255,0,0), -1)
    # Dibujar rectángulo
    cv2.rectangle(img, (50,50), (100,100), (0,255,0), -1)
    
    messagebox.showinfo("OpenCV", "Se abrirá una ventana de OpenCV. Presiona cualquier tecla en esa ventana para cerrarla.")
    
    cv2.imshow("Imagen Generada", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    top = tk.Toplevel(root)
    top.title("Fase 5: Generación con OpenCV")
    top.configure(bg='#F0F4F8')
    top.geometry("350x150")
    
    frame = tk.Frame(top, bg='#F0F4F8')
    frame.pack(expand=True, fill='both', padx=20, pady=20)
    
    tk.Label(frame, text="Objetivo: Comprender generación basada en primitivas gráficas.", font=('Segoe UI', 10, 'italic'), bg='#F0F4F8', wraplength=300).pack()

def show_final_challenge():
    # Fase 6: final
    # Desafío grupal: Crear una imagen que combine gradiente, patrón matemático, al menos una figura
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    # Gradiente + patrón matemático
    for x in range(300):
        for y in range(300):
            # Gradiente azul
            b = int((x / 300) * 255)
            # Patrón en verde
            g = int(abs(np.sin(x/20) + np.cos(y/20)) * 127)
            img[x, y] = [b, g, 50]
            
    # Figura: Círculo rojo en el centro
    cv2.circle(img, (150, 150), 60, (0, 0, 255), -1)
    
    # Usar matplotlib para mostrar
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(img_rgb)
    ax.set_title("Desafío Final")
    
    top = tk.Toplevel(root)
    top.title("Fase 6: Desafío Final")
    top.configure(bg='#F0F4F8')
    
    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
    
    frame = tk.Frame(top, bg='#F0F4F8')
    frame.pack(pady=10, padx=20, fill='x')
    
    txt = ("Desafío grupal:\n"
           "Crear una imagen que combine:\n"
           "✔ Gradiente\n"
           "✔ Patrón matemático\n"
           "✔ Al menos una figura\n\n"
           "¡Este es un ejemplo generado por código!")
    tk.Label(frame, text=txt, font=('Segoe UI', 10), bg='#F0F4F8', justify='left').pack(anchor='w')

# Configuración de la ventana principal con diseño profesional
root = tk.Tk()
root.title("Taller 2: Imágenes y Matrices")
root.geometry("500x550")
root.configure(bg='#2C3E50') # Color de fondo oscuro y elegante

# Estilo para ttk buttons
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Segoe UI', 11), padding=6, background='#34495E', foreground='white')
style.map('TButton', background=[('active', '#415B76')])

header_frame = tk.Frame(root, bg='#2C3E50')
header_frame.pack(pady=(20, 10))

tk.Label(header_frame, text="TALLER 2", font=('Segoe UI', 22, 'bold'), fg='#ECF0F1', bg='#2C3E50').pack()
tk.Label(header_frame, text="Procesamiento de Imágenes Interactivo", font=('Segoe UI', 12, 'italic'), fg='#BDC3C7', bg='#2C3E50').pack()

buttons_frame = tk.Frame(root, bg='#2C3E50')
buttons_frame.pack(fill='both', expand=True, padx=40)

def create_menu_button(parent, text, command):
    btn = tk.Button(parent, text=text, font=('Segoe UI', 12, 'bold'), bg='#E74C3C', fg='white', 
                    activebackground='#C0392B', activeforeground='white',
                    relief='flat', cursor='hand2', command=command, pady=8)
    btn.pack(fill='x', pady=8)

create_menu_button(buttons_frame, "Fase 1: Imagen como matriz", show_black_image)
create_menu_button(buttons_frame, "Fase 2: Generación de gradientes", show_gradient)
create_menu_button(buttons_frame, "Fase 3: Patrones matemáticos", show_math_pattern)
create_menu_button(buttons_frame, "Fase 4: Imágenes en color", show_rgb_image)
create_menu_button(buttons_frame, "Fase 5: Generación con OpenCV", show_opencv_shapes)
create_menu_button(buttons_frame, "Fase 6: Desafío Final", show_final_challenge)

tk.Button(root, text="Salir del Taller", font=('Segoe UI', 11, 'bold'), fg='#ECF0F1', bg='#34495E', 
          activebackground='#2C3E50', activeforeground='white', relief='flat', 
          cursor='hand2', command=root.quit).pack(pady=20)

if __name__ == "__main__":
    root.mainloop()
