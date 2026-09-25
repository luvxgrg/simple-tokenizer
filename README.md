# Simple Tokenizer

A word-level tokenizer built from scratch in Python to understand the fundamentals of text tokenization used in Large Language Model (LLM) pipelines.

Instead of relying on an existing tokenizer library, this project implements the core tokenization process manually to explore how text is converted into numerical token IDs and reconstructed back into readable text.

## Features

- Word-level text tokenization
- Vocabulary-based token-to-ID mapping
- Token ID-to-text decoding
- Punctuation handling
- Unknown token (`<|unk|>`) support
- Special token support
- Reusable Python tokenizer module
- Basic tokenizer testing
- Jupyter notebooks documenting the learning process

## How It Works

The tokenizer follows a simple pipeline:

```text
Raw Text
   ↓
Tokenization
   ↓
Vocabulary Lookup
   ↓
Token IDs
   ↓
Numerical Representation
```

For example:

```text
Hello, world!
```

is split into tokens:

```text
["Hello", ",", "world", "!"]
```

These tokens can then be represented using numerical IDs:

```text
[0, 1, 2, 3]
```

The tokenizer can also decode the IDs back into readable text:

```text
Hello, world!
```

## Unknown Token Handling

If a word does not exist in the vocabulary, the tokenizer maps it to:

```text
<|unk|>
```

For example, if `Lovish` is not present in the vocabulary:

```text
Hello, Lovish!
```

the tokenizer can encode it using the unknown-token ID and decode it as:

```text
Hello, <|unk|>!
```

This prevents the tokenizer from failing when it encounters vocabulary it has not seen before.

## Project Structure

```text
simple-tokenizer/
│
├── tokenizer.py
├── test_tokenizer.py
├── tokenizer.ipynb
├── 1Tokenizer.ipynb
├── TheVerdict.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Usage

Import the tokenizer:

```python
from tokenizer import SimpleTokenizerV2
```

Create a vocabulary:

```python
vocab = {
    "Hello": 0,
    ",": 1,
    "world": 2,
    "!": 3,
    "<|unk|>": 4,
    "<|endoftext|>": 5,
}
```

Initialize the tokenizer:

```python
tokenizer = SimpleTokenizerV2(vocab)
```

### Encode Text

```python
text = "Hello, world!"

ids = tokenizer.encode(text)

print(ids)
```

Output:

```text
[0, 1, 2, 3]
```

### Decode Token IDs

```python
text = tokenizer.decode(ids)

print(text)
```

Output:

```text
Hello, world!
```

### Unknown Token Example

```python
text = "Hello, Lovish!"

ids = tokenizer.encode(text)

print(ids)
print(tokenizer.decode(ids))
```

Example output:

```text
[0, 1, 4, 3]
Hello, <|unk|>!
```

## Running the Test

The repository includes a simple test script for checking encoding, decoding, punctuation handling, and unknown tokens.

Run:

```bash
python test_tokenizer.py
```

Example output:

```text
Original: Hello, world!
Encoded: [0, 1, 2, 3]
Decoded: Hello, world!

Unknown token test:
Original: Hello, Lovish!
Encoded: [0, 1, 4, 3]
Decoded: Hello, <|unk|>!
```

## Version History

### v1.0

Initial word-level tokenizer implementation.

### v1.1

Added unknown-token and special-token handling.

### v1.2

Moved the tokenizer into a reusable Python module and added a standalone test script.

## Roadmap

This project will continue evolving as I explore more advanced tokenization and LLM concepts.

Planned areas include:

- Automated unit tests
- Vocabulary generation utilities
- Improved special-token handling
- Token frequency analysis
- Subword tokenization
- Byte Pair Encoding (BPE)
- Integration with a simple language-model pipeline

## Why I Built This

Tokenization is one of the first stages in an LLM pipeline. Before text can be processed by a language model, it must be transformed into numerical representations.

I built this project from scratch to better understand that process rather than treating tokenization as a black box provided by an external library.

The project will continue to evolve alongside my study of language models and NLP.

## Author

**Lovish Garg**

Software Development • Artificial Intelligence • LLM Fundamentals