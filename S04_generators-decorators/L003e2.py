import time

def load_data_eagerly(count, delay=0.1) -> list[str]:
    """Simulates loading `count` items eagerly with a delay between each item.

    Args:
        count (int): The number of items to load
        delay (float, defaults to 0.1): The delay between each item loaded, in seconds.

    Returns:
        list(str): The loaded items
    """
    result = []
    for i in range(count):
        time.sleep(delay)
        result.append(f"Data item {i}.")

    return result

t0 = time.time()
data = load_data_eagerly(5)
t1 = time.time()
print(f"REGULAR : Returned {data} in {t1-t0:.2f}s")

def load_data_lazily(count, delay=0.1):
    """Simulates loading `count` items lazily with a delay between each item.

    Args:
        count (int): The number of items to load
        delay (float, defaults to 0.1): The delay between each item loaded, in seconds.

    Returns:
        generator(str): A generator that yields each data item.
    """
    for i in range(count):
        time.sleep(delay)
        yield f"Data item {i}."

data_gen = load_data_lazily(5)

while True:
    t0 = time.time()
    try:
        item = next(data_gen)
    except StopIteration:
        break
    t1 = time.time()
    print(f"Received data {item} in {t1-t0:.2f}s")