# example

## code

```python
from cmdline_adapter import call

def example(word: str, n: int = 1):
    for _ in range(n):
        print(word)
    return n

result = call(example)
```

## execution

```shell
$ python example.py --help
usage: example.py [-h] --word WORD [--n N]

options:
  -h, --help   show this help message and exit
  --word WORD  str
  --n N        int
```


```shell
$ python example.py --word="Hello World"
Hello World
```

```shell
$ python example.py --word="Hello World" --n=3
Hello World
Hello World
Hello World
```
