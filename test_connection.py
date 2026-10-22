import base64
import requests

def test_connection_simple():
    # Intentamos con la ruta estándar de OpenAI
    url = "http://127.0.0.1:1234/v1/chat/completions"

    # Un pixel rojo 1x1 en formato JPEG base64
    base64_image = "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAABAAEDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDBAIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1FVWV1hZWmNkZWZnaGlqc3R1dnd4eXqGhcXHyMnKy9PU1lW14uPk5ebn6Onq8fLz90fX3+Pn6/9oADAMBAAIRAxEAPwAf/9k="

    payload = {
        "model": "google/gemma-4-e2b", # Nombre exacto del identificador en LM Studio
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                    {"type": "text", "text": "¿Hay alguien con gorra en esta imagen? Responde solo Sí o No"}
                ]
            }
        ],
        "max_tokens": 10
    }

    try:
        print(f"Enviando petición a {url}...")
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
        response.raise_for_status()
        print("Respuesta recibida:")
        print(response.json()['choices'][0]['message']['content'])
    except Exception as e:
        print(f"Error al conectar con LM Studio: {e}")

if __name__ == "__main__":
    test_connection_simple()
