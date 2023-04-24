# Flask Emotion Recognition API

## INSTRUCTIONS

1. Download the latest version of Python from https://www.python.org/downloads/.
2. Navigate to the root folder of this project containing **app.py** and run ***pip install -r requirements.txt*** (in case this doesnt work, see **Dependecies**).
3. Once all the dependencies are installed, run ***flask run*** in the root of the project.
4. Ensure that the Flutter web app is also running to test the API.
5. Test the API with Flutter open.

## Dependencies

All the  dependencies required for this project are contained in the ***requirements.txt*** file found in the root of the Flask project. When running the project for the first time, run ***pip install -r requirements.txt*** to install all these dependencies. In case the dependencies are not automatically downloaded, run ***pip install DEPENDENCY***, replacing **Dependency** with each dependency name. The list of dependencies with the specific versions are as below:

1. flask
2. opencv-python
3. deepface==0.0.75
4. numpy