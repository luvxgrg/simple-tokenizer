from tokenizer import SimpleTokenizerV2


vocab = {
    "Hello": 0,
    ",": 1,
    "world": 2,
    "!": 3,
    "<|unk|>": 4,
    "<|endoftext|>": 5,
}

tokenizer = SimpleTokenizerV2(vocab)


# Test encoding
text = "Hello, world!"
ids = tokenizer.encode(text)

print("Original:", text)
print("Encoded:", ids)
print("Decoded:", tokenizer.decode(ids))


# Test unknown token
unknown_text = "Hello, Lovish!"
unknown_ids = tokenizer.encode(unknown_text)

print("\nUnknown token test:")
print("Original:", unknown_text)
print("Encoded:", unknown_ids)
print("Decoded:", tokenizer.decode(unknown_ids))