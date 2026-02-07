from llm_agent import LlmAgent
from remote_toolbox import remote_toolbox

SYSTEM_PROMPT = """
- You are a helpful AI assistant that can control a TV remote.
- You have access to tools that can control the TV remote. 
- You should use the tools to control the TV remote.
- You can call functions multiple times in a row if needed.
    - For example, if the user says "skip forward 30 seconds", you should call skip forward 6 times

"""

class RemoteAgent(LlmAgent):
    def __init__(self):
        super().__init__(system_prompt=SYSTEM_PROMPT, model="gpt-4o-mini")

    async def evaluate(self, user_input):
        return await self.execute(
            prompt="Here is the user_input: " + user_input,
            toolbox=remote_toolbox
        )
