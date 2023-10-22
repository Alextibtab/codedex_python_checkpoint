# Terminal RPG with Pygame

This project is an extension of a terminal-based RPG game, enhanced with graphics using the `pygame` library. Instead of a traditional terminal interface, this game provides a graphical window with interactive elements.

## Dependencies

- **Python**: This project is written in Python. Ensure you have Python 3.x installed.
- **Pygame**: A popular game development library for Python. Used for rendering graphics and handling user input.
- **pytest**: A popular testing framework for Python. Used for writing and running tests.
- **mypy**: An optional dependency used for static type checking.
- **black**: An optional dependency used for code formatting.

## Project Structure

The project uses a modern Python project structure with the help of `pyproject.toml` and `Makefile`.

### pyproject.toml

The `pyproject.toml` file is the configuration file for the build system and tools like `mypy`. It specifies build system requirements and can be used to configure various Python tools.

For example, the `[tool.mypy]` section in `pyproject.toml` is used to configure `mypy` for type checking.

### Makefile

The `Makefile` provides automation for common tasks such as setting up a virtual environment, running tests, linting, and type checking. Some common commands you might find in the `Makefile` include:

- `make help`: Display a help message with available commands.
- `make test`: Run the test suite.
- `make format`: Format the code using `black`.
- `make env/venv`: Create the virtual environment.
- `make build`: Build the project.
- `make clean`: Remove the virtual environment and any build artifacts.

To use the `Makefile`, simply run the desired command using `make`. For example, to set up the project, you'd run:

```bash
make env
```

Activate the virtual environment:
```bash
source .venv/bin/activate
```

Run the game:
```bash
terminal_rpg
```