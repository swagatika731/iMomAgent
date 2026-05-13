# iMom Agent

A multi-agent system for personal assistant tasks including activity management, calendar scheduling, task tracking, weather forecasts, web search, and retrieval-augmented generation.

## Project Structure

```
iMomAgent/
├── imom_agent/              # Main package
│   ├── __init__.py
│   ├── base.py              # Base agent class
│   ├── activity_agent.py    # Activity management agent
│   ├── calendar_agent.py    # Calendar scheduling agent
│   ├── rag_agent.py         # RAG agent
│   ├── task_agent.py        # Task management agent
│   ├── weather_agent.py     # Weather information agent
│   ├── web_search_agent.py  # Web search agent
│   └── main.py              # Main entry point
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_agents.py
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # Python dependencies
├── Makefile                 # Useful commands
├── .gitignore               # Git ignore rules
└── README.md               # This file
```

## Installation

### Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd iMomAgent
```

2. Install in development mode with dependencies:
```bash
make dev-install
```

Or using pip directly:
```bash
pip install -e ".[dev]"
```

### Production Install

```bash
make install
# or
pip install -e .
```

## Usage

### Basic Example

```python
from imom_agent import ActivityAgent, WeatherAgent, TaskAgent

# Initialize agents
activity_agent = ActivityAgent()
weather_agent = WeatherAgent()
task_agent = TaskAgent()

# Execute tasks
activity_agent.execute("recommend_activity")
weather_agent.execute("get_forecast", location="New York")
task_agent.execute("create_task", title="Buy groceries")
```

### Running the Main Application

```bash
python -m imom_agent.main
```

## Development

### Running Tests

```bash
make test
```

Or directly with pytest:
```bash
pytest tests/ -v
```

### Code Formatting

Format code with Black:
```bash
make format
```

### Linting

Run flake8:
```bash
make lint
```

### Cleaning Build Artifacts

```bash
make clean
```

## Available Commands

View all available make commands:
```bash
make help
```

## Requirements

- Python 3.9+
- See `requirements.txt` for dependencies

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
