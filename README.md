# Gemini Jarvis

Gemini Jarvis is a virtual assistant program developed in Python, inspired by Jarvis from Iron Man. It utilizes various APIs and libraries to perform tasks such as fetching weather information, searching the web, providing general assistance, and more.

## Features

- **Function-based Command Execution**: Gemini Jarvis executes functions based on user queries, allowing for seamless interaction.
- **Voice Input and Output**: Users can interact with Gemini Jarvis using voice commands, and the assistant responds with synthesized audio.
- **Web Scraping and Search**: Gemini Jarvis can search the web for information based on user queries and scrape relevant data from websites.
- **Integration with Flask**: The program includes a Flask web server for easy deployment and interaction via HTTP requests.

## Getting Started

To get started with Gemini Jarvis, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `git clone https://github.com/chaitanyaram1204/My_jarvis.git`.

2. **Install Dependencies**: Install the necessary Python dependencies by running `pip install -r requirements.txt`.

3. **API Keys**: Obtain API keys for services like Google Text-to-Speech, Yahoo Weather, and Google Custom Search. Update the `config.py` file with your API keys.

4. **Run the Program**: Execute `python flask_web.py` to start Gemini Jarvis. The Flask server will run locally, and you can interact with the assistant through the provided interface or by sending HTTP POST requests.

## Usage

Gemini Jarvis supports both text and voice input. You can interact with it in the following ways:

- **Text Input**: Simply type your query or command into the provided interface or send an HTTP POST request with a JSON payload containing your message to `/process_message`.

- **Voice Input**: Use a microphone to speak your query or command. The program will recognize your speech and process it accordingly.

## Contributing

Contributions to Gemini Jarvis are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to submit a pull request. Make sure to follow the existing code style and guidelines.

## Acknowledgements

Gemini Jarvis utilizes various open-source libraries and APIs, including:

- SpeechRecognition
- gTTS (Google Text-to-Speech)
- Flask
- BeautifulSoup
- Google Custom Search API
- Yahoo Weather API
