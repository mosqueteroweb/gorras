# Registro de Conversación 01 - Proyecto Detección de Gorras

## Contexto del Proyecto
Desarrollo de una PoC (Prueba de Concepto) para la detección de personas usando gorras en tiempo real, destinada a ejecutarse en una **NVIDIA Jetson Orin Nano**.

## Configuración Técnica Inicial
- **Backend de IA:** LM Studio ejecutándose localmente en `http://127.0.0.1:1234`.
- **Modelo:** Gemma-2b (VLM) con capacidades de visión, compatible con la API de OpenAI.
- **Hardware de desarrollo:** Equipo local con cámara conectada (índice 0).
- **Hardware de despliegue final:** Jetson Orin Nano.
- **Software:** Python, OpenCV, FastAPI.

## Decisiones Tomadas
1. **Local vs Cloud:** Se descartó el uso de GitHub Pages/Actions para el alojamiento de la web y el procesamiento debido a:
    - Necesidad de acceso a hardware local (cámara).
    - Latencia en el procesamiento de frames.
    - Seguridad y conectividad con el localhost (LM Studio).
2. **Interfaz de Usuario:** Se desarrollará una página web local (FastAPI) que muestre el stream de la cámara en tiempo real y registre las detecciones.
3. **Frecuencia de Procesamiento:** Objetivo de ~10 FPS (ajustable según rendimiento del modelo).
4. **Prompt de Visión:** "¿Hay alguien con gorra en esta imagen? Responde solo Sí o No".

## Plan de Implementación Acordado
1. **Fase 1: Conexión IA:** Validar API de LM Studio con `test_vlm.py`.
2. **Fase 2: Motor de Visión:** Captura de video y lógica de detección asíncrona.
3. **Fase 3: Backend FastAPI:** Streaming de video y base de datos SQLite para logs.
4. **Fase 4: Frontend Web:** Dashboard en tiempo real con Vanilla JS/Tailwind.
5. **Fase 5: Integración y Optimización:** Ajustes finales de rendimiento.
6. **Pre-commit y Entrega:** Verificación total y entrega de código.
