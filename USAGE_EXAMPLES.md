# Usage Examples

## Basic Examples

### Hash a Password String
```bash
python hash_calculator.py -s "MySecretPassword123"
```

### Verify File Integrity
```bash
python hash_calculator.py -f important_document.pdf
```

## Advanced Examples

### Compare All Hash Types for a String
```bash
python hash_calculator.py -s "test" --all
```

### Use Specific Algorithm for Large Files
```bash
python hash_calculator.py -f large_archive.zip -a sha256
```

## Output Examples

For command: `python hash_calculator.py -s "hello" --all`

```
String: hello
All Hash Values:
--------------------------------------------------
MD5         : 5d41402abc4b2a76b9719d911017c592
SHA1        : aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA224      : 75641015b0d7872da45c33da5041a3a10031a8321e5065551f12a4b3
SHA256      : 2cf24dba4f21d4288094c14d9f59e30a1f2b4d7c5a7e19d7a59b3a5a3e4f8b04
SHA384      : 59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f
SHA512      : 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
SHA3_224    : 80092bbb05573183576b8dad583f1a2010d93c01072b06e4d746443e97337540
SHA3_256    : 335785f098ff1b17bf912a88b87638130c9870637031b5fcda361768a1e70aa6
SHA3_384    : ed4eeed5c157fbe6d55b801eb0ea70855dac9c9b133009e3d6269006230a0f57125d1d4cca0b1a2d09216f8cfd2a4740
SHA3_512    : 75d527c368f7e0e2a1a054b3d7d0824c0a9f250a8914bfd7d1d6b0eb58e50bc933c004d7d7d9a65923d8e004cd10509d1202b679bb809830dc2ca9094005811
```
