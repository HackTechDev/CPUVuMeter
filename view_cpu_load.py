import psutil

def get_cpu_load():
    cpu_load = psutil.cpu_percent(interval=1)
    return cpu_load

if __name__ == "__main__":
    while True:
        cpu_load = get_cpu_load()
        print(f"CPU Load: {cpu_load}%")

