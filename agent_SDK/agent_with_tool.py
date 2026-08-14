from agents import Agent, Runner
from agent import WebSearchTool



# Define an agent
hello_agent = Agent[Any](
    name: "Hello World Agent",
    instructions="you'r are an agent which greets the user and helps them ans using emojis and in funny way",
    tools=[
        WebSearchTool()
    ]
)


result = Runner.run.sync(hello_agent, "Hey There, My Name is Arjun")

print(result.final_output)