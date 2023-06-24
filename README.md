# Proyecto de Generación de Imágenes de Grietas en el Asfalto

Este proyecto es parte del trabajo final del Máster en Inteligencia Artificial y tiene como objetivo desarrollar modelos GAN (Generative Adversarial Networks) para generar imágenes realistas de grietas en el asfalto y otros tipos de daños.

## Colaboradores

- Guillermo San Vicente Frías
- María Inmaculada García Hernández
- Pablo Bolivar López
- Roberto Jiménez García

## Descripción

El proyecto se centra en la aplicación de diferentes arquitecturas de GAN para la generación de imágenes de grietas en el asfalto. Se han utilizado los siguientes modelos:

- InfoGAN
- DCGAN (Deep Convolutional GAN)
- WGAN (Wasserstein GAN)
- pix2pix GAN

Se ha creado un conjunto de datos que contiene aproximadamente 3000 imágenes de grietas en el asfalto y otros tipos de daños. Los modelos han sido entrenados utilizando estos datos y los notebooks correspondientes se encuentran en el directorio `notebooks/`.

## Estructura del Repositorio

- `notebooks/`: Contiene los notebooks utilizados para entrenar y evaluar los modelos GAN.
- `dataset_64x64/`: Directorio que almacena el conjunto de datos de imágenes de grietas en el asfalto.
- `modelos/`: Directorio que almacena los modelos entrenados compilados con extension h5.
- `templates/`: Directorio con plantillas.
- `imagenes generadas/`: directorio con imagenes obtenidas mediante los modelos.
- `app.py`: El archivo app.py contiene la implementación de una API basada en Flask para generar imágenes utilizando modelos GAN. La API carga modelos pre-entrenados y permite generar imágenes a partir de imágenes de entrada.
- `index.html`: El archivo index.html es la página principal de la aplicación web. Proporciona un formulario donde se puede ingresar un vector latente y generar una imagen utilizando los modelos GAN.
- `result.html`: El archivo result.html muestra el resultado de la generación de imágenes. Muestra la imagen generada a partir del vector latente proporcionado en la página anterior.

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local: https://github.com/Robertuelo/TFM_GAN_CRACKS
2. Configura tu entorno de desarrollo de acuerdo a las dependencias y requisitos mencionados en los notebooks.
3. Explora los notebooks en el directorio `notebooks/` para entender cómo se han implementado y entrenado los modelos GAN.
4. Utiliza el conjunto de datos en el directorio `dataset/` para entrenar tus propios modelos o generar nuevas imágenes de grietas en el asfalto.
