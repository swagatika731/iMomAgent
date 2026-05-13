"""Main entry point for the iMom Agent system."""

from google.adk import Agent

from imom_agent import (
    ActivityAgent,
    CalendarAgent,
    RagAgent,
    TaskAgent,
    WeatherAgent,
    WebSearchAgent,
)


def main():
    """Main function to initialize and run the agent system."""

    # Mock tool implementation
    def get_current_time(city: str) -> dict:
        """Returns the current time in a specified city."""
        return {"status": "success", "city": city, "time": "10:30 AM"}

    root_agent = Agent(
        model='gemini-flash-latest',
        name='root_agent',
        description="Tells the current time in a specified city.",
        instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
        tools=[get_current_time],
    )

    # Initialize all agents
    agents = {
        "activity": ActivityAgent(),
        "calendar": CalendarAgent(),
        "rag": RagAgent(),
        "task": TaskAgent(),
        "weather": WeatherAgent(),
        "web_search": WebSearchAgent(),
    }

    print("iMom Agent System initialized")
    for name, agent in agents.items():
        print(f"  - {agent.name}: {agent.description}")


if __name__ == "__main__":
    main()
