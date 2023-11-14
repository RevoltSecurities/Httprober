# Httrpober

Httrpober is a versatile subdomain Probing tool designed to efficiently probe for alive subdomains from a provided list. It offers customizable concurrency and threading options to balance speed and resource utilization. This tool is built under the Apache 2.0 license.

## Features

- Probe for alive subdomains from a list of subdomains and urls
- Customize concurrency and thread settings for optimal performance.
- Save the output to a file.
- Prevent potential damage to the operating system by following recommended concurrency and thread values.
- Support stdin and stdout to pipe the output
- Easy installation and tool management
- Integrated updating system
- Support Concurrency and Threading for Multiple probing

## Usage:

```bash
httprober --help
usage: httprober [-h] [-f FILENAME] [-o OUTPUT] [-s] [-c CONCURRENCY] [-t THREADS] [-up]

[INFO]: A fast alive subdomains finder with new generation HTTPX client

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        [INFO]: A filename that contains list of subdomains to probe and find alive subdomains
  -o OUTPUT, --output OUTPUT
                        [INFO]: File name to save the output
  -s, --silent          [INFO]: Switiching Silent flag will make the output to pipe
  -c CONCURRENCY, --concurrency CONCURRENCY
                        [INFO]: Concurrency level to make fast process
  -t THREADS, --threads THREADS
                        [INFO]: Threading level to make fast process
  -up, --update         [INFO]: Updated the Httprober to later version

```
## Installation

### Method 1:

1.Pip Installation:

```bash
pip install httprober
```
### Method 2:

2.Clone the repository:
   ```bash
   git clone https://github.com/sanjai-AK47/Httrpober.git
   cd Httrpober
   pip install .
   httprober --help
   ```
## Example Run on Httprober:


![Screenshot from 2023-11-14 22-15-43](https://github.com/sanjai-AK47/Httprober/assets/119435129/1f4b7eed-8cdf-4afb-ae97-fa8e804c67ca)


## Issues:

For questions, issues or suggestions, feel free to open an issue on the [GitHub repository](https://github.com/sanjai-AK47/Httrpober).

## Inspired:

To develop this tool in python for more concurrency and accurate results than others [tomnomnom's httprobe](https://github.com/tomnomnom/httprobe) Inspired me.

## INformation:

This tool is developed by [D.Sanjai Kumar](https://www.linkedin.com/in/d-sanjai-kumar-109a7227b/) for support the open source community for CyberSecurity and Ethical Hacking and The Httprober is built for reconnaissance and ethical hacking purposes and developer is not responsible for any unethical purposes so please use the Httprober with responsible and Ethically . Happy Hacking Hackers you can support my contribution by giving a ⭐ to the Httprober which motivate me to develop more like this ♥️.
