import math
import time


print(make_heartbeat(0.5, 75))
print("=" * 50)
print("Heart Rate Monitor")
print("=" * 50)

heart_rate_target = 75
beat_count = 0
last_beat_t = 0
peak_times = []
start = time.time()

def make_heartbeat(t, heart_rate):
    seconds_per_beat = 60 / heart_rate
    position_in_beat = (t % seconds_per_beat) / seconds_per_beat

    if position_in_beat < 0.3:
        value = (position_in_beat / 0.3) ** 2
    else:
        value = math.exp(-(position_in_beat - 0.3) * 8)

    noise = math.sin(t * 50) * 0.05
    breathing = math.sin(t * 0.2) * 0.1

    return value + noise + breathing
