# Telegram Redirector Site

This is an example of a web application that collects user information through a form, stores it in a database, and sends the data to an administrator on Telegram using a bot.

## Usage

To use this project, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/ImmuneFOMO/TelegramRedirectorSite.git
   ```

2. Navigate to the project directory:

   ```shell
   cd TelegramRedirectorSite
   ```

3. Install the required dependencies:

   ```shell
   pip install Flask Flask-SQLAlchemy
   ```

4. Open the `main.py` file in a text editor:

   ```shell
   nano main.py
   ```

5. In the `main.py` file, update the following lines with your Telegram Bot Token and Chat ID:

   ```python
   telegram_bot_token = "your telegram bot token"
   chat_id = "your chat id"
   ```

6. Save the `main.py` file.

7. Create the SQLite database by running the application:

   ```shell
   python3 main.py
   ```

   This command will also start the web application locally.

8. Access the web application in your browser by navigating to `http://localhost:5000`.

9. Fill out the form on the web page with user information and submit it.

10. The information will be stored in the SQLite database, and a notification will be sent to your Telegram account with the submitted data.

## Project Structure

The project structure includes the following files:

- `main.py`: The main Python script that runs the Flask web application, handles form submissions, stores data in the SQLite database, and sends data to Telegram.

- `index.html`: HTML template for the web form.

- `css/index.css`: CSS stylesheet for styling the web form.

## Customization

You can customize the web form and styling by modifying the `index.html` and `css/index.css` files to suit your needs.

## Dependencies

- Flask: Web framework for Python.
- Flask-SQLAlchemy: SQLAlchemy integration for Flask.
- requests: Library for making HTTP requests.

Feel free to explore and modify this project to fit your requirements. Happy coding!
