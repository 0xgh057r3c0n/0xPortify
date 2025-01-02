# 0xPortify

![Logo](logo.png)

**0xPortify** is a Python tool designed to convert a list of IP:port pairs into URLs formatted as `https://IP:port/`. This tool is useful for processing IP:port lists in network security assessments, system configurations, or any other tasks that require IP to URL conversion.

## Features

- Converts a list of IP:port pairs to `https://IP:port/` format.
- Supports custom separators between IP and port.
- Handles input from a file and outputs to another file.
- Provides colorized output for added clarity (using `colorama`).
- Includes logging support for debugging and verbose output.

## Requirements

- Python 3.x
- `colorama` Python library (for colorized terminal output)

## Installation

1. **Clone the repository:**

   To get started, clone the repository from GitHub:

   ```bash
   git clone https://github.com/0xgh057r3c0n/0xPortify.git
   cd 0xPortify
   ```

2. **Install dependencies:**

   Install the required dependencies using the `requirements.txt` file. Run the following command:

   ```bash
   pip3 install -r requirements.txt
   ```

   This will install `colorama` (the only external dependency).

## Usage

### Command-Line Arguments

- `-i` or `--input`: Specify the input file containing the IP:port list (e.g., `input.txt`).
- `-o` or `--output`: Specify the output file to save the formatted URLs (e.g., `output.txt`).
- `-s` or `--separator`: (Optional) Specify the separator between the IP address and port (default is `:`).
- `-v` or `--verbose`: (Optional) Enable verbose logging to show detailed information.

### Example

To convert an IP:port list from `input.txt` to the `https://IP:port/` format and save it to `output.txt`:

```bash
python3 0xPortify.py -i input.txt -o output.txt -s ':' -v
```

### Sample Input (`input.txt`):

```
192.168.1.1:8080
10.0.0.1:443
127.0.0.1:8080
```

### Sample Output (`output.txt`):

```
https://192.168.1.1:8080/
https://10.0.0.1:443/
https://127.0.0.1:8080/
```

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
