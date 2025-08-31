🌱 Sustainable Agriculture Using Machine Learning & Deep Learning Algorithms


📌 Project Overview

This project focuses on building a data-driven approach to analyze agricultural datasets and predict crop yield trends. By leveraging Machine Learning (ML) and Deep Learning (DL) models, the system helps in improving agricultural planning, food security, and sustainable farming practices.

The project is divided into milestones:

Week 1: Data Collection, Cleaning, and Exploratory Data Analysis (EDA)

Week 2: Model Building (Machine Learning + Deep Learning)

Week 3 (Final): Streamlit Deployment, GitHub Documentation, and Final Report Submission

├── crop_production.csv        # Raw dataset
├── crop_yield_cleaned.xls     # Cleaned dataset
├── crop_yield_prediction.py   # Streamlit app code
├── SUSTAINABLE AGRICULTURE USING MACHINE LEARNING DEEP LEARNING ALGORITHMS.ipynb # Jupyter notebook with full pipeline
└── README.md                  # Project documentation

⚙️ Steps in the Project
🔹 Step 1: Data Cleaning

Removed missing values, duplicates, and inconsistencies

Standardized units (Production in tonnes, Area in hectares)

Saved final dataset as crop_yield_cleaned.xls

🔹 Step 2: Exploratory Data Analysis (EDA)

Yield Distribution across crops

Top 10 crops by total production

Production trend by year (time-series analysis)

Correlation analysis of Area vs Production

🔹 Step 3: Machine Learning Models

Linear Regression

Random Forest Regressor

XGBoost

🔹 Step 4: Deep Learning Model

Neural Network (Keras/TensorFlow) for crop yield prediction

🔹 Step 5: Streamlit Deployment

Built an interactive web app with Streamlit

User can upload crop data and get yield predictions instantly

File: crop_yield_prediction.py

🚀 How to Run the Project
🔧 Local Setup
git clone https://github.com/YOUR-USERNAME/SUSTAINABLE-AGRICULTURE-USING-MACHINE-LEARNING-DEEP-LEARNING-ALGORITHMS.git
cd SUSTAINABLE-AGRICULTURE-USING-MACHINE-LEARNING-DEEP-LEARNING-ALGORITHMS

pip install -r requirements.txt

jupyter notebook

streamlit run crop_yield_prediction.py

📊 Results

The Random Forest model achieved the highest accuracy among ML models.

Deep Learning model performed well with larger datasets.

Visual EDA provided insights into crop patterns & sustainability trends.

🌍 Real-World Applications

Crop yield prediction for farmers

Government policy-making for food security

Sustainable agriculture planning

AI-based decision support for agri-business

👩‍💻 Author

Brijeshrath67
Sustainable Agriculture Research Enthusiast | Machine Learning & Deep Learning Developer

📜 License

This project is licensed under the MIT License – free to use and modify.
