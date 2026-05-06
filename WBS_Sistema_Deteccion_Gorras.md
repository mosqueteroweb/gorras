# WBS: Sistema de Detección de Gorras (Edge AI - Jetson Orin Nano)

Este documento contiene el Desglose de Tareas (Work Breakdown Structure) detallado para el desarrollo de la Prueba de Concepto (PoC) de detección de gorras utilizando hardware de borde (NVIDIA Jetson) y modelos de la familia Gemma.

---

## 1. Infraestructura Edge
*Configuración del hardware y el entorno de desarrollo local en la Jetson Orin Nano.*

| ID | Tarea | Descripción Técnica | Entregable |
| :--- | :--- | :--- | :--- |
| **1.1** | Configuración de Sistema Operativo | Flash de JetPack OS (6.x o superior) y actualización de repositorios (`apt update`). | Jetson operativa con acceso SSH y red. |
| **1.2** | Entorno de Desarrollo Python | Instalación de `virtualenv`, configuración de variables de entorno para CUDA y drivers de NVIDIA. | Entorno virtual aislado y funcional. |
| **1.3** | Dependencias de IA y Visión | Instalación de `PyTorch` (específico para Jetson), `Transformers` y `OpenCV` con soporte CUDA. | Script de prueba verificando acceso a la GPU. |
| **1.4** | Preparación del Modelo Gemma | Descarga del modelo `google/gemma-2b` desde Hugging Face y aplicación de cuantización (4-bit). | Modelo cargado en caché local. |

---

## 2. Pipeline de Visión (IA)
*Desarrollo del motor de inferencia encargado de procesar el stream de video.*

| ID | Tarea | Descripción Técnica | Entregable |
| :--- | :--- | :--- | :--- |
| **2.1** | Captura de Video (Camera Stream) | Implementación de `cv2.VideoCapture` para leer de cámara USB o CSI de forma eficiente. | Script `camera_test.py` operativo. |
| **2.2** | Preprocesamiento y Tiling | Transformación de frames (Resize, Normalización) para adaptarlos al input del modelo Gemma. | Función `preprocess_frame()` validada. |
| **2.3** | Lógica de Inferencia | Ejecución del modelo Gemma sobre los frames capturados para clasificar "Persona con Gorra". | Función `detect_hat()` devolviendo resultados. |
| **2.4** | Optimización de FPS | Ajuste del bucle de procesamiento para mantener una temperatura estable en la Jetson. | Bucle de visión estable a 3-10 FPS. |

---

## 3. Back-end y Web UI
*Estructura de almacenamiento local y visualización de resultados.*

| ID | Tarea | Descripción Técnica | Entregable |
| :--- | :--- | :--- | :--- |
| **3.1** | Servidor API (FastAPI) | Creación de un servicio local que expone rutas para recibir eventos y servir la web. | Servidor en `localhost:8000`. |
| **3.2** | Base de Datos (SQLite) | Diseño de esquema para logs de detección (ID, timestamp, cámara, ruta_imagen). | Archivo `detections.db` inicializado. |
| **3.3** | Sistema de Almacenamiento | Configuración de carpetas locales para el guardado de capturas fotográficas (confirmación). | Directorio `/captures/` gestionado por el API. |
| **3.4** | Dashboard (Front-end) | Interfaz web simple en Vanilla JS/Tailwind para visualizar la tabla de eventos y fotos. | UI de dashboard operativa en navegador. |

---

## 4. Integración End-to-End
*Unión de todas las partes en un sistema fluido y funcional.*

| ID | Tarea | Descripción Técnica | Entregable |
| :--- | :--- | :--- | :--- |
| **4.1** | Comunicación Visión-API | El script de IA envía una petición POST al servidor al confirmar una detección positiva. | Logs de IA apareciendo en tiempo real en BD. |
| **4.2** | Pipeline de Captura | Al detectar la gorra, se guarda el fotograma exacto en disco y se vincula su URL en el Dashboard. | Fotos de confirmación visibles en la UI. |
| **4.3** | Pruebas de Estrés y Logs | Monitoreo del sistema durante periodos extendidos usando `jtop` para validar viabilidad. | Reporte final de rendimiento y ajustes. |
