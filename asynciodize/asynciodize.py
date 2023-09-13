__author__ = "Daniel Peña Iglesias"
__copyright__ = "Copyright (C) 2023 Daniel Peña Iglesias"
__credits__ = ["Daniel Peña Iglesias"]
__license__ = "MIT"

from concurrent.futures import ThreadPoolExecutor
import asyncio
import multiprocessing
from functools import wraps 

default_executor = ThreadPoolExecutor(multiprocessing.cpu_count())

def asynciodize(default_fn=None, executor=default_executor):
    def wrapper_decorator(fn):
        @wraps(fn)
        async def wrapper_fn(*args, **kwargs):
            loop = asyncio.get_running_loop()
            return await loop.run_in_executor(executor, fn, *args, **kwargs)

        return wrapper_fn

    if default_fn is None:
        return wrapper_decorator
    else:
        return wrapper_decorator(default_fn)