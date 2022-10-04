from discord_webhook import DiscordWebhook

print("Welcome to Sipo's Webhook Spammer, this will spam a discord webhook until you close this.")

webhook_url = input("Enter webhook url: ")
webhook_username = input("Enter webhook username: ")
webhook_content = input("Input what you want the content to be: ")

webhook = DiscordWebhook(url=webhook_url, username=webhook_username, content=webhook_content)
while True:
    webhook.execute()