# Fetch-Flask-App
# Receipt Count Prediction App

This Flask web application predicts monthly receipt counts for the year 2022 based on historical data. It includes user interaction and visualizations using Plotly.

## Getting Started

### Prerequisites

Make sure you have Docker installed on your machine.

### Build and Run the Docker Container

```bash
docker build -t my-flask-app .
docker run -p 4000:80 my-flask-app
Visit http://localhost:4000/ in your web browser.

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
