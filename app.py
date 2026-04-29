import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fest Season Scoreboard", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. CONFIGURACIÓN DE IMAGEN DE FONDO ---
fondo_url = "https://greenastragames.com/juego-de-mesa/fest-season/img/publico4.png"

# --- 3. DICCIONARIO DE GÉNEROS Y COLORES ---
colores_generos = {
    "ROCK": "#4A0E0E",
    "ALTERNATIVE": "#D68A45",
    "EDM": "#C5A046",
    "PUNK": "#2D5A3A",
    "HIP HOP / RAP": "#4A90C2",
    "METAL": "#5E4085",
    "HEAVY METAL": "#1B264F",
    "POP": "#A64473"
}

# --- 4. GENERACIÓN DINÁMICA DE CSS PARA CADA FADER ---
css_faders = ""
for g, color_hex in colores_generos.items():
    g_clean = g.replace(" ", "_").replace("/", "")
    css_faders += f"""
    div.element-container:has(#label-{g_clean}) + div.element-container .stSlider > div > div > div > div {{
        background-color: {color_hex} !important;
    }}
    """

# --- 5. ESTILOS CSS GENERALES ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("{fondo_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .centered-title {{
        text-align: center;
        color: #00D1FF;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 0 0 20px rgba(0, 209, 255, 0.6);
    }}
    .main-container {{
        background-color: rgba(16, 12, 43, 0.9);
        border-radius: 20px;
        padding: 25px;
        margin-top: 10px;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .category-label {{ 
        font-weight: bold; font-size: 16px; color: #00D1FF; margin-top: 10px;
    }}
    .total-card {{
        background: linear-gradient(145deg, #1e1942, #0a081a);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px solid;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
        margin-bottom: 10px;
    }}
    div[data-baseweb="input"] {{ background: transparent !important; border: none !important; }}
    input {{ color: white !important; text-align: center !important; font-weight: bold !important; }}
    
    {css_faders}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='centered-title'>🎸 FEST SEASON - SCOREBOARD 🎸</div>", unsafe_allow_html=True)

# --- 6. SELECCIÓN DE JUGADORES Y REGLA DE TAMAÑO FIJO ---
col_players, _ = st.columns([1, 10])
with col_players:
    num_jugadores = st.number_input("¿Cuántos juegan?", min_value=1, max_value=5, value=5)

# REGLA MAESTRA DE COLUMNAS (Alineación perfecta)
peso_label = 2.5
peso_jugador = 1.5
peso_fantasma = (5 - num_jugadores) * peso_jugador

if peso_fantasma > 0:
    anchos_columnas = [peso_label] + [peso_jugador] * num_jugadores + [peso_fantasma]
else:
    anchos_columnas = [peso_label] + [peso_jugador] * num_jugadores

# --- 7. LÓGICA DE CAPTURA DINÁMICA ---
colores_jugadores = ["#00D1FF", "#FF3366", "#FFD700", "#00FF85", "#BF00FF"]
nombres = []
totales = [0] * num_jugadores

with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # SECCIÓN: NOMBRES
    cols_n = st.columns(anchos_columnas)
    with cols_n[0]: st.subheader("👤 JUGADORES")
    for i in range(num_jugadores):
        with cols_n[i+1]:
            n = st.text_input(f"n_{i}", value="", placeholder="Ingrese nombre", key=f"n_{i}", label_visibility="collapsed")
            nombres.append(n)

    st.divider()

    def crear_fila(label, key_p, sub=""):
        cols = st.columns(anchos_columnas)
        with cols[0]: 
            st.markdown(f"<div class='category-label'>{label}</div>", unsafe_allow_html=True)
            if sub: st.caption(sub)
        valores = []
        for i in range(num_jugadores):
            with cols[i+1]:
                v = st.number_input("", 0, key=f"{key_p}_{i}", label_visibility="collapsed")
                valores.append(v)
        return valores

    # --- SECCIÓN 1: ALINEACIÓN ---
    with st.expander("🎼 1. ALINEACIÓN (CONSOLA DE GÉNEROS)"):
        st.caption("Ajusta el fader (0 a 4) y anota los artistas de cada jugador.")
        puntos_ali = [0] * num_jugadores
        
        for g, color_hex in colores_generos.items():
            g_clean = g.replace(" ", "_").replace("/", "")
            cols = st.columns(anchos_columnas)
            with cols[0]:
                st.markdown(f"<div id='label-{g_clean}' style='color: white; font-weight: bold; font-size: 16px; margin-bottom: -15px;'>🔊 {g}</div>", unsafe_allow_html=True)
                vol = st.slider(g, min_value=0, max_value=4, value=0, key=f"vol_{g_clean}", label_visibility="collapsed")
            for i in range(num_jugadores):
                with cols[i+1]:
                    cartas = st.number_input(f"Cartas_{g_clean}_{i}", 0, key=f"c_{g_clean}_{i}", label_visibility="collapsed")
                    puntos_ali[i] += cartas * vol
            st.markdown("<hr style='margin: 8px 0; border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)

    # --- SECCIÓN 2: TRACKS ---
    st.markdown("<div class='category-label'>📊 2. TRACKS</div>", unsafe_allow_html=True)
    cols_t = st.columns(anchos_columnas)
    puntos_tracks = []
    with cols_t[0]: st.caption("Se toma el PV de la ficha más baja")
    for i in range(num_jugadores):
        with cols_t[i+1]:
            with st.popover("📍 Editar"):
                t1 = st.number_input("Amenidad", 0, key=f"tr1_{i}")
                t2 = st.number_input("Asistencia", 0, key=f"tr2_{i}")
                t3 = st.number_input("Precio", 0, key=f"tr3_{i}")
            val_min = min(t1, t2, t3)
            st.code(f"PV: {val_min}")
            puntos_tracks.append(val_min)

    # --- CATEGORÍAS ESTÁNDAR ---
    obj = crear_fila("🎯 3. OBJETIVOS", "obj", "PV marcadores completados")
    sede = crear_fila("⛺ 4. SEDE", "sed", "Suma de construcciones")
    proy = crear_fila("📋 5. PROYECTOS", "pro", "Suma de grupos")
    esc = crear_fila("🏟️ 6. ESCENARIOS", "esc", "Tableros de alineación")

    # --- SECCIÓN 7: DINERO ---
    cols_d = st.columns(anchos_columnas)
    puntos_dinero = []
    with cols_d[0]: 
        st.markdown("<div class='category-label'>💰 7. DINERO</div>", unsafe_allow_html=True)
    for i in range(num_jugadores):
        with cols_d[i+1]:
            din = st.number_input("Dinero", 0, key=f"din_{i}", label_visibility="collapsed")
            pd = din // 5
            st.code(f"PV: {pd}")
            puntos_dinero.append(pd)

    # --- SECCIÓN EXTRAS ---
    ex1 = crear_fila("➕ EXTRA 1", "e1")
    ex2 = crear_fila("➕ EXTRA 2", "e2")
    ex3 = crear_fila("➕ EXTRA 3", "e3")

    for i in range(num_jugadores):
        totales[i] = (puntos_ali[i] + puntos_tracks[i] + obj[i] + 
                     sede[i] + proy[i] + esc[i] + puntos_dinero[i] + 
                     ex1[i] + ex2[i] + ex3[i])

    st.markdown("</div>", unsafe_allow_html=True)

# --- 8. PANEL DE RESULTADOS (ALINEACIÓN PERFECTA BAJO JUGADORES) ---
st.markdown("---")

# Usamos la misma regla de anchos que la tabla para que coincidan las columnas
res_cols = st.columns(anchos_columnas)

# Saltamos la primera columna (índice 0) porque es el espacio de las etiquetas
for i in range(num_jugadores):
    with res_cols[i+1]: # Empezamos en i+1 para alinear con las columnas de jugadores
        nombre_display = nombres[i] if nombres[i] else f"JUGADOR {i+1}"
        st.markdown(f"""
        <div class="total-card" style="border-color: {colores_jugadores[i]};">
            <h2 style="color: {colores_jugadores[i]}; margin:0; font-size:40px;">{totales[i]}</h2>
            <div style="color: white; font-weight: bold; margin-top:5px; font-size:14px;">{nombre_display}</div>
        </div>
        """, unsafe_allow_html=True)

# --- BOTÓN DE REINICIO ---
st.markdown("<br><br>", unsafe_allow_html=True)
_, col_boton, _ = st.columns([2, 1, 2])
with col_boton:
    if st.button("🔄 REINICIAR TABLERO", use_container_width=True):
        st.rerun()
