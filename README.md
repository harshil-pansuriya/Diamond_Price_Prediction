# Diamond Price Prediction

## Overview

This project implements a machine learning solution for predicting diamond prices based on various characteristics. The system uses features such as carat weight, cut, color, clarity, and dimensions to provide accurate price estimations.

## Features

- Data pipeline for ingestion and transformation
- Multiple regression models (Linear Regression, Lasso, Ridge, ElasticNet, Decision Tree)
- Automated model selection based on best performance
- Web interface for real-time predictions
- Comprehensive logging system
- Custom exception handling

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/Diamond_Price_Prediction.git
   ```

2. Create and activate virtual environment:
   ```
   python -m venv env_name
   env_name/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Training Pipeline

To train the model:
`    python src/pipelines/training_pipeline.py
   `

### Web Application

To run the Flask application:
`    python application.py
   `
Access the web interface at `http://localhost:5000/predict`

## Input Features

The model accepts the following diamond characteristics:

- carat: Weight of the diamond (0.2-5.01)
- cut: Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- color: Diamond color, from J (worst) to D (best)
- clarity: Clarity grade (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
- depth: Total depth percentage (43-79)
- table: Width of top of diamond relative to widest point (43-95)
- x: Length in mm (0-10.74)
- y: Width in mm (0-58.9)
- z: Depth in mm (0-31.8)

## Model Details

The system evaluates multiple regression models:

- Linear Regression
- Lasso Regression
- Ridge Regression
- Elastic Net
- Decision Tree Regressor
