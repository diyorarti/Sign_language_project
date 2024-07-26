import os
import sys
import yaml
import shutil
import zipfile
import subprocess
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainingConfig
from signLanguage.entity.artifacts_entity import ModelTrainingArtifact

class ModelTrainer:
    def __init__(self, model_training_config: ModelTrainingConfig):
        self.model_training_config = model_training_config

    def initiate_model_trainer(self) -> ModelTrainingArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            with zipfile.ZipFile("Sign recoginition.v1i.yolov5pytorch.zip", 'r') as zip_ref:
                zip_ref.extractall()

            os.remove("Sign recoginition.v1i.yolov5pytorch.zip")

            # Ensure the data.yaml file is properly formatted
            data_yaml_path = "data.yaml"
            with open(data_yaml_path, 'r') as stream:
                data_yaml = yaml.safe_load(stream)
                if 'val' not in data_yaml:
                    raise ValueError("data.yaml 'val:' field missing")

            num_classes = str(data_yaml['nc'])
            model_config_file_name = self.model_training_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)

            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            # Change directory and run the command using subprocess
            command = [
                'python', 'train.py',
                '--img', '416',
                '--batch', '16',
                '--epochs', '1',
                '--data', '../data.yaml',
                '--cfg', './models/custom_yolov5s.yaml',
                '--weights', 'yolov5s.pt',
                '--name', 'yolov5s_results',
                '--cache'
            ]
            subprocess.run(command, cwd="yolov5", check=True)


            shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", "yolov5/best.pt")
            os.makedirs(self.model_training_config.model_trainer_dir, exist_ok=True)
            shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", os.path.join(self.model_training_config.model_trainer_dir, "best.pt"))

            shutil.rmtree("yolov5/runs", ignore_errors=True)
            shutil.rmtree("train", ignore_errors=True)
            shutil.rmtree("test", ignore_errors=True)
            os.remove(data_yaml_path)

            model_training_artifact = ModelTrainingArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_training_artifact}")

            return model_training_artifact

        except Exception as e:
            raise SignException(e, sys)

