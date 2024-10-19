# Iris Flower Species Prediction & Chatbot with LLaMA

## Overview

This repository contains two main projects:

1. **Iris Flower Species Prediction**: A simple web-based machine learning application that predicts the species of an Iris flower based on its sepal and petal dimensions using a decision tree model.
2. **Chatbot Interface with LLaMA**: A web interface for interacting with a chatbot powered by the LLaMA model.

### Iris Prediction App

This application uses a pre-trained decision tree model to predict the species of an Iris flower. Users can input sepal and petal dimensions through a web interface built with Streamlit, and the model will predict whether the flower is of the species *Iris-setosa*, *Iris-versicolor*, or *Iris-virginica*.

### Chatbot App

The chatbot uses the LLaMA model to provide conversational interactions via a simple web interface.

## Features

### Iris Prediction App
- Input sepal and petal dimensions via sliders.
- Predicts Iris species using a machine learning model.
- Provides an easy-to-use interface built with Streamlit.

### Chatbot Interface
- Web-based interface to interact with LLaMA model.
- Simple and intuitive user design.

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- `pip` for Python package management

### Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Install Dependencies**:

    Use the provided `requirements.txt` file to install the necessary Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download the Pre-trained Model**:

    Make sure you have the decision tree model file `decision_tree_model.joblib` in the appropriate directory (e.g., `C:/Users/Home/Desktop/ids5/TP1_MLOPS_Streamlit/` as specified in the `app.py` file). If not, either train the model yourself using `model.ipynb` or update the path in `app.py`.

4. **Run the Iris Prediction App**:

    ```bash
    streamlit run app.py
    ```

    This will launch the Streamlit web app for predicting the species of Iris flowers. Open the URL provided in the terminal to interact with the app.

5. **Run the Chatbot App**:

    To launch the chatbot interface, ensure the `chatbot.py` file is correctly configured, then run:

    ```bash
    python chatbot.py
    ```

## Usage

### Iris Prediction App

- Open the Streamlit app in your browser.
- Adjust the sepal and petal dimensions using the sliders.
- Click the "Prédire l'espèce de la fleur" button to get the predicted species.

### Chatbot App

- Interact with the LLaMA-powered chatbot via the web interface. You can ask questions, have casual conversations, or test its capabilities.

## Files

- `app.py`: The main file for the Iris flower species prediction app.
- `chatbot.py`: The main file for the chatbot interface.
- `model.ipynb`: Jupyter notebook for training the decision tree model.
- `decision_tree_model.joblib`: Pre-trained model for Iris prediction.
- `prediction.py`: Contains the logic for loading the model and making predictions.
- `requirements.txt`: List of required Python packages.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to contribute by forking this repository and submitting pull requests. Any improvements or bug fixes are welcome!
