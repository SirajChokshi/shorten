# Shorten (s5n)

## CLI

### Installation

1. After cloning the repo proceed to navigate to the `cli/` directory

2. Install the CLI dependencies

```bash
pip install requirements.txt
```

3. Execute the following to make `s5n.py` executable, strip the `.py` extension and setup a global path for `s5n` 

```bash
chmod +x s5n.py && mv s5n.py s5n && mkdir -p ~/bin && cp s5n ~/bin
```

5. Append this line to add `~/bin` to your PATH in your `.bash_profile` or `.zshrc` and reload your shell.
```bash
export PATH=$PATH":$HOME/bin"
```

The `s5n` interface should be globally available.

## Server

Server-side rendered application and REST API built with Flask/Jinja.

### Getting Started

To get started add an environment variable in the `app/` directory as such.

```bash
export FLASK_APP=app
```

To start the server in development mode:

```bash
export FLASK_ENV=development
```

### Starting the Server

```bash
flask run
```
