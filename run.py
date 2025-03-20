from todor import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Utiliza el puerto desde la variable de entorno PORT o 5000 como predeterminado
    port = int(os.environ.get("PORT", 5000))
    # Ejecuta en 0.0.0.0 para que sea accesible desde fuera del entorno local
    app.run(host='0.0.0.0', port=port)