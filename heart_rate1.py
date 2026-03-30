import math
import time

def make_heartbeat(t, heart_rate):
    secounds_per_beat = 60/ heart_rate
    position_in_beat = (t %secounds_per_beat)/ secounds_per_beat

    if position_in_beat < 0.3:
        value = (position_in_beat/0.3) ** 2
    else:
        value = math.exp(-(position_in_beat - 0.3) * 8)

    noise = math.sin(t * 50) * 0.05
    breathing = math.sin(t * 0.2) * 0.1

    return value + noise + breathing

print(make_heartbeat(0.5, 75))
print("=" * 50)
print("Heart Rate Monitor")
print("=" * 50)

heart_rate_target = 75
beat_count = 0
last_beat_t = 0
peak_times = []
start = time.time()

print("Starting...")
for i in range(100):
    now = time.time() - start
    signal = make_heartbeat(now, heart_rate_target)
    print(f'{now:.2f}: {signal:3f}')
    time.sleep(0.01)

print("Done")

print ("Looking for heartbeats...")

for i in range(500): 
    now = time.time() - start
    signal = get_heartbeat(now, heart_rate_target)

    if signal > 0.5 and (now - last_beat_time) > 0.35
        last_beat_time = now
        beat_count = beat_count + 1
        peak_times.append(now)
        print(f"BEAT {beat_count} at {now:.2f} seconds! Signal: {signal:.3f}")
    time.sleep(0.01)
