import os

# Set your API key (replace YOUR_API_KEY with your actual key)
os.environ["GOOGLE_API_KEY"] = "AIzaSyBQ_pZ37jQiQG1tFGiyfViNrWXOZXjew5U"

# Verify it’s set
print("GOOGLE_API_KEY set successfully!")

from agno.agent import Agent, RunOutput, RunOutputEvent, RunEvent
from agno.utils.pprint import pprint_run_response
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.hackernews import HackerNewsTools

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the report.",
    markdown=True,
)

agent.print_response(input="Trending startups and product and Stories from hackernews")


# Run agent with input="Trending startups and products."
# response: RunOutput = agent.run(input="Trending startups and products and Stories from Hackernews.")
# Print the response in markdown format
# print(response)