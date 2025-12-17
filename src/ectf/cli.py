"""CLI to interact with the eCTF API

Author: Ben Janis

This source file is part of an example system for MITRE's 2025 Embedded System CTF
(eCTF). This code is being provided only for educational purposes for the 2025 MITRE
eCTF competition, and may not meet MITRE standards for quality. Use this code at your
own risk!

Copyright: Copyright (c) 2025 The MITRE Corporation
"""

import webbrowser
from typing import Annotated

import typer

from ectf import CONFIG
from ectf.console import info

app = typer.Typer(help="Interact with the eCTF hardware, design, and API")


@app.command("rules")
def rules() -> None:
    """Open the eCTF rules website"""
    url = "https://rules.ectf.mitre.org"
    info(f"Opening eCTF rules website at {url}")
    webbrowser.open_new_tab(url)


@app.callback()
def set_globals(
    verbose: Annotated[
        int,
        typer.Option("--verbose", "-v", count=True, help="Enable debug prints"),
    ] = 0,
) -> None:
    """Set the verbosity of all scripts"""
    CONFIG["VERBOSE"] = verbose


if __name__ == "__main__":
    app()
