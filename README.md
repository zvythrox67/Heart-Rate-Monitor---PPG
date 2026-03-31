# Heart Rate Monitor (PPG Simulator)

A real-time heart rate monitor that simulates PPG (photoplethysmogram) signals, detects individual heartbeats, and calculates BPM using peak detection algorithms similar to clinical pulse oximeters.

## How It Works

1. **Generates realistic PPG waveform** - Simulates blood volume changes  each heartbeat
3. **Detects peaks** - Identifies individual heartbeats using threshold and timing
4. **Calculates BPM** 
5. **Displays live graph** -  bar graph of 

## Requirements

- Python 3.x

## How to Run

- (reminder: Once you start the code, the beats will generate endlessly until **Ctrl + C** is pressed.
```bash
python heart_rate_monitor.py
