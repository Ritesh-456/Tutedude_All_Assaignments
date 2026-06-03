# TuteDude Assignments Repository 🚀

Welcome to my central hub for tracking all my TuteDude assignments! This space is designed to keep everything organized, neat, and easy to find as I progress through the course.

Currently, this repository contains my work for the first seven assignments:

### 📁 [Assignment_1](./Assignment_1)
This folder holds my work for the very first assignment. It covers the introductory concepts and initial tasks to get things started.

### 📁 [Assignment_2](./Assignment_2)
In this folder, you'll find my solutions for the second assignment. This one dives into more advanced Python data science tools! It features hands-on exercises covering:
* **NumPy:** Array creation and mathematical operations.
* **Pandas:** Data manipulation, filtering, and grouping using DataFrames.
* **Matplotlib:** Data visualization through line plots, bar charts, pie charts, and histograms.

### 📁 [Assignment_3](./Assignment_3)
This folder contains my solutions for the third assignment covering Probability (Module 13). It includes a Jupyter Notebook that uses beginner-friendly Python to simulate:
* Coin tosses and dice rolls.
* Conditional probability and Bayes' Theorem verifications.
* Discrete and Exponential continuous random variables distributions.
* The Central Limit Theorem (CLT) simulation and visualization.

### 📁 [Assignment_4](./Assignment_4)
This folder contains my Module 21 KNN Case Study on Diabetes. It features:
* A Jupyter Notebook applying the K-Nearest Neighbors (KNN) algorithm.
* Steps for missing data handling, standardizing features, and creating a target prediction column.
* Model evaluation using accuracy scores and confusion matrices.
* The original Kaggle Diabetes dataset (`diabetes.csv`).

### 📁 [Assignment_5](./Assignment_5)
This folder contains my completely revised Module 22 Naive Bayes Case Study on the **Authentic Titanic dataset**. It features:
* An extensive **Exploratory Data Analysis (EDA)** section with 5+ visualizations using `seaborn` and `matplotlib`.
* In-depth Data Preprocessing with imputation and encoding.
* Class Imbalance Mitigation by comparing standard `GaussianNB` with `LogisticRegression(class_weight='balanced')`.
* Robust evaluation using K-Fold Cross Validation, side-by-side Confusion Matrices, and Classification Reports addressing recall constraints.
* The original Kaggle Titanic dataset (`Titanic-Dataset.csv`).

### 📁 [Assignment_6](./Assignment_6)
This folder contains my Module 26 Sales Forecasting Case Study. It features:
* A Jupyter Notebook applying predictive modeling (Linear Regression) to predict sales over time.
* Data preprocessing steps including converting string dates to datetime formats and daily aggregation.
* Feature extraction (Year, Month, Day) for machine learning models.
* Model evaluation using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.
* The original Kaggle Superstore Sales forecasting dataset (`train.csv`).

### 📁 [Assignment_7](./Assignment_7)
This folder contains my Module 27 Cardiac Diagnostics Case Study. It features:
* A Jupyter Notebook applying a Machine Learning classification model (Random Forest Classifier).
* Medical data preprocessing steps including mapping categorical text and standardizing continuous variables via `StandardScaler`.
* Model evaluation using Accuracy, Confusion Matrix, Precision, Recall, and F1-score.
* The original Kaggle Heart Disease Prediction dataset (`Heart_Disease_Prediction.csv`).

---

## 🚀 How to Run

To test out these assignments and run the code on your own machine, follow these instructions:

### Prerequisites
You need Python installed, along with Jupyter Notebook or VS Code to open `.ipynb` files. You also need the required libraries.
1. Open your terminal or command prompt.
2. Install the necessary libraries by running:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

### Running the Notebooks
1. Navigate to the folder of the assignment you want to check (e.g., `cd Assignment_5`).
2. Open the `.ipynb` file in your preferred editor (VS Code, JupyterLab, etc.).
3. Run the cells sequentially from top to bottom.
4. **Expected Output:** You should see dataframes printed as tables, statistical summaries, and performance metrics. Some assignments will also generate visualizations and charts right below the code cells!
