from uagents import Agent
import requests
from twilio.rest import Client
from uagents import Context
from uagents.setup import fund_agent_if_low


newsman = Agent(name="newsman", 
        port=8000,
        endpoint=["http://127.0.0.1:8000/submit"],
        seed="newsman recovery phrase",
)


# Replace 'your_api_key_here' with your actual News API key
NEWS_API_KEY = 'ADD_YOUR_API_KEY'#add your new api key here
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

# Define news categories
NEWS_CATEGORIES = {
    'entertainment': 'entertainment',
    'technology': 'technology',
    'sports': 'sports',
    # Add more categories as needed
}

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ADD_YOUR_ACCOUNT_SID_KEY'#add your ACCOUNT_SID api key here
TWILIO_AUTH_TOKEN = 'ADD_YOUR_AUTH_TOKEN_KEY'#add your AUTH_TOKEN api key here

def fetch_top_headlines(category, country):
    params = {
        'apiKey': NEWS_API_KEY,
        'category': category,
        'country': country,
        'pageSize': 10,  # Adjust as needed
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    articles = data['articles']
    # Implement your own logic to filter and select the top 3 stories
    top_stories = articles[:3]
    return top_stories

def present_news(category, top_stories):
    print(f"Top headlines in {category.capitalize()}:")
    for i, story in enumerate(top_stories, start=1):
        print(f"{i}. {story['title']}")
        print(f"   {story['description']}")
        print(f"   Read more: {story['url']}\n")

def send_sms(to_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            to=to_number,
            from_='ADD_YOUR_TWILIO_NUMBER',  # Replace with your Twilio phone number
            body=message
        )
        print(f"Message sent successfully to {to_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

def main_print():
    print("Welcome to the News Headline Agent!")

    while True:
        # Prompt the user for their preferred news category
        print("Select the news category you are interested in:")
        print("Available categories: ", ', '.join(NEWS_CATEGORIES.keys()))
        category_input = input("Enter your choice: ").strip().lower()

        if category_input not in NEWS_CATEGORIES:
            print("Invalid category. Exiting.")
            break
        else:
            # Prompt the user for their preferred country
            country_input = input("Enter your preferred country (e.g., US, UK): ").strip().upper()

            # Fetch and present the top headlines for the selected category and country
            top_stories = fetch_top_headlines(NEWS_CATEGORIES[category_input], country_input)
            present_news(category_input, top_stories)

            # Ask the user if they want to receive the news headlines via SMS
            send_sms_option = input("Do you want to receive these headlines via SMS? (yes/no): ").strip().lower()
            if send_sms_option == "yes":
                phone_number = input("Enter your phone number to receive SMS: ").strip()
                for story in top_stories:
                    message = f"{story['title']}\n{story['description']}\nRead more: {story['url']}"
                    send_sms(phone_number, message)
                print("Headlines sent via SMS.")

            # Ask the user if they want to run the program again
            run_again = input("Do you want to fetch news again? (yes/no): ").strip().lower()
            if run_again != "yes":
                print("Exiting.")
                break
@newsman.on_interval(period=28800.0)
async def time_interval(ctx:Context):
    news = main_print()
    ctx.logger.info(news)
    if "yes" in news:
        await send_sms_alert(news) 

if __name__ == "__main__":
     newsman.run()
