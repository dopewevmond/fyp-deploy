# DimPo Pred: A Machine Learning Web Application
Deployment of Machine Learning models built [here](https://github.com/dopewevmond/fyp) using Flask.

## High level overview of how it works
* Users input canonical SMILES of the compound they want to predict
* OpenBabel package is used to convert the SMILES of the compound to an `.sdf` file
* Mold2 is used to calculate the molecular descriptors of the compound from the `.sdf` file
* The molecular descriptors are used to make a prediction using the already trained and saved (pickled) models
* The output is displayed to the user

## To work on this project locally:
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
