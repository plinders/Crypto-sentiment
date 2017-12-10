import gdax, time, signal, os, csv
from datetime import datetime

def killme(signum, f):
    wsClient.close()
    os._exit(0)

class myWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["BTC-USD"]
        self.message_count = 0
        print("Lets count the messages!")
    def on_message(self, msg):
        self.message_count += 1
        try:
            if msg["type"] == 'match':
                self.price = float(msg["price"])
                self.time = datetime.strptime(msg["time"], '%Y-%m-%dT%H:%M:%S.%fZ')

        except KeyError:
            pass

    def on_close(self):
        print("-- Goodbye! --")

wsClient = myWebsocketClient()
wsClient.start()
signal.signal(signal.SIGINT, killme)
#print(wsClient.url, wsClient.products)
while True:
    #if wsClient.message_count > 1:
    try:
        with open("gdax-out.txt", "a") as g:
            writer = csv.writer(g)
            writer.writerow([wsClient.time, wsClient.price])
    except AttributeError:
        print(f"No message yet")
        pass
    time.sleep(1)
