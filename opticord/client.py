"""""""""
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
"""""""""

import asyncio
import json
import websockets

class authenticate:
    def __init__(self, token):
        self.token = token
        print("Opticord | Authenticating to the discord gateway")
        loop = asyncio.get_event_loop()
        client = loop.run_until_complete(self._authenticate(token=self.token))
    async def _authenticate(self, token):
        uri = 'wss://gateway.discord.gg/?v=9&encoding=json'
        headers = {
            'Authorization': f'Bot {token}'
        }

        async with websockets.connect(uri, extra_headers=headers) as websocket:
            message = {
                'op': 2,
                'd': {
                    'token': token,
                    'intents': 513,
                    'properties': {
                        '$os': 'linux',
                        '$browser': 'my_library',
                        '$device': 'my_library'
                    }
                }
            }
            await websocket.send(json.dumps(message))

            while True:
                response = await websocket.recv()
                data = json.loads(response)

                if data['op'] == 10:
                    print("Opticord | Successfully Authenticated to discord gateway")
                elif data['op'] == 0 and data['t'] == 'READY':
                    print("Opticord | Received READY event:", data['d'])
                    # Handle the READY event here
                else:
                    print("Opticord | Received unknown event:", data)
