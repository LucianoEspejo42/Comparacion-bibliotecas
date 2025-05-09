from app import app
import os

# Crear carpeta docs si no existe
if not os.path.exists('docs'):
    os.makedirs('docs')

# Cliente de prueba
with app.test_client() as test_client:
    # Página principal
    response = test_client.get('/')
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(response.data.decode('utf-8'))

    # Página de Matplotlib
    response = test_client.get('/libreria/matplotlib')
    with open('docs/matplotlib.html', 'w', encoding='utf-8') as f:
        f.write(response.data.decode('utf-8'))

    # Página de Plotly
    response = test_client.get('/libreria/plotly')
    with open('docs/plotly.html', 'w', encoding='utf-8') as f:
        f.write(response.data.decode('utf-8'))

    # Página de Bokeh
    response = test_client.get('/libreria/bokeh')
    with open('docs/bokeh.html', 'w', encoding='utf-8') as f:
        f.write(response.data.decode('utf-8'))

print("¡Sitio estático generado con éxito en la carpeta docs/")
