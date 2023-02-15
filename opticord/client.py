import aiosonic
import asyncio
import json


class authenticate:
    def __init__(self, token):
        self.token = token
        print("Opticord | Authenticating to the discord gateway")

    def __str__(self):
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self._authenticate(token=self.token))
        data['token'] = self.token
        return str(data)


    async def _authenticate(self, token):
        url = 'https://discord.com/api/users/@me'
        headers = {
            'Authorization': f'Bot {token}'
        }

        http_client = aiosonic.HTTPClient()
        response = await http_client.get(url=url, headers=headers)
        if response.status_code == 200:
            print("Opticord | Successfully Authenticated to discord gateway")
            return await response.json()
        else:
            raise Exception(f"Unknown error during authentication\nStatus code: {response.status_code}")
