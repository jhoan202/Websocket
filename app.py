import asyncio
import signal
import os

import websockets


async def echo(websockets):
    async for message in websockets:
        await websockets.send(message)


async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=int(os.environ[6497]),
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())
