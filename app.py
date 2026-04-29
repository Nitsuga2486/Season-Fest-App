import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fest Season Scoreboard", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. CONFIGURACIÓN DE IMAGEN DE FONDO ---
fondo_url = "https://greenastragames.com/juego-de-mesa/fest-season/img/publico4.png"

# --- 3. ESTILOS CSS (DISEÑO NEÓN) ---
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
    
    /* Estilo para los sliders de niveles */
    .stSelectSlider div[data-baseweb="slider"] {{
        padding-bottom: 25px;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='centered-title'>🎸 FEST SEASON - SCOREBOARD 🎸</div>", unsafe_allow_html=True)

# --- 4. SELECCIÓN DE JUGADORES ---
col_players, _ = st.columns([1, 3])
with col_players:
    num_jugadores = st.number_input("¿Cuántos juegan?", min_value=1, max_value=5, value=5)

# --- 5. LÓGICA DE CAPTURA DINÁMICA ---
colores = ["#00D1FF", "#FF3366", "#FFD700", "#00FF85", "#BF00FF"]
nombres = []
totales = [0] * num_jugadores

with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # SECCIÓN: NOMBRES
    # Usamos una proporción de 3 para la etiqueta y 1 para cada jugador para dar estabilidad
    proporciones = [3] + [1] * num_jugadores
    cols_n = st.columns(proporciones)
    with cols_n[0]: st.subheader("👤 JUGADORES")
    for i in range(num_jugadores):
        with cols_n[i+1]:
            n = st.text_input(f"n_{i}", value="", placeholder="Nombre", key=f"n_{i}", label_visibility="collapsed")
            nombres.append(n)

    st.divider()

    # Función auxiliar para filas estándar
    def crear_fila(label, key_p, sub=""):
        cols = st.columns(proporciones)
        with cols[0]: 
            st.markdown(f"<div class='category-label'>{label}</div>", unsafe_allow_html=True)
            if sub: st.caption(sub)
        valores = []
        for i in range(num_jugadores):
            with cols[i+1]:
                v = st.number_input("", 0, key=f"{key_p}_{i}", label_visibility="collapsed")
                valores.append(v)
        return valores

    # --- SECCIÓN 1: ALINEACIÓN (CONSOLA ESTÁNDAR) ---
    with st.expander("🎼 1. ALINEACIÓN (NIVELES DE GÉNERO)", expanded=True):
        st.caption("Ajusta el nivel del género (0-4) y anota cuántas cartas tiene cada jugador.")
        generos = ["Pop", "Rock", "Electronic", "Jazz", "Metal", "Indie", "Hip Hop", "Classical"]
        puntos_ali = [0] * num_jugadores
        
        for g in generos:
            cols = st.columns(proporciones)
            with cols[0]:
                # Usamos select_slider para tener indicadores fijos (0, 1, 2, 3, 4)
                vol = st.select_slider(
                    f"🎛️ {g}",
                    options=[0, 1, 2, 3, 4],
                    value=0,
                    key=f"vol_{g}"
                )
            
            for i in range(num_jugadores):
                with cols[i+1]:
                    cartas = st.number_input(f"c_{g}_{i}", 0, key=f"c_{g}_{i}", label_visibility="collapsed")
                    puntos_ali[i] += cartas * vol
            
            st.markdown("<hr style='margin: 5px 0; opacity: 0.1;'>", unsafe_allow_html=True)

    # --- SECCIÓN 2: TRACKS ---
    st.markdown("<div class='category-label'>📊 2. TRACKS</div>", unsafe_allow_html=True)
    cols_t = st.columns(proporciones)
    puntos_tracks = []
    with cols_t[0]: st.caption("PV de la ficha más baja (Amenidad/Asist/Precio)")
    for i in range(num_jugadores):
        with cols_t[i+1]:
            with st.popover("📍 Editar"):
                t1 = st.number_input("Amenidad", 0, key=f"tr1_{i}")
                t2 = st.number_input("Asistencia", 0, key=f"tr2_{i}")
                t3 = st.number_input("Precio", 0, key=f"tr3_{i}")
            val_min = min(t1, t2, t3)
            st.code(f"PV: {val_min}")
            puntos_tracks.append(val_min)

    # --- RESTO DE CATEGORÍAS ---
    obj = crear_fila("🎯 3. OBJETIVOS", "obj", "PV marcadores")
    sede = crear_fila("⛺ 4. SEDE", "sed", "Suma construcciones")
    proy = crear_fila("📋 5. PROYECTOS", "pro", "Suma grupos")
    esc = crear_fila("🏟️ 6. ESCENARIOS", "esc", "Tableros alineación")

    # --- DINERO ---
    cols_d = st.columns(proporciones)
    puntos_dinero = []
    with cols_d[0]: st.markdown("<div class='category-label'>💰 7. DINERO (PV: 1x5$)</div>", unsafe_allow_html=True)
    for i in range(num_jugadores):
        with cols_d[i+1]:
            din = st.number_input("Dinero", 0, key=f"din_{i}", label_visibility="collapsed")
            pd = din // 5
            st.code(f"PV: {pd}")
            puntos_dinero.append(pd)

    # EXTRAS
    ex1 = crear_fila("➕ EXTRA 1", "e1")
    ex2 = crear_fila("➕ EXTRA 2", "e2")
    ex3 = crear_fila("➕ EXTRA 3", "e3")

    for i in range(num_jugadores):
        totales[i] = (puntos_ali[i] + puntos_tracks[i] + obj[i] + sede[i] + 
                     proy[i] + esc[i] + puntos_dinero[i] + ex1[i] + ex2[i] + ex3[i])

    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. PANEL DE RESULTADOS ---
st.markdown("---")
res_cols = st.columns(num_jugadores)
for i in range(num_jugadores):
    with res_cols[i]:
        nombre_display = nombres[i] if nombres[i] else f"JUGADOR {i+1}"
        st.markdown(f"""
        <div class="total-card" style="border-color: {colores[i]};">
            <h2 style="color: {colores[i]}; margin:0; font-size:40px;">{totales[i]}</h2>
            <div style="color: white; font-weight: bold; margin-top:5px;">{nombre_display}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
_, col_boton, _ = st.columns([2, 1, 2])
with col_boton:
    if st.button("🔄 REINICIAR TABLERO", use_container_width=True):
        st.rerun()
