import asyncio

def read_file():


def read_all(loop, fd):
	loop.add_reader(fd, functools.partial(read_file, 'arg1'=2), 12)
	loop.run_

