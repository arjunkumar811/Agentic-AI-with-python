from agents import Agent, Runner




# Define an agent
hello_agent = Agent[Any](
    name: "Hello World Agent",
    instructions="you'r are an agent which greets the user and helps them ans using emojis and in funny way"
)


result = Runner.run.sync(hello_agent, "Hey There, My Name is Arjun")