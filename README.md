# Laptop_Price_Prediction Model

This project predicts laptop prices using supervised machine learning techniques. It includes robust data preprocessing, feature engineering, multiple regression models, hyperparameter tuning, and performance evaluation to deliver accurate price estimates based on real laptop specifications.

---

## Dataset

- **Source:** Kaggle — Laptop Price Prediction Dataset (collected 6 months ago)
- **Description:** Contains detailed laptop specifications, user ratings, and actual selling prices.
- **Purpose:** Used to train, test, and evaluate regression models to predict fair market prices.

---

## Attributes

- **name**: Laptop brand/model name.
- **price**: Actual selling price (target variable).
- **spec_score**: Combined score of specifications.
- **votes**: Number of user votes.
- **user_rating**: Average user rating.
- **os**: Operating system.
- **utility**: Intended use (e.g., Gaming, Business).
- **thickness**: Physical thickness.
- **weight**: Weight of the laptop.
- **warranty**: Warranty period.
- **screen_size**: Screen size in inches.
- **resolution**: Screen resolution (e.g., 1920x1080).
- **ppi**: Pixels per inch.
- **battery**: Battery capacity or backup.
- **screen_feature1**: Additional screen feature (e.g., touchscreen).
- **screen_feature2**: Another screen feature (e.g., IPS/OLED).
- **processor_name**: Processor type.
- **processor_speed**: Processor clock speed.
- **no_cores**: Number of CPU cores.
- **caches**: Processor cache size.
- **graphics_card**: GPU name/type.
- **ram_memory**: RAM capacity.
- **internal_memory**: Internal storage capacity.
- **port_connection**: Available physical ports.
- **wireless_connection**: Supported wireless technologies.
- **usb_ports**: Number/type of USB ports.
- **hardware_features**: Other hardware highlights.

---

## **Preprocessing Techniques**

The project applies thorough **data preprocessing** to ensure clean and reliable input for the models:

- **Duplicate Removal:** Detected and removed duplicate records to avoid bias.
- **Missing Value Handling:** Identified and handled null or missing values appropriately.
- **Outlier Handling:** Applied IQR (Interquartile Range) method to detect and cap extreme outliers.
- **Skewness Correction:** Checked feature distributions using mean and median; transformed skewed data to improve model learning.
- **Feature Extraction:** Extracted detailed information from combined or complex attributes (e.g., resolution split, processor details).
- **Encoding:** Converted categorical variables to numeric using `OneHotEncoder`.
- **Scaling:** Standardized numerical features using `StandardScaler` to normalize value ranges.
- **Column Transformation:** Used `ColumnTransformer` to apply different preprocessing steps to relevant columns.
- **Pipeline:** Built a `Pipeline` to combine preprocessing and model training for efficient, repeatable execution.

---

## **Machine Learning Techniques Applied**

Multiple regression algorithms were implemented and compared to find the best model for price prediction:

- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **XGBoost Regressor**
- **LightGBM Regressor**
- **Gradient Boosting Regressor (final best model)**

Hyperparameter tuning was performed, with the **Gradient Boosting Regressor** achieving the highest **R² score of 89%**.

---

## **System Approach**

- The system is developed in Python using libraries like `pandas`, `numpy`, `scikit-learn`, `xgboost`, `lightgbm`, `matplotlib`, and `seaborn`.
- Data is collected, cleaned, transformed, and split into training and testing sets.
- Various models are trained, tuned, and compared to select the most accurate one.
- The best model can be deployed as a web application or API for real-time laptop price prediction.

---

## **Final Result**

The tuned **Gradient Boosting Regressor** achieved an **R² score of 89%**, demonstrating strong prediction accuracy for estimating laptop prices based on specifications and user preferences.

---

## **Conclusion**

The project proves that using robust preprocessing, feature extraction, and advanced regression models can accurately estimate laptop prices, supporting better pricing decisions for buyers, sellers, and retailers.
