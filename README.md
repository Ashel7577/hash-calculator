# Hash Calculator

A Python-based hash calculator tool for penetration testing and security analysis. This tool supports multiple hash algorithms and is designed for security professionals conducting authorized assessments.

## Features

- Supports multiple hash algorithms (MD5, SHA-1, SHA-2 family, SHA-3 family)
- Calculates hashes for both strings and files
- Memory-efficient processing for large files
- Command-line interface for easy integration
- Batch processing of all supported algorithms

## Installation

1. Clone this repository or download the `hash_calculator.py` file
2. Ensure you have Python 3.6+ installed

## Usage

### Basic Hash Calculation

```bash
# Hash a string with default SHA-256
python hash_calculator.py -s "password123"

# Hash a file with SHA-256
python hash_calculator.py -f /path/to/file.txt

# Hash with specific algorithm
python hash_calculator.py -s "secret" -a md5
```

### Advanced Usage

```bash
# Calculate all hashes for a string
python hash_calculator.py -s "password" --all

# Calculate all hashes for a file
python hash_calculator.py -f /path/to/file.txt --all
```

## Supported Algorithms

- MD5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512
- SHA3-224
- SHA3-256
- SHA3-384
- SHA3-512

## Requirements

- Python 3.6 or higher
- No external dependencies

## Legal Notice

This tool is intended for authorized security testing only. Users must have explicit permission before testing any systems or networks. Unauthorized use is strictly prohibited.

## License

MIT License - see [LICENSE](LICENSE) file for details
