# Proyecto de Detección de Fatiga - Programación Avanzada - UNAB

Este proyecto implementa un sistema de detección de fatiga en conductores utilizando Python y OpenCV. Utiliza técnicas de procesamiento de imágenes para monitorear el estado del conductor en tiempo real y detectar signos de somnolencia

## Funcionalidades

- **Detección de Fatiga en Tiempo Real:** Utiliza una cámara para capturar imágenes del conductor y procesarlas en tiempo real para detectar signos de fatiga.
- **Indicación Visual de Somnolencia:** Marca visualmente las imágenes capturadas con indicaciones cuando se detecta somnolencia.
- **Interfaz de Usuario Simple:** Muestra la salida de detección en una ventana de visualización de OpenCV de manera intuitiva y fácil de entender.

## Requisitos

1. Python 3.x
2. Las siguientes librerías de Python:

    ```
    opencv-python
    dlib
    numpy
    scipy
    ```

    Para instalar estas dependencias, usamos `requirements.txt` incluido en el proyecto.



## Configuración del Proyecto

Para utilizar este proyecto, sigue estos pasos:

### Instalación de Dependencias

1. **Python y Pip:**
   - Descarga e instala Python desde la [página oficial de Python](https://www.python.org/downloads/).
   - Asegúrate de seleccionar la opción "Add Python to PATH" durante la instalación.
   - Pip generalmente se instala automáticamente con Python. Verifica la instalación de pip ejecutando `pip --version` en tu terminal.

2. **Git:**
   - Descarga e instala Git desde la [página oficial de Git](https://git-scm.com/downloads).

3. **Clonar el Repositorio:**
   - Clona este repositorio desde GitHub:
     ```bash
     git clone https://github.com/PereiraMauro/TP-OpenCV.git
     cd TP-OpenCV
     ```
4. **Instalación de paquetes Python:**
   - Abre una terminal en el directorio del proyecto.
   - Ejecuta el siguiente comando para instalar las dependencias necesarias:
     ```bash
     pip install -r requirements.txt
     ```

### Ejecución del Proyecto

1. **Dirigirse hacia la ruta del proyecto:**
     ```bash
     cd TP-OpenCV
     ```  

2. **Ejecutar el Proyecto:**
   - Ejecuta el script principal `main.py` para iniciar el sistema de detección de fatiga:
     ```bash
     python main.py
     ```

3. La aplicación comenzará a capturar video desde la cámara que se tenga instalada por defecto y mostrará la ventana de detección de fatiga. Si se detecta fatiga, se mostrará un mensaje de alerta y se emitirá un sonido.

---


