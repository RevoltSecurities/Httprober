# Httrpober

Httrpober is a versatile subdomain enumeration tool designed to efficiently probe for alive subdomains from a provided list. It offers customizable concurrency and threading options to balance speed and resource utilization. This tool is built under the Apache 2.0 license.

## Features

- Probe for alive subdomains from a list of subdomains.
- Customize concurrency and thread settings for optimal performance.
- Save the output to a file.
- Prevent potential damage to the operating system by following recommended concurrency and thread values.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sanjai-AK47/Httrpober.git
   cd Httrpober
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Linux Users

For Linux users, you can move the provided binary file to `/usr/local/bin` to run it from anywhere:

```bash
sudo cp httrpober /usr/local/bin/
```

Now you can use the `httrpober` command from any directory:

```bash
httrpober -l subdomains.txt -o output.txt -c 50 -t 3
```

### Windows and macOS Users

Windows and macOS users can run the Python script:

```bash
python httrpober.py -l subdomains.txt -o output.txt -c 50 -t 3
```

- `-l` or `--list`: Path to the file containing the list of subdomains.
- `-o` or `--output`: Path to save the output file.
- `-c` or `--concurrency`: Number of concurrent workers. Recommended value: 50.
- `-t` or `--threads`: Number of threads per worker. Recommended value: 3.

**Note:** For optimal performance and to avoid potential damage to the running OS, it's recommended to use `-c 50` and `-t 3`.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to open an issue on the [GitHub repository](https://github.com/sanjai-AK47/Httrpober).

## Thanks and Keep on Checking for my Recon Tools
