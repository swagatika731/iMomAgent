"""Tests for agent classes."""

import pytest

from imom_agent import (
    ActivityAgent,
    CalendarAgent,
    RagAgent,
    TaskAgent,
    WeatherAgent,
    WebSearchAgent,
)


class TestAgentInitialization:
    """Test agent initialization."""

    def test_activity_agent_init(self):
        """Test ActivityAgent initialization."""
        agent = ActivityAgent()
        assert agent.name == "ActivityAgent"
        assert "activity" in agent.description.lower()

    def test_calendar_agent_init(self):
        """Test CalendarAgent initialization."""
        agent = CalendarAgent()
        assert agent.name == "CalendarAgent"
        assert "calendar" in agent.description.lower()

    def test_weather_agent_init(self):
        """Test WeatherAgent initialization."""
        agent = WeatherAgent()
        assert agent.name == "WeatherAgent"
        assert "weather" in agent.description.lower()

    def test_task_agent_init(self):
        """Test TaskAgent initialization."""
        agent = TaskAgent()
        assert agent.name == "TaskAgent"
        assert "task" in agent.description.lower()

    def test_web_search_agent_init(self):
        """Test WebSearchAgent initialization."""
        agent = WebSearchAgent()
        assert agent.name == "WebSearchAgent"
        assert "search" in agent.description.lower()

    def test_rag_agent_init(self):
        """Test RagAgent initialization."""
        agent = RagAgent()
        assert agent.name == "RagAgent"
        assert "rag" in agent.description.lower()
