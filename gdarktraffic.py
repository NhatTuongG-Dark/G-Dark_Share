import requests
import threading

def send_request(url):
    try:
        response = requests.get(url)
        print("[G-Dark] - Sent request to:", url)
    except requests.exceptions.RequestException as e:
        print("[G-Dark] - Error sending request to:", url)

def increase_traffic(url, num_threads):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    target_url = input("Nhập link website: ")
    num_threads = int(input("Nhập số luồng: "))

    increase_traffic(target_url, num_threads)