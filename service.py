from queue import Queue
import time
import threading
import subprocess
import concurrent.futures


def trigger(deviceName):
    params = [str(deviceName)]
    subprocess.run(['bash', 'restart.sh'] + params)


class Handler:
    def __init__(self):
        self.queue = Queue(-1)
        thread_read = threading.Thread(name="read data from queue", target=self.read_data, daemon=True)
        thread_read.start()

    def push_data(self, data):
        if str(data) not in self.queue.queue:
            self.queue.put(data)

    def read_data(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            while True:

                if self.queue.empty():
                    time.sleep(60)
                    continue

                deviceName = self.queue.get()
                executor.submit(trigger, deviceName)
