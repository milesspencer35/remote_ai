import asyncio
from remote_agent import RemoteAgent

async def main():
    agent = RemoteAgent()
    await agent.evaluate("Play the video, go back 30 seconds, and turn the volume up a lot")


if __name__ == "__main__":
    asyncio.run(main())