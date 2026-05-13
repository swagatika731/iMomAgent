"""iMom Agent - A multi-agent system for personal assistant tasks."""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .activity_agent import ActivityAgent
from .calendar_agent import CalendarAgent
from .rag_agent import RagAgent
from .task_agent import TaskAgent
from .weather_agent import WeatherAgent
from .web_search_agent import WebSearchAgent

__all__ = [
    "ActivityAgent",
    "CalendarAgent",
    "RagAgent",
    "TaskAgent",
    "WeatherAgent",
    "WebSearchAgent",
]
