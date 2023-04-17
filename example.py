from cmdline_adapter import call


def example(word: str, n: int = 1):
    for _ in range(n):
        print(word)
    return n


result = call(example)
