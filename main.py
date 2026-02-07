import asyncio
from remote_agent import RemoteAgent

async def main():
    agent = RemoteAgent()
    await agent.evaluate("Increase the volume and pause the video")


if __name__ == "__main__":
    asyncio.run(main())