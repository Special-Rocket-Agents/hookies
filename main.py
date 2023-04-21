from discord_webhook import DiscordWebhook
print("Welcome to hookies!")
url = input("Enter in your Webhook URL, this will be saved for the whole running duration >>> ")
while (True):
    message = input(">>> ")
    DiscordWebhook(url = url, content = message).execute()