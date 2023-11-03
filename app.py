from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

# Load your dataset from the CSV file
df = pd.read_csv('data_daily.csv')

# Convert 'Date' to datetime format
df['# Date'] = pd.to_datetime(df['# Date'])

# Set 'Date' as the index
df.set_index('# Date', inplace=True)

# Feature Engineering
df['Day_of_Week'] = df.index.dayofweek
df['Day_of_Month'] = df.index.day
df['Month'] = df.index.month

# Lag features (previous day's receipt count)
df['Prev_Day_Receipts'] = df['Receipt_Count'].shift(1)

# Handle missing values
df.dropna(inplace=True)  # Drop rows with missing values for simplicity

# Define features and target
features = ['Day_of_Week', 'Day_of_Month', 'Month', 'Prev_Day_Receipts']
target = 'Receipt_Count'

# Separate data for training the model
X_train, y_train = df[features], df[target]

# Model training without imputation
X_train = np.c_[np.ones(X_train.shape[0]), X_train]  # Add a column of ones for the intercept term
theta = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

# Full dataset for predicting the year 2022
X_full = df[features]
X_full = np.c_[np.ones(X_full.shape[0]), X_full] 
full_predictions = X_full @ theta

# Predictions for the year 2022
monthly_predictions = pd.Series(full_predictions, index=df.index).resample('M').sum()

# Convert the predictions to integers
monthly_predictions = monthly_predictions.astype(int)

# Convert the Pandas Series to a list of dictionaries
monthly_predictions_list = [{'month': month.strftime('%B'), 'prediction': prediction} for month, prediction in zip(monthly_predictions.index, monthly_predictions)]

# Pass actual receipt counts to the template
actual_data_list = [{'month': month, 'actual': actual} for month, actual in zip(df.index.strftime('%B'), df[target])]

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(df.index, df[target], label='Actual Receipt Count', marker='o')
plt.plot(df.index, full_predictions, label='Predicted Receipt Count', marker='o')
plt.xlabel('# Date')
plt.ylabel('Receipt Count')
plt.title('Receipt Count Prediction')
plt.legend()

# Save plot to a BytesIO object
img = BytesIO()
plt.savefig(img, format='png')
img.seek(0)

# Encode the plot image to base64
plot_img = base64.b64encode(img.getvalue()).decode()

plt.close()


@app.route('/')
def index():
    # Calculate total receipt count for each month
    monthly_actual_data = df[target].resample('M').sum().astype(int)

    # Convert the monthly actual data to a list of dictionaries
    actual_data_list = [{'month': month.strftime('%B'), 'actual': actual} for month, actual in zip(monthly_actual_data.index, monthly_actual_data)]

    # Pass the lists to the template
    return render_template('index_interactive.html', predictions=monthly_predictions_list, actual_data=actual_data_list, plot_img=plot_img)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
