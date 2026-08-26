# IT1114 - Programming Principles

Coursework for IT1114, an introductory Python course.

## Rules

- No AI-generated code. All work must be written by hand.

## Setup

This project uses a Nix flake to provide a consistent Python environment (Python 3.12 with
pygame, numpy, requests, pytest, black, and ruff).

1. Install [Nix](https://nixos.org/download) with flakes enabled.
2. Enter the dev shell:

   ```sh
   nix develop
   ```

## Commands

Available inside the dev shell:

| Command | Description |
| --- | --- |
| `run`  | Run `main.py` |
| `repl` | Start a Python REPL with project packages available |
| `fmt`  | Format code with black |
| `lint` | Lint code with ruff |
| `test` | Run tests with pytest |

## Structure

Each lab/assignment lives in its own directory (e.g. `lab1/`).
