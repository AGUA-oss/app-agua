import streamlit as st
import pandas as pd

# Configurar el diseño de la aplicación móvil
st.set_page_config(page_title="Agua Express - Vendedores", page_icon="💧", layout="centered")

st.title("💧 Sistema de Ventas: Agua Express")
st.write("Bienvenido al panel del repartidor")

# 1. Leer los datos reales desde tu archivo de Excel
EXCEL_PATH = "Datos_Agua.xlsx"
df_clientes = pd.read_excel(EXCEL_PATH, sheet_name="Clientes")
df_catalogo = pd.read_excel(EXCEL_PATH, sheet_name="Catalogo")

# --- SECCIÓN 1: RUTA OPTIMIZADA DE CLIENTES ---
st.header("📍 Tu Hoja de Ruta del Día")
st.write("Clientes ordenados automáticamente por distancia:")

# Ordenar los clientes por distancia (Algoritmo que creamos antes)
df_clientes_ordenado = df_clientes.sort_values(by="Distancia_KM")

for index, cliente in df_clientes_ordenado.iterrows():
    # Crear una tarjeta visual para cada cliente
    with st.container():
        st.subheader(f"{cliente['Nombre_Cliente']} (a {cliente['Distancia_KM']} km)")
        st.write(f"🏠 Dirección: {cliente['Direccion']}")
        st.write(f"🏢 Tipo: {cliente['Tipo_Establecimiento']}")
        
        # Botón para abrir Google Maps automáticamente con la dirección del Excel
        url_maps = "https://google.com"
        st.markdown(f"[🗺️ Ver en Google Maps]({url_maps})")
        st.write("---")

# --- SECCIÓN 2: CATÁLOGO LLAMATIVO DE PRODUCTOS ---
st.header("🛒 Catálogo Inteligente de Productos")

# Mostrar los productos en un diseño de cuadrícula elegante
cols = st.columns(len(df_catalogo))

for i, (index, producto) in enumerate(df_catalogo.iterrows()):
    with cols[i]:
        # Dibujar la imagen web que configuramos en el Excel
        st.image(producto['Imagen_URL'], use_column_width=True)
        st.write(f"**{producto['Nombre_Producto']}**")
        st.write(f"💰 Precio: ${producto['Precio']}")
        st.write(f"🏷️ Categoría: {producto['Categoria']}")
        # Botón interactivo para simular la venta
        if st.button(f"Vender {producto['ID_Producto']}", key=producto['ID_Producto']):
            st.success(f"¡Pedido registrado para {producto['Nombre_Producto']}!")
