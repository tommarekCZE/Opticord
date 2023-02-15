import os
from dotenv import load_dotenv
from opticord import client

load_dotenv()

token = os.getenv('discordtkn')

client = client.authenticate(token=token)