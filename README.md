# FastAPI OCR Microservice

This is a microservice built using FastAPI that performs Optical Character Recognition (OCR) on images. It uses Tesseract-OCR for the OCR functionality and can be easily deployed using Docker.

## Features

- Upload an image to perform OCR.
- Returns the recognized text from the uploaded image.
- Echoes back the uploaded image (for debugging purposes).
- Authentication using a bearer token.

## Installation

To run the microservice locally, follow these steps:

1. Clone this repository.
2. Install Docker if not already installed.
3. Build the Docker image:

    ```bash
    docker build -t fastapi-ocr .
    ```

4. Run the Docker container:

    ```bash
    docker run -d --name fastapi-ocr -p 8000:8000 fastapi-ocr
    ```

5. Access the microservice at `http://localhost:8000`.

## Endpoints

- `/`: Home endpoint, returns HTML page with basic information.
- `POST /`: Upload an image for OCR.
- `POST /img-echo/`: Echoes back the uploaded image.

## Environment Variables

- `APP_AUTH_TOKEN`: Authentication token for accessing the microservice.
- `DEBUG`: Enable debug mode.
- `ECHO_ACTIVE`: Enable/disable image echoing.
- `APP_AUTH_TOKEN_PROD`: Authentication token for production mode.
- `SKIP_AUTH`: Skip authentication for debugging purposes.

## Usage

To use the microservice, send a POST request with an image file to the appropriate endpoint. Make sure to include the authentication token in the request header.

## Dependencies

- FastAPI
- Pytesseract
- Pillow
- Docker
