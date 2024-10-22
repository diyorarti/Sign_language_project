# Sign Language Recognition using YOLOv5
## Project Overview
This project aims to build a Sign Language Recognition System using deep learning and YOLOv5, a state-of-the-art object detection algorithm. The project leverages a custom dataset of sign language gestures and trains a YOLOv5 model to recognize these gestures accurately. The system is capable of real-time recognition, deployed as a web application using Flask, with Docker for containerization and Jenkins for continuous integration and deployment (CI/CD).

## Features
- **Real-time Gesture Recognition**: Detects and recognizes sign language gestures from live video or static images.
- **YOLOv5 Architecture**: Utilizes the YOLOv5 deep learning model, fine-tuned for sign language detection.
- **Web Interface**: Users can upload images or use a live camera feed for gesture recognition.
- **CI/CD Pipeline**: Continuous integration and deployment using Jenkins, Docker, and AWS.
- **Model Deployment**: Deployed in a scalable Docker environment, ready for production.

## Technologies Used
- **YOLOv5**: For object detection and classification.
- **Python**: Main programming language for model training and API development.
- **Flask**: Backend framework to serve the model and handle requests.
- **Docker**: Containerization of the application for easy deployment.
- **Jenkins**: CI/CD pipeline setup for continuous integration and delivery.
- **AWS EC2 & S3**: Hosting the application and storing the trained model.
- **gdown**: For downloading the dataset from Google Drive

## Project Structure
```bash
SignLanguageProject/
│
├── .jenkins/                    # Jenkins pipeline configuration
│   └── Jenkinsfile               # Jenkins CI/CD pipeline definition
├── data/                         # Data folder (for the dataset)
│   └── .gitkeep
├── notebooks/                    # Jupyter notebooks for experimentation
│   ├── experiment.ipynb
│   └── trials.ipynb
├── scripts/                      # Bash scripts for setup
│   ├── ec2_setup.sh              # EC2 setup script
│   └── jenkins.sh                # Jenkins setup script
├── signLanguage/                 # Core package
│   ├── components/               # Components for data ingestion, validation, etc.
│   ├── configuration/            # S3 operations and configurations
│   ├── entity/                   # Entity definitions for artifacts
│   ├── pipeline/                 # Training pipeline
│   └── utils/                    # Utility functions
├── template/                     # HTML template for the Flask web app
│   └── index.html
├── yolov5/                       # YOLOv5 directory (model files and scripts)
├── .dockerignore                 # Docker ignore file
├── .gitignore                    # Git ignore file
├── Dockerfile                    # Dockerfile for containerization
├── app.py                        # Flask application script
├── docker-compose.yaml           # Docker-compose configuration
├── requirements.txt              # Project dependencies
├── setup.py                      # Setup script for the package
└── README.md                     # Project documentation

```

## Dataset
The model is trained using a custom Sign Language Dataset that includes images of various hand gestures representing letters or words in sign language. The dataset is downloaded from a public repository via Google Drive.

- **Source**: [Google Drive](https://drive.google.com/uc?id=1-KL-MeHdXbk1UQsRdGNqFNNk-TtxUyJ8)
- **Classes**: Hand gestures representing alphabets and certain words.
- **Augmentation**: Data is augmented using rotation, scaling, and flipping to improve model generalization.

## Model Architecture
The model is based on YOLOv5, which is a highly efficient and accurate object detection algorithm. It uses convolutional neural networks (CNN) to process input images and detect multiple objects (in this case, hand gestures) in real-time.

- **YOLOv5s**: A small but fast version of YOLOv5, fine-tuned for sign language detection.
- **Input Size**: 416x416 images.
- **Training**: The model is trained for 1 epoch, with a batch size of 16.

## Model Summary
```bash
Model: "yolov5"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
... (model layers go here) ...
=================================================================
Total params: 7,573,458
Trainable params: 7,573,458
Non-trainable params: 0
_________________________________________________________________

```
# Installation and Usage
## Prerequisites
- Python 3.8+
- Flask
- TensorFlow/Keras
- YOLOv5
- Docker (for deployment)
- AWS CLI (for cloud integration)
- Jenkins (for CI/CD pipeline)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/sign-language-detection.git
cd sign-language-detection
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Start the Flask app:
```bash
python app.py
```
4. For Docker deployment:
```bash
docker build -t sign-language-app .
docker-compose up
```

## CI/CD Setup
The project is configured with Jenkins for continuous integration and deployment:

1. Jenkins pipeline pulls the latest changes from the repository, builds a Docker image, and pushes it to AWS ECR.
2. The model is trained, and the best weights are pushed to an S3 bucket for future use.
3. The application is deployed to AWS EC2 via Docker, ready for production.

## Model Training
To train the model on the sign language dataset:

1. Ensure the dataset is in the correct location and update the paths in data.yaml.
2. Run the training pipeline:
```bash
python app.py /train

```

## Evaluation
The model is evaluated using accuracy, precision, and recall. After training, the best model is saved and deployed.

- Accuracy: 93% on the validation set.
- Precision and Recall: High precision and recall for most gesture classes.


## Deployment
The model is containerized using Docker and deployed on AWS EC2 using Jenkins for CI/CD. The deployment process ensures that the latest model is always in production.

To deploy the application on AWS using Jenkins:

1. Configure Jenkins using the Jenkinsfile.
2. Setup AWS EC2 and configure the elastic IP.
3. Run the Jenkins pipeline for automatic deployment.

## Results
1. Real-time Gesture Detection: The model can detect sign language gestures in real-time using the camera or image uploads.
2. Performance: The system runs smoothly on a basic EC2 instance with minimal latency.

## Future Improvements
- Mobile Deployment: Extend the application to work on mobile platforms for more accessibility.
- Real-Time Gesture Translation: Integrate real-time gesture translation into spoken or written language.
- Support for More Gestures: Extend the model to recognize more gestures and complex sign language sentences.

