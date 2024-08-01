from typing import List

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, ToolMessage

load_dotenv()

def execute_tools(state: List[BaseMessage]) -> List[ToolMessage]:
    pass

if __name__ == "__main__":
    print("Tool Executor Enter")
    
    human_message