import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fest Season Scoreboard", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. CONFIGURACIÓN DE IMAGEN DESDE CDN ---
fondo_url = "https://greenastragames.com/juego-de-mesa/fest-season/img/publico4.png"

# --- 3. ESTILOS CSS ---
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
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='centered-title'>🎸 FEST SEASON - SCOREBOARD 🎸</div>", unsafe_allow_html=True)

# --- 4. SELECCIÓN DE JUGADORES ---
col_players, _ = st.columns([1, 5])
with col_players:
    num_jugadores = st.number_input("¿Cuántos juegan?", min_value=1, max_value=5, value=5)

# --- 5. LÓGICA DE CAPTURA DINÁMICA ---
colores = ["#00D1FF", "#FF3366", "#FFD700", "#00FF85", "#BF00FF"]
nombres = []
totales = [0] * num_jugadores

with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # SECCIÓN: NOMBRES (Solo el número seleccionado)
    cols_n = st.columns([2] + [1] * num_jugadores)
    with cols_n[0]: st.subheader("👤 JUGADORES")
    for i in range(num_jugadores):
        with cols_n[i+1]:
            n = st.text_input(f"n_{i}", f"JUGADOR {i+1}", key=f"n_{i}", label_visibility="collapsed")
            nombres.append(n)

    st.divider()

    # Función auxiliar para filas de puntos dinámica
    def crear_fila(label, key_p, sub=""):
        cols = st.columns([2] + [1] * num_jugadores)
        with cols[0]: 
            st.markdown(f"<div class='category-label'>{label}</div>", unsafe_allow_html=True)
            if sub: st.caption(sub)
        valores = []
        for i in range(num_jugadores):
            with cols[i+1]:
                v = st.number_input("", 0, key=f"{key_p}_{i}", label_visibility="collapsed")
                valores.append(v)
        return valores

    # 1. ALINEACIÓN
    with st.expander("🎼 1. ALINEACIÓN (8 GÉNEROS)"):
        generos = ["Pop", "Rock", "Electronic", "Jazz", "Metal", "Indie", "Hip Hop", "Classical"]
        puntos_ali = [0] * num_jugadores
        for g in generos:
            p_gen = crear_fila(f"Artistas {g}", f"g_{g}", "PV x Volumen")
            for i in range(num_jugadores): puntos_ali[i] += p_gen[i]

    # 2. TRACKS
    st.markdown("<div class='category-label'>📊 2. TRACKS</div>", unsafe_allow_html=True)
    cols_t = st.columns([2] + [1] * num_jugadores)
    puntos_tracks = []
    with cols_t[0]: st.caption("PV de la ficha más baja")
    for i in range(num_jugadores):
        with cols_t[i+1]:
            with st.popover("📍 Editar"):
                t1 = st.number_input("Amenidad", 0, key=f"tr1_{i}")
                t2 = st.number_input("Asistencia", 0, key=f"tr2_{i}")
                t3 = st.number_input("Precio", 0, key=f"tr3_{i}")
            m = min(t1, t2, t3)
            st.code(f"PV: {m}")
            puntos_tracks.append(m)

    # RESTO DE CATEGORÍAS
    obj = crear_fila("🎯 3. OBJETIVOS", "obj", "PV marcadores")
    sede = crear_fila("⛺ 4. SEDE", "sed", "Suma construcciones")
    proy = crear_fila("📋 5. PROYECTOS", "pro", "Suma grupos")
    esc = crear_fila("🏟️ 6. ESCENARIOS", "esc", "Tableros alineación")

    # 7. DINERO
    cols_d = st.columns([2] + [1] * num_jugadores)
    puntos_dinero = []
    with cols_d[0]: 
        st.markdown("<div class='category-label'>💰 7. DINERO</div>", unsafe_allow_html=True)
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

    # CÁLCULO TOTAL
    for i in range(num_jugadores):
        totales[i] = puntos_ali[i] + puntos_tracks[i] + obj[i] + sede[i] + proy[i] + esc[i] + puntos_dinero[i] + ex1[i] + ex2[i] + ex3[i]

    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. RESULTADOS (Dinámicos) ---
st.markdown("---")
res_cols = st.columns(num_jugadores)
for i in range(num_jugadores):
    with res_cols[i]:
        st.markdown(f"""
        <div class="total-card" style="border-color: {colores[i]};">
            <h2 style="color: {colores[i]}; margin:0; font-size:40px;">{totales[i]}</h2>
            <div style="color: white; font-weight: bold; margin-top:5px;">{nombres[i]}</div>
        </div>
        """, unsafe_allow_html=True)

# ESPACIADOR Y BOTÓN
st.markdown("<br><br>", unsafe_allow_html=True)
_, col_boton, _ = st.columns([2, 1, 2])
with col_boton:
    if st.button("🔄 REINICIAR TABLERO", use_container_width=True):
        st.rerun()
