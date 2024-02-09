# Flask Form Application

![GitHub license](https://img.shields.io/github/license/the0mikkel/flask-form) ![GitHub issues](https://img.shields.io/github/issues/the0mikkel/flask-form) ![GitHub pull requests](https://img.shields.io/github/issues-pr/the0mikkel/flask-form) ![GitHub last commit](https://img.shields.io/github/last-commit/the0mikkel/flask-form)

A simple Flask application that generates a form based on a JSON file and saves the form data to another JSON file. The application is built using Flask and runs in a Docker container.

## Running the Application

The application is designed to run in Docker. An included `docker-compose.yml` file will build the image and run the container. To run the application, execute the following commands in the root directory of the project:


```bash
docker compose build
docker compose up
```

Please note, that a `.env` file is required to run the application. The `.env` file should contain the following variables:

```.env
SECRET_KEY=<secret_key>
FORM_TITLE=<form_title>

SUCCESS_MESSAGE=Your message has been sent successfully.
ERROR_MESSAGE=An error occurred while sending your message. Please try again later.
BUTTON_TEXT=Submit

SUBMISSIONS_USER=<username>
SUBMISSIONS_PASS=<password>
```

An example `.env` file is included in the repository as `.env.example`.

*Please note, there have been prepared for nginx reverse proxy, and therefore requires the external network to be named "nginx-proxy". The CLI will prompt you to create the network if it does not exist.*  
*It can be deleted from the docker-compose file if not needed.*

## License

Please see the LICENSE file for license details.

## Contribution

To contribute, please fork the repository and create a pull request.  
If you find bugs or have suggestions for improvements, please create an issue.

## Authors and Acknowledgment

This project was made by [Mikkel Albrechtsen](https://github.com/the0mikkel) with the assistance of GitHub Copilot.