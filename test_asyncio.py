
#!/usr/bin/env python3

import asyncio
import signal

DRONE_HOST = '192.168.10.1'

CONTROL_UDP_PORT = 8889
STATE_UDP_PORT = 8890


class TelloProtocol:

    command_ok = None

    def connection_made(self, transport):
        print('CONNECTION MADE')
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('RECEIVED', message)
        if message == 'ok' and self.command_ok and not self.command_ok.done():
            self.command_ok.set_result(True)

    def error_received(self, exc):
        print('ERROR', exc)

    def connection_lost(self, exc):
        print('CONNECTION LOST', exc)
        if self.command_ok:
            self.command_ok.cancel()

async def main():
    loop = asyncio.get_event_loop()

    transport, protocol = await loop.create_datagram_endpoint(TelloProtocol, remote_addr=(DRONE_HOST,CONTROL_UDP_PORT))

    loop.add_signal_handler(signal.SIGINT, lambda: transport.close())

    async def send(message):
        print(f'SEND {message}')
        protocol.command_ok = loop.create_future()
        transport.sendto(message.encode())
        await protocol.command_ok

    try:
        await send('command')
        await send('takeoff')
        await send('land')
    finally:
        transport.close()

asyncio.run(main())