import re


class SimpleTokenizerV2:
    """A simple word-level tokenizer with unknown-token support."""

    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {token_id: token for token, token_id in vocab.items()}

        if "<|unk|>" not in self.str_to_int:
            raise ValueError("Vocabulary must contain the <|unk|> token.")

    def encode(self, text):
        """Convert text into token IDs."""

        tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)

        tokens = [
            token.strip()
            for token in tokens
            if token.strip()
        ]

        tokens = [
            token if token in self.str_to_int else "<|unk|>"
            for token in tokens
        ]

        return [self.str_to_int[token] for token in tokens]

    def decode(self, ids):
        """Convert token IDs back into text."""

        tokens = [self.int_to_str[token_id] for token_id in ids]

        text = " ".join(tokens)

        text = re.sub(
            r'\s+([,.:;?_!"()\'])',
            r'\1',
            text,
        )

        return text