import click


@click.group()
def main():
    pass


@main.command()
def build():
    pass


if __name__ == "__main__":
    main()
