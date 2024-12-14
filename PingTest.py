import datetime
import time
import pandas as pd

from ping3 import ping

path = "test.xlsx"

def test_round_trip(host):
    comment = input("write a comment about this session: ")
    end_time = time.time() +300
    while time.time() < end_time:
        # Perform a ping to the host
        latency = ping(host, timeout=4)
        
        if latency is not None:
            # Convert latency from seconds to milliseconds
            now = datetime.datetime.now()
            lag = latency *1000
            print(f"{latency * 1000:.2f} ms {now}")
            if latency*1000 > 0:
                old_df=pd.read_excel(path)
                dict={'latency in ms': [lag], 'timestamp': [now], 'comment': [comment]}
                df = pd.DataFrame(dict)
           # df.to_excel("pingexcel.xlsx")
                new_df = pd.concat([old_df, df], ignore_index=True)
                new_df.to_excel(path, index=False)
        else:
            print("timed out")
            


if __name__ == "__main__":
    test_round_trip("google.com")