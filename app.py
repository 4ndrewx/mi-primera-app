import numpy as np
from PIL import Image
import streamlit as st

# Configuración general de la página
st.set_page_config(
    page_title="Interfaces Multimodales | Andres Felipe Gonzalez",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CABECERA PERSONALIZADA ---
st.title("Plataforma Multimodal de Andres Felipe Gonzalez")
st.markdown(
    "### Innovación en sistemas embebidos, visión artificial y control"
    " inteligente."
)
st.write(
    "Este espacio digital integra procesamiento de señales visuales y"
    " arquitectura de hardware simulado."
)

# --- SECCIÓN VISUAL PRINCIPAL (Imagen abstracta / tecnológica) ---
# Generamos un banner visual dinámico o contenedor estético
st.markdown("---")
col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
  # Creación de un diseño visual atractivo por defecto
  st.info(
      "💻 Módulo activo: Procesamiento de Visión Artificial y Protocolos de"
      " Red"
  )

# --- ENTRADA DE TEXTO DINÁMICA ---
st.markdown("### Consola de Comandos y Parámetros")
user_input = st.text_input(
    "Escribe un comando o instrucción del sistema:",
    "inicializar_servidor_mqtt",
)
st.success(f"Estado del sistema: Ejecutando instrucción -> `{user_input}`")

st.markdown("---")

# --- SECCIÓN DE 2 COLUMNAS (Estructura Avanzada) ---
st.markdown("### Arquitectura de Control Distribuido")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Panel Operativo A")
  st.write(
      "Los sistemas basados en eventos reducen la latencia en la transmisión"
      " de datos IoT."
  )
  confirm_state = st.checkbox("Sincronización de nodos completada")
  if confirm_state:
    st.markdown(
        "<p style='color: #10B981; font-weight: bold;'>¡Flujo de datos"
        " validado correctamente!</p>",
        unsafe_allow_html=True,
    )
  else:
    st.warning("Esperando confirmación de nodos...")

with col2:
  st.subheader("Panel Operativo B")
  st.write("Selecciona el protocolo de comunicación principal:")
  protocol_choice = st.radio(
      "Protocolo activo:", ["MQTT (Broker)", "WebSockets", "HTTP REST API"]
  )
  st.markdown(
      f"Canal seleccionado: <span"
      f" style='color:#38BDF8;font-weight:bold;'>{protocol_choice}</span>",
      unsafe_allow_html=True,
  )

st.markdown("---")

# --- SECCIÓN DE ACCIÓN / BOTONES ---
st.markdown("### Panel de Control de Hardware")
col_btn1, col_btn2 = st.columns([1, 3])

with col_btn1:
  trigger_action = st.button("Ejecutar Secuencia")

with col_btn2:
  if trigger_action:
    st.success(
        "¡Secuencia de comandos enviada exitosamente a los dispositivos"
        " remotos!"
    )
  else:
    st.markdown(
        "<span style='color: gray;'>Sistema en espera de activación...</span>",
        unsafe_allow_html=True,
    )
