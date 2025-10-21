#!/usr/bin/env python3
"""
Hash Calculator for Penetration Testing
This tool calculates various hash values for files and strings, useful for:
- Verifying file integrity
- Password hash analysis
- Digital forensics
- Vulnerability assessment
"""

import hashlib
import argparse
import sys
import os

class HashCalculator:
    def __init__(self):
        self.supported_algorithms = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha224': hashlib.sha224,
            'sha256': hashlib.sha256,
            'sha384': hashlib.sha384,
            'sha512': hashlib.sha512,
            'sha3_224': hashlib.sha3_224,
            'sha3_256': hashlib.sha3_256,
            'sha3_384': hashlib.sha3_384,
            'sha3_512': hashlib.sha3_512,
        }
    
    def calculate_string_hash(self, text, algorithm='sha256'):
        """Calculate hash of a string"""
        if algorithm not in self.supported_algorithms:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        hasher = self.supported_algorithms[algorithm]()
        hasher.update(text.encode('utf-8'))
        return hasher.hexdigest()
    
    def calculate_file_hash(self, filepath, algorithm='sha256'):
        """Calculate hash of a file"""
        if algorithm not in self.supported_algorithms:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        hasher = self.supported_algorithms[algorithm]()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def calculate_all_hashes(self, data, is_file=False):
        """Calculate all supported hashes for data"""
        results = {}
        for algo in self.supported_algorithms:
            try:
                if is_file:
                    results[algo] = self.calculate_file_hash(data, algo)
                else:
                    results[algo] = self.calculate_string_hash(data, algo)
            except Exception as e:
                results[algo] = f"Error: {str(e)}"
        return results

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Hash Calculator")
    parser.add_argument('-s', '--string', help='String to hash')
    parser.add_argument('-f', '--file', help='File to hash')
    parser.add_argument('-a', '--algorithm', default='sha256', 
                       choices=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
                                'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512'],
                       help='Hash algorithm to use')
    parser.add_argument('--all', action='store_true', 
                       help='Calculate all supported hashes')
    
    args = parser.parse_args()
    
    # Validate input
    if not args.string and not args.file:
        print("Error: Please specify either a string (-s) or file (-f) to hash")
        parser.print_help()
        sys.exit(1)
    
    if args.string and args.file:
        print("Error: Please specify either a string or file, not both")
        sys.exit(1)
    
    calculator = HashCalculator()
    
    try:
        if args.all:
            if args.string:
                results = calculator.calculate_all_hashes(args.string)
                print(f"String: {args.string}")
            else:
                results = calculator.calculate_all_hashes(args.file, is_file=True)
                print(f"File: {args.file}")
            
            print("\nAll Hash Values:")
            print("-" * 50)
            for algo, hash_value in results.items():
                print(f"{algo.upper():<12}: {hash_value}")
        else:
            if args.string:
                result = calculator.calculate_string_hash(args.string, args.algorithm)
                print(f"String: {args.string}")
                print(f"{args.algorithm.upper()}: {result}")
            else:
                result = calculator.calculate_file_hash(args.file, args.algorithm)
                print(f"File: {args.file}")
                print(f"{args.algorithm.upper()}: {result}")
                
    except Exception as e:
        print(f"Error calculating hash: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
