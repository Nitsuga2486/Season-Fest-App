[slides]
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fest Season App V3 Update</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { box-sizing: border-box; }
        body { background-color: #0b0e14; display: grid; gap: 20px; grid-template-columns: 1fr; margin: 0; min-height: 100vh; padding: 20px 0; place-items: center; }
        .slide-container { align-items: center; background-color: #10141d; border-radius: 8px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); display: flex; flex-direction: column; font-family: 'Lato', sans-serif; height: 720px; justify-content: center; overflow: hidden; padding: 60px; position: relative; width: 1280px; border: 1px solid #1e293b; }
        .slide-container::before { content: ''; height: 100%; left: 0; position: absolute; top: 0; width: 100%; z-index: 0; background: radial-gradient(circle at 20% 30%, rgba(0, 209, 255, 0.05) 0%, transparent 50%), radial-gradient(circle at 80% 70%, rgba(166, 68, 115, 0.05) 0%, transparent 50%); }
        .slide-container>* { position: relative; z-index: 1; }
        .slide-container h1, .slide-container h2, .slide-container h3 { color: #f8fafc; font-weight: 700; font-family: 'Poppins', sans-serif; margin: 0; }
        .slide-container p, .slide-container li { color: #94a3b8; font-size: 18px; line-height: 1.5; }
        .slide-container h1 { font-size: 70px; text-shadow: 0 0 20px rgba(0, 209, 255, 0.4); }
        .slide-container .slide-title { font-size: 40px; font-weight: 700; margin-bottom: 40px; text-align: left; width: 100%; color: #00D1FF; border-left: 5px solid #00D1FF; padding-left: 20px; }
        .content-area { align-items: center; display: flex; flex-direction: column; flex-grow: 1; justify-content: center; width: 100%; }
        .two-column { align-items: flex-start; display: grid; grid-template-columns: 1fr 1fr; gap: 50px; width: 100%; }
        .image-wrapper { border-radius: 12px; height: 400px; overflow: hidden; width: 100%; border: 1px solid #334155; }
        .image-wrapper img { height: 100%; width: 100%; object-fit: cover; }
        .tile { background-color: #1e293b; border-radius: 12px; border: 1px solid #334155; padding: 30px; text-align: center; flex: 1; }
        .tile .icon { color: #00D1FF; font-size: 48px; margin-bottom: 20px; }
        .tile h3 { font-size: 24px; margin-bottom: 10px; }
        .tiled-content { display: flex; gap: 30px; width: 100%; }
        .highlight { color: #00D1FF; font-weight: bold; }
        .accent { color: #A64473; font-weight: bold; }
        .bullet-list { list-style: none; padding: 0; margin: 0; }
        .bullet-list li { margin-bottom: 20px; position: relative; padding-left: 40px; }
        .bullet-list i { position: absolute; left: 0; top: 5px; color: #00D1FF; font-size: 24px; }
        .bleed-image-layout { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: start; padding: 0 !important; }
        .bleed-text-side { padding: 60px; display: flex; flex-direction: column; justify-content: center; height: 100%; }
        .bleed-image-side { height: 720px; width: 100%; object-fit: cover; border-radius: 0 8px 8px 0; }
    </style>
</head>
<body>

<div class="slide-container" id="slide1">
    <div class="content-area">
        <h3 style="color: #00D1FF; letter-spacing: 5px; margin-bottom: 10px;">PROYECTO: SCOREBOARD</h3>
        <h1>FEST SEASON <span style="color:#A64473">V3</span></h1>
        <p style="font-size: 24px; margin-top: 20px;">Optimización Visual, Estructura y Legibilidad Neón</p>
    </div>
</div>

<div class="slide-container" id="slide2">
    <div class="content-area">
        <h2 style="font-size: 60px; margin-bottom: 20px;">El Desafío</h2>
        <p style="max-width: 800px; text-align: center; font-size: 22px;">Mejorar la experiencia de usuario en entornos de baja luz, manteniendo la estética de festival y la precisión en el cálculo de puntuación.</p>
    </div>
</div>

<div class="slide-container" id="slide3">
    <h2 class="slide-title">Pilares de la Actualización</h2>
    <div class="content-area">
        <div class="tiled-content">
            <div class="tile">
                <div class="icon"><i class="fa-solid fa-eye"></i></div>
                <h3>Contraste</h3>
                <p>Textos en blanco puro y celeste brillante para garantizar lectura sobre fondos oscuros.</p>
            </div>
            <div class="tile">
                <div class="icon"><i class="fa-solid fa-layer-group"></i></div>
                <h3>Estructura</h3>
                <p>Uso de combos expansibles para agrupar puntuaciones secundarias y limpiar la UI.</p>
            </div>
            <div class="tile">
                <div class="icon"><i class="fa-solid fa-palette"></i></div>
                <h3>Identidad</h3>
                <p>Colores de diales mapeados directamente a la iconografía oficial del juego.</p>
            </div>
        </div>
    </div>
</div>

<div class="slide-container bleed-image-layout" id="slide4">
    <div class="bleed-text-side">
        <h2 class="slide-title">Consola de Géneros</h2>
        <p>Implementación de un sistema de <span class="highlight">Faders Individuales</span> con colores personalizados:</p>
        <ul class="bullet-list">
            <li><i class="fa-solid fa-sliders"></i> <strong>Colores Hex:</strong> Mapeo de Rock, Punk, Pop, etc.</li>
            <li><i class="fa-solid fa-check"></i> <strong>Legibilidad:</strong> Etiquetas blancas permanentes.</li>
            <li><i class="fa-solid fa-bolt"></i> <strong>Reactividad:</strong> Cálculo inmediato de PV.</li>
        </ul>
    </div>
    <img class="bleed-image-side" src="http://googleusercontent.com/image_collection/image_retrieval/8883493826498783594" alt="Audio Mixer Faders">
</div>

<div class="slide-container" id="slide5">
    <h2 class="slide-title">Reglas de Puntuación</h2>
    <div class="content-area">
        <div class="two-column">
            <div>
                <h3>Límites y Validación</h3>
                <p>Para asegurar la fidelidad al manual de juego, hemos reforzado los controles de entrada:</p>
                <ul class="bullet-list">
                    <li><i class="fa-solid fa-gauge-high"></i> <strong>Tracks 1-12:</strong> Límite estricto en Amenidad, Asistencia y Precios.</li>
                    <li><i class="fa-solid fa-coins"></i> <strong>Dinero:</strong> Conversión automática de 1 PV por cada $5 sobrantes.</li>
                    <li><i class="fa-solid fa-star"></i> <strong>Extras:</strong> Sección agrupada para eventos VIP.</li>
                </ul>
            </div>
            <div class="image-wrapper">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/3454299562641968922" alt="Scoreboard UI Design">
            </div>
        </div>
    </div>
</div>

<div class="slide-container" id="slide6">
    <h2 class="slide-title">Equilibrio de Espacio</h2>
    <div class="content-area">
        <div class="two-column" style="grid-template-columns: 40% 60%; align-items: center;">
            <div style="text-align: center;">
                <div style="font-size: 120px; color: #00D1FF; font-weight: 700;">25/15</div>
                <p style="font-size: 24px; font-weight: bold;">Ratio de Diseño</p>
            </div>
            <div>
                <p>Hemos fijado el ancho de las columnas para evitar distorsiones:</p>
                <ul class="bullet-list">
                    <li><span class="highlight">25%</span> para etiquetas y faders de volumen.</li>
                    <li><span class="highlight">15%</span> exacto para cada columna de jugador.</li>
                    <li>Columnas fantasma para mantener la simetría con 1 a 5 jugadores.</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="slide-container" id="slide7">
    <h2 class="slide-title">Componentes V3</h2>
    <div class="content-area">
        <div class="tiled-content">
            <div class="tile" style="padding: 0; overflow: hidden; height: 350px;">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/7087738139991979940" style="width: 100%; height: 200px; object-fit: cover;">
                <div style="padding: 15px;"><h3>Fondo Inmersivo</h3><p>Público en neón.</p></div>
            </div>
            <div class="tile" style="padding: 0; overflow: hidden; height: 350px;">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/2682471893741030309" style="width: 100%; height: 200px; object-fit: cover;">
                <div style="padding: 15px;"><h3>Mixer de Géneros</h3><p>8 estilos musicales.</p></div>
            </div>
            <div class="tile" style="padding: 0; overflow: hidden; height: 350px;">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/15378116546739882301" style="width: 100%; height: 200px; object-fit: cover;">
                <div style="padding: 15px;"><h3>Cards de Neón</h3><p>Resultados finales.</p></div>
            </div>
        </div>
    </div>
</div>

<div class="slide-container" id="slide8">
    <h2 class="slide-title">Mapeo de Colores Oficiales</h2>
    <div class="content-area">
        <table style="width: 100%; border-collapse: collapse; color: white;">
            <thead>
                <tr style="background-color: #1e293b;">
                    <th style="padding: 15px; text-align: left; border-bottom: 2px solid #00D1FF;">Género</th>
                    <th style="padding: 15px; text-align: left; border-bottom: 2px solid #00D1FF;">Color Identidad</th>
                    <th style="padding: 15px; text-align: left; border-bottom: 2px solid #00D1FF;">Hexadecimal</th>
                </tr>
            </thead>
            <tbody>
                <tr><td style="padding: 12px; border-bottom: 1px solid #334155;">ROCK</td><td style="color: #4A0E0E; font-weight: bold;">Tinto</td><td>#4A0E0E</td></tr>
                <tr><td style="padding: 12px; border-bottom: 1px solid #334155;">EDM</td><td style="color: #C5A046; font-weight: bold;">Dorado</td><td>#C5A046</td></tr>
                <tr><td style="padding: 12px; border-bottom: 1px solid #334155;">HIP HOP</td><td style="color: #4A90C2; font-weight: bold;">Celeste</td><td>#4A90C2</td></tr>
                <tr><td style="padding: 12px; border-bottom: 1px solid #334155;">POP</td><td style="color: #A64473; font-weight: bold;">Fucsia</td><td>#A64473</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="slide-container" id="slide9">
    <div class="content-area">
        <div style="max-width: 800px; text-align: center;">
            <i class="fa-solid fa-quote-left" style="font-size: 60px; color: #00D1FF; margin-bottom: 20px;"></i>
            <h2 style="font-size: 48px; font-weight: 400; font-style: italic;">"La mejor herramienta no es la que más datos muestra, sino la que mejor los organiza para el momento crítico del juego."</h2>
            <p style="margin-top: 20px;">— Team Green Astra Games</p>
        </div>
    </div>
</div>

<div class="slide-container" id="slide10">
    <h2 class="slide-title">Hoja de Ruta de Implementación</h2>
    <div class="content-area" style="position: relative; width: 100%; height: 300px; display: flex; align-items: center; justify-content: space-around;">
        <div style="height: 4px; background: #334155; position: absolute; width: 80%; top: 50%; z-index: 0;"></div>
        <div style="text-align: center; position: relative; z-index: 1;">
            <div style="width: 30px; height: 30px; background: #00D1FF; border-radius: 50%; margin: 0 auto 10px;"></div>
            <h3>Captura</h3>
            <p>Selector de jugadores</p>
        </div>
        <div style="text-align: center; position: relative; z-index: 1;">
            <div style="width: 30px; height: 30px; background: #00D1FF; border-radius: 50%; margin: 0 auto 10px;"></div>
            <h3>Mixer</h3>
            <p>Niveles de Género</p>
        </div>
        <div style="text-align: center; position: relative; z-index: 1;">
            <div style="width: 30px; height: 30px; background: #A64473; border-radius: 50%; margin: 0 auto 10px;"></div>
            <h3>Cálculo</h3>
            <p>Suma de Tracks/Extras</p>
        </div>
    </div>
</div>

<div class="slide-container" id="slide11" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('http://googleusercontent.com/image_collection/image_retrieval/3097432020004693412'); background-size: cover; background-position: center;">
    <div class="content-area" style="text-align: center;">
        <h2 style="font-size: 56px;">Listos para el Rock</h2>
        <p style="font-size: 24px; color: white; max-width: 800px;">La versión V3 está optimizada para dispositivos móviles y tablets, permitiendo que el Scoreboard esté presente en la mesa sin estorbar la jugabilidad.</p>
    </div>
</div>

<div class="slide-container" id="slide12">
    <div class="content-area">
        <h2 style="font-size: 64px; color: #00D1FF;">¿Dudas sobre el Setup?</h2>
        <p style="font-size: 22px;">Actualiza tu archivo en GitHub y disfruta la experiencia.</p>
        <div style="margin-top: 50px; font-size: 20px; border-top: 1px solid #334155; padding-top: 20px;">
            <span class="highlight">GREEN ASTRA GAMES</span> | 2024
        </div>
    </div>
</div>

</body>
</html>

