# pokemmo-shiny-bot

Bot de tracking de Shinies para PokéMMO - Notificaciones en tiempo real de apariciones de Pokémon Shiny

## Descripción

Este proyecto está pensado para ayudar a los jugadores de PokéMMO a:

- contar encuentros realizados
- detectar cuándo aparece un Pokémon shiny
- registrar un historial de encuenros
- enviar notificaciones visuales o sonoras
- apoyar rutas de grind o búsquedas de shiny

La idea principal es detectar la aparición real del shiny mediante comparación visual de la pantalla o de elementos relevantes del juego, en lugar de depender solo de probabilidades.

## Objetivo

Crear un bot útil para monitorear encuentros en PokéMMO y avisar al jugador cuando ocurra un shiny.

## Tecnologías recomendadas

- Python 3.12+
- PyAutoGUI
- Pillow (PIL)
- OpenCV
- PyWin32 o win32api (Windows)
- Discord Webhook (opcional)
- Tkinter o PyQt (opcional para interfaz gráfica)

## Estructura sugerida del proyecto

```text
pokemmo-shiny-bot/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── capture.py
│   ├── detector.py
│   ├── notifications.py
│   └── logger.py
├── assets/
│   ├── templates/
│   └── samples/
├── data/
│   └── history.json
├── .gitignore
└── LICENSE
```

## Funcionalidades planeadas

- Captura de pantalla del cliente de PokéMMO
- Conteo de encuentros
- Detección visual de shiny
- Notificaciones por sonido, consola o Discord
- Registro de historial en JSON
- Interfaz simple para empezar a usar el bot

## Cómo funciona

1. El bot captura una imagen del juego.
2. Compara zonas clave de la pantalla con referencias conocidas.
3. Detecta un cambio indicando la aparición de shiny.
4. Registra la cantidad de encuentros realizados.
5. Notifica al usuario con un aviso inmediato.

## Requisitos

- Python 3.12 o superior
- Windows 10/11
- PokéMMO abierto en la pantalla
- Permisos para capturar la ventana del juego

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# o .venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Ejecución

```bash
python src/main.py
```

## Importante

Este proyecto está en fase inicial. El README puede cambiar conforme se agreguen módulos y función real de detección.

## Licencia

MIT

## Nota final

Este bot está pensado para uso personal y educativo, y debe respetarse la política del juego y del cliente. No se recomienda automatizar acciones que puedan considerarse uso indebido o trampas.
