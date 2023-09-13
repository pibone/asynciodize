# asynciodize

A simple decorator to "unblock" blocking functions using a threaded executor. Eases the usage of asyncio with subprocesses or multithreading.

Use it to decorate or wrap your blocking functions and convert them into coroutine based functions usable with async/await.

## Features
* Executes your function using your asyncio running loop.
* Executes your code in the executor of preference.
* By default creates a ThreadPoolExecutor with the using the total amount of cpus in the machine.

## Install

You may install this via the [`argexec`](https://pypi.org/project/asynciodize/) package on [PyPi](https://pypi.org):

```bash
pip3 install asynciodize
```

## Usage

The decorator may be applied to any Python function that meets the following requirements:
* Is not a member function in a class. DOES NOT SUPPORT SELF

Example (`foo.py`):
```python
#!/usr/bin/python3

import logging
import asyncio
from asynciodize import asynciodize 
import time

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")

def blocking_sleep_message(delay, message):
    logging.info(f"{message} received - waiting {delay} seconds")
    time.sleep(delay)
    logging.info(f"Printing {message}")

@asynciodize
def unblocking_fn(num, message):
    return blocking_sleep_message(num, message)

async def main():
    logging.info("Main started")
    await asyncio.gather(
        unblocking_fn(1, 'First message'),
        asynciodize(blocking_sleep_message)(2, 'Second message'),
        asynciodize(blocking_sleep_message)(3, 'Third message'),
        unblocking_fn(4, 'Fourth message'),
    )
    logging.info("Main Ended")

if __name__ == '__main__': 
    asyncio.run(main())
```