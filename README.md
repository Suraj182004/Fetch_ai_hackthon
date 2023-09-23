

# News Headline Agent

This Python script, powered by the `uagents` library, allows you to fetch and receive top news headlines and alerts via SMS using the News API and Twilio. It periodically checks for news updates and sends them to your phone number if you opt to receive them.

## Getting Started

### Prerequisites

Before running this script, you'll need the following:

- Python 3.x installed on your machine.
- Dependencies installed. You can install them using `pip`:

    ```bash
    pip install requests twilio uagents
    ```

- News API Key: Get your News API key [here](https://newsapi.org/).

- Twilio Account: Sign up for a Twilio account [here](https://www.twilio.com/). You will need your Twilio Account SID and Auth Token.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Suraj182004/Fetch_ai_hackthon.git
    cd Fetch_ai_hackthon
    ```

2. Configure your News API key and Twilio credentials:

    Replace `'your_api_key_here'` with your News API key in the `NEWS_API_KEY` variable.

    Replace `'your_account_sid'` and `'your_auth_token'` with your Twilio Account SID and Auth Token in the `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` variables.

3. Run the script:

    ```bash
    python newsapi_hackathon.py
    ```

## Usage

1. Select a news category from the available categories (e.g., entertainment, technology, sports).

2. Enter your preferred country (e.g., US, UK).

3. View the top headlines in the selected category.

4. Choose to receive headlines via SMS by entering 'yes' when prompted.

5. Enter your phone number to receive SMS alerts.

6. The headlines will be sent to your phone via Twilio.

7. You can choose to fetch news again or exit the program.



## Contributors

- Suraj Yaligar & Kshitij Verma

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [News API](https://newsapi.org/)
- [Twilio](https://www.twilio.com/)
- [uagents](https://pypi.org/project/uagents/)

---


