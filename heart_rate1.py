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

print ("Looking for heartbeats...")
print("Press Ctrl+C to stop")
print()

try:
    while True:
        now = time.time() - start
        signal = make_heartbeat(now, heart_rate_target)

        if signal > 0.7 and (now - last_beat_t) > 0.6:
            last_beat_t = now
            beat_count = beat_count + 1
            peak_times.append(now)

            if len(peak_times) >= 2:
                if len(peak_times) >= 3:
                    recent = peak_times[-3:]
                else:
                    recent = peak_times

                intervals = []
                for j in range(len(recent) - 1):
                    intervals.append(recent[j+1] - recent[j])
                avg_interval = sum(intervals) / len(intervals)
                current_bpm = 60 / avg_interval
            else:
                current_bpm = 0

            bar_length = int(signal * 40)
            bar = "█" * bar_length
            print(f"Beat {beat_count:4d} | {bar} | {current_bpm:3.0f} BPM")
        time.sleep(0.01)


except KeyboardInterrupt:
    print()
    print()
    print("Stopped!")
    print(f"Total beats: {beat_count}")
    if len(peak_times) >= 2:
        total_time = peak_times[-1] - peak_times[0]
        avg_bpm = 60 / (total_time / (len(peak_times) - 1))
        print(f"Average BPM: {avg_bpm: .0f}")



if len(peak_times) >= 2:
    total_time = peak_times[-1] - peak_times[0]
    avg_bpm = 60 / (total_time / (len(peak_times) - 1))
    print(f"Total time: {total_time:.1f} seconds")
    print(f"Average heart rate: {avg_bpm:.0f} BPM")
    print(f"Target heart rate: {heart_rate_target} BPM")

