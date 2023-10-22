from terminal_rpg.app import App


def main() -> None:
    app = App(800, 600)
    app.run()


def sum(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    main()
