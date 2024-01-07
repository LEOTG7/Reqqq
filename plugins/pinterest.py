import pyrogram
from pyrogram import Client, filters
import requests
from urllib.parse import urljoin

STICKER_ID = "CAACAgUAAxkBAAIefmWa2mFflQjODv8DcWTwKN5rb7x3AAJyCgACywLBVKKgVw2dk9PbHgQ"  

@Client.on_message(filters.text & filters.regex(r"https://pin\.it/\w+"))
async def download_photo(client, message):
    try:
        await message.reply_sticker(STICKER_ID)  # Send the sticker

        pin_url = message.text
        response = requests.get(pin_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Extract the direct image URL from the response content
        image_url = response.urljoin(response.json()["data"]["images"]["orig"]["url"])  # Adjusted extraction

        await client.send_photo(message.chat.id, image_url)  # Send the downloaded photo
    except Exception as e:
        await message.reply_text(f"Error downloading photo: {e}")


