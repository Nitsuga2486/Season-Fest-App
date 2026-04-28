import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Fest Season Scoreboard", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. CONFIGURACIÓN DE IMAGEN DESDE GITHUB ---
# Usando la ruta organizada que creaste
fondo_url = "https://raw.githubusercontent.com/Nitsuga2486/Season-Fest-App/main/static/images/festival-celebration.png"

# --- 3. ESTILOS CSS (DISEÑO NEÓN Y TRANSPARENCIAS) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("{fondo_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-container {{
        background-color: rgba(16, 12, 43, 0.9);
        border-radius: 20px;
        padding: 25px;
        margin-top: 10px;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .category-label {{ 
        font-weight: bold; 
        font-size: 16px; 
        color: #00D1FF; 
        margin-top: 10px;
    }}
    .player-name {{
        color: white;
        text-align: center;
        font-weight: bold;
    }}
    /* Estilo para los totales finales */
    .total-card {{
        background: linear-gradient(145deg, #1e1942, #0a081a);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px solid;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
    }}
    /* Limpieza de inputs de Streamlit */
    div[data-baseweb="input"] {{ background: transparent !important; border: none !important; }}
    input {{ color: white !important; text-align: center !important; font-weight: bold !important; }}
</style>
""", unsafe_allow_html=True)

st.title("🎸 FEST SEASON - SCOREBOARD 🎸")

# --- 4. LÓGICA DE CAPTURA ---
colores = ["#00D1FF", "#FF3366", "#FFD700", "#00FF85", "#BF00FF"]
nombres = []
totales = [0] * 5

with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    # SECCIÓN: JUGADORES
    cols_n = st.columns([2, 1, 1, 1, 1, 1])
    with cols_n[0]: st.subheader("👤 JUGADORES")
    for i in range(5):
        with cols_n[i+1]:
            n = st.text_input(f"n_{i}", f"JUGADOR {i+1}", key=f"n_{i}", label_visibility="collapsed")
            nombres.append(n)

    st.divider()

    # Función auxiliar para filas de puntos
    def crear_fila(label, key_p, sub=""):
        cols = st.columns([2, 1, 1, 1, 1, 1])
        with cols[0]: 
            st.markdown(f"<div class='category-label'>{label}</div>", unsafe_allow_html=True)
            if sub: st.caption(sub)
        valores = []
        for i in range(5):
            with cols[i+1]:
                v = st.number_input("", 0, key=f"{key_p}_{i}", label_visibility="collapsed")
                valores.append(v)
        return valores

    # 1. ALINEACIÓN (8 FILAS DE GÉNEROS)
    with st.expander("🎼 1. ALINEACIÓN (8 GÉNEROS - Detalle)"):
        generos = ["Pop", "Rock", "Electronic", "Jazz", "Metal", "Indie", "Hip Hop", "Classical"]
        puntos_ali = [0] * 5
        for g in generos:
            p_gen = crear_fila(f"Artistas {g}", f"g_{g}", "PV x Volumen")
            for i in range(5): puntos_ali[i] += p_gen[i]

    # 2. TRACKS (MÍNIMO AUTOMÁTICO)
    st.markdown("<div class='category-label'>📊 2. TRACKS (Amenidad, Asistencia, Precio)</div>", unsafe_allow_html=True)
    cols_t = st.columns([2, 1, 1, 1, 1, 1])
    puntos_tracks = []
    with cols_t[0]: st.caption("Se toma el PV de la ficha más baja")
    for i in range(5):
        with cols_t[i+1]:
            with st.popover("📍 Editar"):
                t1 = st.number_input("Amenidad", 0, key=f"tr1_{i}")
                t2 = st.number_input("Asistencia", 0, key=f"tr2_{i}")
                t3 = st.number_input("Precio", 0, key=f"tr3_{i}")
            m = min(t1, t2, t3)
            st.code(f"PV: {m}")
            puntos_tracks.append(m)

    # CATEGORÍAS ESTÁNDAR
    obj = crear_fila("🎯 3. OBJETIVOS", "obj", "PV marcadores completados")
    sede = crear_fila("⛺ 4. SEDE", "sed", "Suma de construcciones")
    proy = crear_fila("📋 5. PROYECTOS", "pro", "Suma de grupos")
    esc = crear_fila("🏟️ 6. ESCENARIOS", "esc", "Tableros de alineación")

    # 7. DINERO (DIVISIÓN / 5 AUTOMÁTICA)
    cols_d = st.columns([2, 1, 1, 1, 1, 1])
    puntos_dinero = []
    with cols_d[0]: 
        st.markdown("<div class='category-label'>💰 7. DINERO</div>", unsafe_allow_html=True)
        st.caption("1 PV por cada 5 sobrantes")
    for i in range(5):
        with cols_d[i+1]:
            din = st.number_input("Dinero", 0, key=f"din_{i}", label_visibility="collapsed")
            pd = din // 5
            st.code(f"PV: {pd}")
            puntos_dinero.append(pd)

    # EXTRAS
    ex1 = crear_fila("➕ EXTRA 1", "e1")
    ex2 = crear_fila("➕ EXTRA 2", "e2")
    ex3 = crear_fila("➕ EXTRA 3", "e3")

    # CÁLCULO FINAL DE TOTALES
    for i in range(5):
        totales[i] = puntos_ali[i] + puntos_tracks[i] + obj[i] + sede[i] + proy[i] + esc[i] + puntos_dinero[i] + ex1[i] + ex2[i] + ex3[i]

    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. PANEL DE RESULTADOS (TARJETAS NEÓN) ---
st.markdown("---")
res_cols = st.columns(5)
for i in range(5):
    with res_cols[i]:
        st.markdown(f"""
        <div class="total-card" style="border-color: {colores[i]};">
            <h2 style="color: {colores[i]}; margin:0; font-size:40px;">{totales[i]}</h2>
            <div style="color: white; font-weight: bold; margin-top:5px;">{nombres[i]}</div>
        </div>
        """, unsafe_allow_html=True)

# --- ESPACIADOR PARA EL BOTÓN ---
# Añadimos tres saltos de línea para empujar el botón hacia abajo
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Centramos el botón usando columnas
_, col_boton, _ = st.columns([2, 1, 2])
with col_boton:
    if st.button("🔄 REINICIAR TABLERO", use_container_width=True):
        st.rerun()
