# faceRecognitionBundle
Sample face recognition bundle written on Python3. Uses opencv, numpy packages and sqllite for storing user information.

## Getting started
Fist of all you need to install all required packages, that located in requirements.txt. Then try to run **testingFaceRecognition.py** to test your webcam and facial recognition algorithm, that was provided by **opencv-contrib-python** package

### Package installation
In file **requirements.txt** you will find all names of the packages, that needed for running this project. To install - create new virtualenv first, or if you don't need one, simply run following command in your terminal:

```sh
pip3 install -r requirements.txt
```

### Usage

#### 1. testingFaceRecognition.py
Run this script to test your webcam is working and opencv package is up and running. New window will open with capturing feed from your webcam
and if human face presented in the feed, square will be drawn around it (if face detection algorithm is working).

#### 2. creatingDataset.py
Run this script to create dataset from capture of your webcam. You will need to insert userId and userName to save information to sqlite database. **NOTE: before running this script, remove sample image from dataset_users folder**
Algorithm finds the human face, then saves image to folder for further training.

#### 3. trainingOnDataset.py
Run this script to create model, that based on LBPH algorithm. Output is YAML file (**trainingUserData.yml**) which will be stored in the recognition folder.

#### 4. detectFacesFromWebcam.py
After all the steps, you can run this script to test you computed model. New window will be opened with feed from your webcam
and if human face or faces are presented in the feed, square (if face detection algorithm is working) will be drawn around them with addition information from sqlite database.

### DB structure
In this sample, sqlite database, that named **FacesDB.db**, is used. Just one table are enough:

| NAME | TYPE |
| ------ | ------ |
| ID | INT |
| NAME | TEXT |
| AGE | INT |
| GENDER | TEXT |
| ROLL_NO | TEXT |

### Future work
(if it's gonna be)

Need to test other algorithms (Eigenfaces, Fisherfaces, Scale Invariant Feature Transform (SIFT), Speed Up Robust Features (SURF))
to test which is better for face recognition.
