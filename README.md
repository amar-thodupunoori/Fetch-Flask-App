# Receipt Count Prediction Web App

This web application predicts monthly receipt counts for the year 2022 based on historical data. It uses Flask for the backend, Plotly for interactive visualizations, and various Python libraries for data processing.

## Getting Started

### Prerequisites

Make sure you have Docker installed on your machine.

### Running the App

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo
  ```
3. Build the Docker image:
  ```bash
  docker build -t my-flask-app .
  ```
4. Run the Docker container:
   ```bash
   docker run -p 4000:80 my-flask-app
  ```
Open your web browser and go to http://127.0.0.1:4000/ to view the app.

### Project Structure

app.py: Flask application code.
templates/index_interactive.html: HTML template with interactive Plotly plot.
requirements.txt: Python dependencies.
Dockerfile: Docker configuration file.

Dependencies

Flask==1.1.4
Werkzeug==1.0.1
MarkupSafe==1.1.1
pandas==1.3.3
numpy==1.21.2
matplotlib==3.4.3

Author
Amar Thodupunoori
