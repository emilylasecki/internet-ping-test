import datetime
import time
import pandas as pd
from ping3 import ping

filepath = "test2.xlsx" # Path to export data to

def test_round_trip(host):
    comment = input("write a comment about this session: ")
    end_time = time.time() +300 # 300 seconds = 5 minutes. Change this value for the test to run for a longer or shorter duration
    while time.time() < end_time:
        latency = ping(host, timeout=4) # Perform a ping to the host
        if latency is not None:
            now = datetime.datetime.now()
            lag = latency *1000  # Convert latency from seconds to milliseconds
            print(f"{latency * 1000:.2f} ms {now}")
            if latency*1000 > 0: # Set what you want to be recorded. If you only want to record when the ping spikes, change the threshold from 0 to 50+
                try:
                    old_df=pd.read_excel(filepath)
                    dict={'latency in ms': [lag], 'timestamp': [now], 'comment': [comment]}
                    df = pd.DataFrame(dict)
                    new_df = pd.concat([old_df, df], ignore_index=True)
                    new_df.to_excel(filepath, index=False, engine='openpyxl')
                except: 
                    dict={'latency in ms': [lag], 'timestamp': [now], 'comment': [comment]}
                    df = pd.DataFrame(dict)
                    df.to_excel(filepath, index=False, engine='openpyxl')
        else:
            print("connection request timed out") # it takes longer than 4 seconds to find a connection. Typically from a bad request, not a ping spike
            


if __name__ == "__main__":
    test_round_trip("google.com") # Change url if you want to ping a different internet address