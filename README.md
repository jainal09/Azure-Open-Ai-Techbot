# GPT 4o Tech Bot 🤖
This is a tech bot that efficiently answers questions related to technology. It is programmed to specialize in answering technological questions, simulating specific use cases of a particular topic. The bot utilizes the GPT-4o API and streamlit for its functionality.


## Built With 🛠️
- [GPT-4o](https://openai.com/index/hello-gpt-4o)
- [Streamlit](https://streamlit.io/)
- [Azure Open AI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3.11 or higher
2. Poetry


### Installing

Assuming you have python and poetry installed, you can install the dependencies by running the following command:

```bash
poetry install
```

### Running the bot
```bash
python -m streamlit run src/tech_bot/main.py
```
This will start a server at `http://localhost:8501` where you can interact with the bot.

## Features 📋
1. Real time chat GPT like interface with the bot 💬
2. Streaming response from the GPT-4o API to the user 🌐
3. Safeguards for inappropriate content 🚫
4. Features to restrict Answers to questions only for the domain of technology achieved through prompt engineering ⚙️
5. Real time token calculation for displaying the token usage to the user 📊
6. Feature to pass the context and history to the GPT-4o API for better responses 📚 



## Contributing 🖇️

Please read [CONTRIBUTING.md](https://) for details on our code of conduct, and the process for submitting pull requests to us.

## License 📄

This project is licensed under the [LICENSE.md](LICENSE.md) - see the file for details