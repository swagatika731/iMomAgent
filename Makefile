.PHONY: help install dev-install test lint format clean

help:
	@echo "Available commands:"
	@echo "  make install       - Install the package"
	@echo "  make dev-install   - Install with development dependencies"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run linting (flake8)"
	@echo "  make format        - Format code with black"
	@echo "  make clean         - Remove build artifacts"

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

lint:
	flake8 imom_agent tests

format:
	black imom_agent tests

clean:
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
