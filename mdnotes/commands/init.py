# -*- coding: utf-8 -*-

import os
from rich import print as rprint


def init(args):
    if os.path.exists(args.path):
        rprint(f'[bold red]Path already exists![/bold red]')
        return

    rprint(f'Creating notes directory in: [bold blue]{args.path}[/bold blue]')
    os.mkdir(args.path)
