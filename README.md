# Jescel-bot: Chatbot Integration with Wine Website

Jescel-bot is a chatbot integrated with a simple website that provides business information and assistance related to wines.

## Features

- **Dialogflow Integration:** Jescel-bot uses Dialogflow for natural language understanding and processing user queries.
- **Backend Technologies:**
  - Built using Python and Flask for the backend server.
  - Utilizes MySQL database for storing session data and enhancing user interaction.
  - Ngrok is used for exposing the Flask server during development for webhook integration with Dialogflow.
- **Frontend:**
  - The website is created using HTML and CSS.
  - Provides a user-friendly interface for customers to interact with Jescel-bot and access business information.

## How to Run

### Prerequisites

- Python 3.x installed on your machine
- MySQL database setup with credentials (username and password)
- Ngrok installed for local webhook testing

### Setting Up

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/jescel-bot.git
   cd jescel-bot
2. **Set Up Python Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. **Install Dependencies:**
    ```bash
    pip install Flask mysql-connector-python

4. **Database Configuration:**
     - Create a MySQL database named jescel_bot.
     - Update app.py with your MySQL database credentials.

5. **Run Flask Application:**
     ```bash
     python app.py

6. **Ngrok Setup:**

    - Run ngrok to expose your local Flask server:
      ```bash
      ngrok http 8080
    - Copy the ngrok URL (https://randomstring.ngrok.io) to Dialogflow's webhook configuration.
  
7. **Dialogflow Configuration:**
   - Create a Dialogflow agent named Jescel-bot.
   - Configure the webhook URL (https://randomstring.ngrok.io/webhook) in Dialogflow's fulfillment section.
  
8. **Start the Website:**
   - Open index.html in a web browser to interact with Jescel-bot.

## Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests to suggest new features or improvements.
