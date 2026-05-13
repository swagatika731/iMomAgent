"""Base agent class for all agents in the system."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseAgent(ABC):
    """Base class for all agents."""

    def __init__(self, name: str, description: str = ""):
        """
        Initialize the agent.

        Args:
            name: The name of the agent
            description: A description of what the agent does
        """
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, task: str, **kwargs) -> Any:
        """
        Execute a task.

        Args:
            task: The task to execute
            **kwargs: Additional arguments for the task

        Returns:
            The result of the task execution
        """
        pass

    def __repr__(self) -> str:
        """Return string representation of the agent."""
        return f"{self.__class__.__name__}(name='{self.name}')"
