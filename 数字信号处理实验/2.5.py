import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import decorate


def filter_spectrum(spectrum):
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    #将hs各个元素除以fs
    spectrum.hs[0] = 0
    #fs[0]=0不能除以0，所以自动让他等于0

wave1 = TriangleSignal(freq=440).make_wave(duration=0.5)
#建立一个频率为440hz的采样长度为0.5s的三角波wave
wave1.make_audio()
plt.subplot(311)
spectrum = wave1.make_spectrum()
#创建wave的频谱
spectrum.plot( color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)#self.hs = factor*self.hs
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave2 = spectrum.make_wave()
plt.subplot(312)
wave1.plot()
plt.subplot(313)
wave2.plot()
#filtered = spectrum.make_wave()
#filtered.write(filename="2.5.wav")

plt.show()