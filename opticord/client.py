import aiosonic
import asyncio

class authentificate:
    def __init__(self, token):
        self.token = token

    def __str__(self):
        loop = asyncio.get_event_loop()
        client = str(loop.run_until_complete(self._authenticate(token=self.token)))
        return client
    async def _authenticate(self, token):
        url = 'https://discord.com/api/users/@me'
        headers = {
            'Authorization': f'Bot {token}'
        }

        http_client = aiosonic.HTTPClient(verify_ssl=False)
        response = await http_client.get(url=url, headers=headers, ssl=None)
        return await response.json()