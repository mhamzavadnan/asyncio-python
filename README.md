# Asyncio Python - Learning Project

A Python project demonstrating fundamental concepts of asynchronous programming using `asyncio`.

## Overview

This project provides practical examples of key asyncio concepts including:
- **Synchronous vs Asynchronous Functions**
- **Futures** - Promise-like objects for handling async results
- **Coroutines** - Async functions that can be awaited
- **Tasks** - Wrapped coroutines that run concurrently

## Features

- ⏱️ Execution time tracking with detailed logs
- 🔄 Side-by-side comparison of sync and async operations
- 📝 Clear examples of asyncio primitives
- 🎯 Demonstrates blocking vs non-blocking operations

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the main script to see asyncio concepts in action:

```bash
python terms.py
```

### Expected Output

The script will demonstrate:
1. Synchronous function execution with blocking sleep
2. Future creation and resolution
3. Coroutine object creation and awaiting
4. Task creation and concurrent execution
5. Total execution time tracking

## Project Structure

```
asyncio-python/
├── terms.py           # Main demonstration script
├── requirements.txt   # Project dependencies
├── examples/          # Additional examples
└── README.md          # This file
```

## Key Concepts Demonstrated

### Synchronous Function
```python
def sync_function(test_param: str) -> str:
    time.sleep(2)  # Blocks execution
    return f"Synchronous result: {test_param}"
```

### Asynchronous Function
```python
async def async_function(test_param: str) -> str:
    await asyncio.sleep(2)  # Non-blocking
    return f"Asynchronous result: {test_param}"
```

### Future
A low-level awaitable object representing an eventual result.

### Coroutine
An async function that must be awaited to execute.

### Task
A coroutine wrapped for concurrent execution in the event loop.

## Learning Resources

- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)

## License

This is a learning project for educational purposes.
