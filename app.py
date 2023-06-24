# -*- coding: utf-8 -*-
from flask import Flask, render_template
import numpy as np
from PIL import Image
import random
from keras.models import load_model
import os

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta de la página principal
@app.route('/')
def index():
    # Obtener una imagen aleatoria del directorio "/dataset_64x64/"
    original_images_dir = '/dataset_64x64/'
    original_images = os.listdir(original_images_dir)
    random_image = random.choice(original_images)
    random_image_path = os.path.join(original_images_dir, random_image)
    
    # Cargar los modelos y generar imágenes falsas
    generated_images = []
    gan_models_dir = '/modelos/'
    gan_models = [
        'infoGAN_generator_model_2_64x64.h5',
        'DCGAN_generator_model_2_64x64.h5',
        'GAN_simple_generator_weights.h5'
    ]
    for model_file in gan_models:
        model_path = os.path.join(gan_models_dir, model_file)
        generator = load_model(model_path)
        
        # Leer y preprocesar la imagen original
        img = Image.open(random_image_path).convert('RGB')
        img = img.resize((32, 32))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Generar una imagen falsa utilizando el modelo
        generated_img = generator.predict(img_array)
        generated_img = np.squeeze(generated_img, axis=0)
        generated_img = (generated_img * 255).astype(np.uint8)
        
        # Guardar la imagen generada en una lista
        generated_images.append(Image.fromarray(generated_img))
    
    return render_template('result.html', original_image=random_image_path, generated_images=generated_images)

if __name__ == '__main__':
    app.run(debug=True)
