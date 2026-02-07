import asyncio
from remote_agent import RemoteAgent

async def main():
    agent = RemoteAgent()
    await agent.evaluate("Mute the video and then skip forward 30 seconds")


if __name__ == "__main__":
    asyncio.run(main())