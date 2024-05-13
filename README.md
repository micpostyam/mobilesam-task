# API de segmentation d'images

Cette API permet de segmenter des images en utilisant un modèle de segmentation d'images.

## Installation et exécution avec Docker

1. **Clonez ce dépôt**

```bash
   git clone https://github.com/micpostyam/mobilesam-task
```
2. **Accédez au répertoire du projet**

```bash
    cd mobilesam-task
```
3. **Construisez l'image Docker**

```bash
    docker build -t segmentation-api .
```    

4. **Lancez le conteneur Docker**

```bash
    docker run -d -p 8000:8000 segmentation-api
```

## Utilisation

Envoyez une requête POST à l'URL http://localhost:8000/segment-image/ avec un fichier image en tant que corps de la requête pour segmenter l'image. Par exemple, vous pouvez utiliser l'outil cURL pour envoyer une requête :

```bash
    curl -X POST -F "file=@/chemin/vers/votre/image.jpg" http://localhost:8000/segment-image/ --output segmented_image.png
```
Cela téléchargera l'image segmentée enregistrée sous le nom segmented_image.png.

## Gestion des erreurs

-- Si vous rencontrez des erreurs lors de l'utilisation de l'API, assurez-vous que le fichier que vous envoyez est bien une image.
-- Si une erreur survient côté serveur, vous recevrez une réponse HTTP avec un code d'erreur 500 et un message détaillé sur l'erreur.

## Mise en cache

-- Les résultats de segmentation sont mis en cache pour améliorer les performances. Les résultats sont conservés en mémoire pendant une heure avant d'être purgés du cache.








## How to Run the Code

1. **Create a Virtual Environment and Activate It**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Code**

    ```bash
    python main.py
    ```

## Task Overview

**Title:** MobileSam Segmentation Model Service

**Expected Time to Complete:** 4 hours

**Objective:** Develop a FastAPI service to deploy the MobileSam segmentation model, containerize the service with Docker, and ensure efficient interaction with the model on the CPU.

**Background:**
MobileSam is a machine learning model specialized in image segmentation on CPUs. Your task is to create a microservice that allows users to interact with this model via an API. You should find the script `main.py` in this repository, which contains the MobileSam model and a function `segment_everything` that takes an image as input and returns the segmentation result. You can use this function to develop your service. Ignore the default parameters of the function for now.

## Task Description

- **Develop a Microservice:** Use a Python API framework (we suggest FastAPI) to expose the MobileSam segmentation model as a RESTful API.
  
- **Model Integration:** Incorporate the MobileSam segmentation model into your service. It should process image inputs and return segmentation results.
  
- **API Endpoints:** Create a POST endpoint `/segment-image` to accept an image file, process it through MobileSam, and return the segmentation result.
  
- **Documentation:** Provide clear instructions for setting up, running, and interacting with the service in a README.md file.

- **[Bonus]** Docker Familiarity: Containerize your service using Docker.

## Submission

- Submit your code via a GitHub repository link.
- Include a README file with detailed setup and usage instructions.
- Provide any necessary scripts or files for testing the API.
