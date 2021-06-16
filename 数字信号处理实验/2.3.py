import matplotlib.pyplot as plt
from thinkdsp import SquareSignal
from thinkdsp import decorate

square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
#创建一个频率为1100HZ方波,然后对其采样长度为0.5s，采样帧率为10000帧每秒
wave2=square.make_spectrum()
#filtered = wave.make_wave()
#filtered.write(filename="2.5.wav")

wave2.plot()
decorate(xlabel='Frequency (Hz)')

plt.show()