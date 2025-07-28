# This is an example of multiagent communication in which the agents interacts in Roundrobin fashion
# an agent interacts with another agent to fine tune the results and give proper response
#once the retriever agent "APPROVES" the response they stop interacting



import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_core import CancellationToken
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import asyncio
from dotenv import load_dotenv
import os


endpoint = keys_value.get("endpoint")
model_name = keys_value.get("model_name")
deployment = keys_value.get("deployment")

subscription_key = keys_value.get("subscription_key")
api_version = keys_value.get("api_version")



az_client = AzureOpenAIChatCompletionClient(
    azure_deployment=model_name,
    model=model_name,
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key
)


# Create the primary agent.
Story_writer = AssistantAgent(
    "Story_writer",
    model_client=az_client,
    system_message="You are a helpful AI assistant which write the story for kids. Keep the story short",
)

# Create the critic agent.
Story_reviewer = AssistantAgent(
    "Story_reviewer",
    model_client=az_client,
    system_message="You are a helpful AI assistant which Provides constructive feedback on Kids stories to add a postive impactful ending. Respond with 'APPROVE' to when your feedbacks are addressed.",
)

# Define a termination condition that stops the task if the critic approves.
text_termination = TextMentionTermination("APPROVE")


# Create a team with the primary and critic agents.
team = RoundRobinGroupChat([Story_writer, Story_reviewer], termination_condition=text_termination)

# Define the main asynchronous function
async def main():
    message = input("Enter your message: ")
    await Console(
        team.run_stream(task=message)
    )  # Stream the messages to the console.

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(main())
