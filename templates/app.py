from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import io
import tensorflow as tf

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Cargar el modelo
generator = tf.keras.models.load_model('modelos/generator_model_reducido.h5')

# Ruta de la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario
@app.route('/generate', methods=['POST'])
def generate():
    # Obtener la imagen enviada desde el formulario
    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    
    # Preprocesar la imagen
    img = img.resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Generar una imagen falsa utilizando el modelo
    generated_img = generator.predict(img_array)
    generated_img = np.squeeze(generated_img, axis=0)
    generated_img = (generated_img * 255).astype(np.uint8)
    
    # Crear un objeto de imagen PIL para mostrarla en la página
    generated_img_pil = Image.fromarray(generated_img)
    
    # Guardar la imagen generada en un buffer
    buffer = io.BytesIO()
    generated_img_pil.save(buffer, format='JPEG')
    buffer.seek(0)
    
    # Renderizar la página con la imagen generada
    return render_template('result.html', generated_image=buffer.getvalue())

if __name__ == '__main__':
    app.run(debug=True)