import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import decorate

triangle = TriangleSignal().make_wave(duration=0.01)
#创建一个时长为0.01s的三角波
#triangle.plot()
#decorate(xlabel='Time (s)')

spectrum = triangle.make_spectrum()
print('hs[0]=',spectrum.hs[0])

spectrum.hs[0] = 100
triangle.plot(color='gray')
#在图上吧原三角波变为灰色
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')

plt.show()

