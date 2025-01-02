import argparse
import re
import logging
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def display_banner():
    banner = f"""
{Fore.CYAN}   __           ____               __           ___             
 /'__`\\        /\\  _`\\            /\\ \\__  __  /'___\\            
/\\ \\_/\\ \\  __  _\\ \\ \\L\\ \\___   _ __\\ \\ ,_\\/\\_/\\ \\__/  __  __    
\\ \\ \\ \\ \\/\\ \\/'\\\\ \\ ,__/ __`\\/\\`'__\\ \\ \\/\\/\\ \\ \\ ,__\\/\\ \\/\\ \\   
 \\ \\ \\_\\ \\>  </ \\ \\ \\/\\ \\L\\ \\ \\ \\/ \\ \\ \\_\\ \\ \\ \\ \\_/\\ \\ \\_\\ \\  
  \\ \\____//\\_/\\_\\ \\ \\_\\ \\____/\\ \\_\\  \\ \\__\\\\ \\_\\ \\_\\  \\/`____ \\ 
   \\/___/ \\//\\/\\_/  \\/_/\\/___/  \\/_/   \\/__/ \\/_/\\/_/   `/___/> \\
                                                          /\\___/
                                                          \\/__/  
{Style.BRIGHT}{Fore.MAGENTA}    Convert IP:port list to https://IP:port/ format
                   Author: 0xgh057r3c0n
    """
    print(banner)

def format_ip_port(input_file, output_file, separator=":"):
    ip_port_pattern = re.compile(r"^(?P<ip>(?:\d{1,3}\.){3}\d{1,3}):(?P<port>\d+)$")
    
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if separator in line:
                    parts = line.split(separator)
                else:
                    parts = line.split()
                if len(parts) == 2:
                    ip, port = parts
                    match = ip_port_pattern.match(f"{ip}:{port}")
                    if match:
                        formatted_line = f"https://{match.group('ip')}:{match.group('port')}/\n"
                        outfile.write(formatted_line)
                        print(f"{Fore.GREEN}Added: {formatted_line.strip()}")
    except FileNotFoundError as e:
        print(f"{Fore.RED}File not found: {e.filename}")
    except IOError as e:
        print(f"{Fore.RED}I/O error: {e}")

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(
        description="Convert IP and port list to https://ip:port/ format",
        epilog="Example: python script.py -i input.txt -o output.txt --separator ':'"
    )
    parser.add_argument("-i", "--input", required=True, help="Input file containing IP and port list")
    parser.add_argument("-o", "--output", required=True, help="Output file to save formatted URLs")
    parser.add_argument("-s", "--separator", default=":", help="Separator between IP and port in the input file (default: ':')")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    format_ip_port(args.input, args.output, args.separator)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(f"{Fore.YELLOW}\n[!] Script terminated by user.")
