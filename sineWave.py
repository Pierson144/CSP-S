# sine_wave.py
import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency=10, duration=1, sample_rate=1000):
    time = np.arange(0, duration, 1/sample_rate)
    amplitude = np.sin(2 * np.pi * frequency * time)

    plt.plot(time, amplitude)
    plt.title(f"Sine Wave - Frequency: {frequency} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()
