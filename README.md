# DimPo Pred: A Machine Learning Web Application
Deployment of Machine learning models built [here](https://github.com/dopewevmond/fyp) using Flask and containerized using Docker.

## High level overview of how it works
* Users input canonical SMILES of the compound whose activity they want to predict using the ML models
* OpenBabel package is used to convert the SMILES of the compound to an `.sdf` file
* Mold2 is used to calculate the molecular descriptors of the compound from the `.sdf` file
* The molecular descriptors are used to make a prediction using the already trained and saved (pickled) models
* The output is displayed to the user

#### To work on this project locally:
Development environment: Linux. Python3 and pip should be installed
* Run `sudo apt-get update` to update all the packages on your system
* Run this command to install the Java Runtime environment (Mold2 depends on it) and the OpenBabel package for linux. `sudo apt install default-jre -y && sudo apt-get install openbabel -y`
* `cd` into the mold2 folder and make the file `Mold2` executable by running `sudo chmod +x ./Mold2`
* Clone this repository
* Create and activate virtual environment by running `python3 -m venv venv && source venv/bin/activate` in a terminal
* Install all dependencies by running `pip3 install -r /path/to/requirements.txt`
* Create a `.env` file in the root of your project and add the following variables
    * FLASK_APP=setup.py
    * FLASK_ENV=development
    * SECRET_KEY=`<some_secret_key>`
* `cd` into the root folder and run `flask run`


#### To run using Docker:
* Clone this repository
* Create a `.env` file in the root of your project and add the following variables
    * SECRET_KEY=`<some_secret_key>`
* Build a local Docker image by running the command `docker build -t <preferred-image-name> .`. Take care to not omit the full stop in the command
* After the image builds successfully, you can create and run a Docker container from the image by running `docker run --name <preferred-container-name> --env-file=.env -p 8000:8080 <preferred-image-name>`. This exposes port 8080 of the container where the application is running (check Dockerfile if in doubt) to port 8000 on your host machine. You can now access the web application at `http://localhost:8000`.
