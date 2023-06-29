import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, send_file
from keras.models import load_model
import io
import random
import shutil

app = Flask(__name__)

# Registrar la función 'enumerate' en el entorno de Jinja2
app.jinja_env.globals['enumerate'] = enumerate

# Ruta de la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para generar y mostrar las imágenes
@app.route('/generate', methods=['POST'])
def generate_images():
    # Obtener el valor del vector de ruido del formulario
    noise_value = float(request.form['noise'])

    # Cargar los modelos y generar imágenes falsas
    generated_images = []
    gan_models_dir = 'modelos/'
    gan_models = [
        'infoGAN_generator_model_2_64x64.h5',
        'DCGAN_generator_model_2_64x64.h5'
    ]
    for model_file in gan_models:
        model_path = os.path.join(gan_models_dir, model_file)
        generator = load_model(model_path)

        # Generar una imagen falsa utilizando el modelo y el vector de ruido
        noise = np.random.randn(1, 100) * noise_value
        generated_img = generator.predict(noise)
        generated_img = np.squeeze(generated_img, axis=0)
        generated_img = (generated_img * 255).astype(np.uint8)

        # Guardar la imagen generada en una lista
        generated_images.append(Image.fromarray(generated_img))

    # Obtener una imagen aleatoria del directorio dataset_64x64
    dataset_dir = 'dataset_64x64/'
    dataset_images = os.listdir(dataset_dir)
    random_image_file = random.choice(dataset_images)
    random_image_path = os.path.join(dataset_dir, random_image_file)

    # Copiar la imagen aleatoria al directorio de descarga
    download_dir = 'downloads/'
    os.makedirs(download_dir, exist_ok=True)
    random_image_copy_path = os.path.join(download_dir, 'random_image.jpg')
    shutil.copy(random_image_path, random_image_copy_path)

    # Guardar las imágenes generadas en el directorio de descarga
    generated_image_paths = []
    for i, image in enumerate(generated_images):
        generated_image_path = os.path.join(download_dir, f'generated_image_{i}.jpg')
        image.save(generated_image_path)
        generated_image_paths.append(generated_image_path)

    return render_template('result.html', generated_images=generated_image_paths, random_image=random_image_copy_path)

# Ruta para descargar las imágenes generadas
@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


