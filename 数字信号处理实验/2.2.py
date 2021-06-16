
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal

class SawtoothSignal(Sinusoid):
    '''锯齿波的类'''
    def evaluate(self, ts):
        #cycle是自起始时间的周期数
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        #np.modf()能将一个数分为小数部分和整数部分
        ys = normalize(unbias(frac), self.amp)
        #frac的序列介于0到1
        #unbias将波形下移使其中心位于0
        #normalize将波形归一化到给定的振幅（amp）
        return ys

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#plt.subplot(511)#产生5行1列的第一个图
#plt.title(u"锯齿波的频谱")
sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
#制作波形长度为0.5s，每秒40000帧
#sawtooth.make_spectrum().plot()


#plt.subplot(513)
#plt.title(u"锯齿波（灰）&方波的频谱")
#sawtooth.make_spectrum().plot(color='gray')#将原锯齿波显示为灰色便于观察
#square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
#将方波的振幅调整为0.5便于比较
#square.make_spectrum().plot()

#plt.subplot(515)
plt.title(u"锯齿波（灰）&三角波的频谱")
sawtooth.make_spectrum().plot(color='gray')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
triangle.make_spectrum().plot()

plt.show()