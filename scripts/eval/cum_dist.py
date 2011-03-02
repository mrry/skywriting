#!/usr/bin/python

from matplotlib import rc, use
use('Agg')
import math
import sys
import matplotlib.pylab as plt

rc('font',**{'family':'serif','sans-serif':['Helvetica'],'serif':['Times'], 'size':8})
rc('text', usetex=True)
rc('legend', fontsize=8)
rc('figure', figsize=(2,2))
rc('figure.subplot', left=0.2, top=0.95, right=0.95, bottom=0.2)
rc('axes', linewidth=0.5)
rc('lines', linewidth=0.5)


with open(sys.argv[1]) as first:
    series1 = [float(x.strip()) for x in first.readlines()]

with open(sys.argv[2]) as second:
    series2 = [float(x.strip()) for x in second.readlines()]

#fig = plt.figure()

#plt.subplots_adjust(wspace=0.2)

plt.subplot(111)
plt.plot(series1, range(len(series1)), color='0.0', label=r'\textsc{Ciel}')
plt.plot(series2, range(len(series2)), color='0.6', label=r'Hadoop')

leg = plt.legend(loc=2, handletextpad=0.25)
leg.get_frame().set_lw(0.5)

plt.xlim(0, 220)
plt.ylim(0, 1500)
plt.yticks([0, 750, 1500], ['0', '0.5', '1'])
plt.xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])

# plt.plot(xseries1, yseries1, 'b-')
# plt.xlim(0, math.ceil(max(duration1, duration2)))
# plt.ylim(0, 21)
# plt.xticks([])
# plt.yticks([0, 20], ['0', '20'])
2
# plt.ylabel(r'\textsc{Ciel}')

# plt.subplot(212)
# plt.plot(xseries2, yseries2, 'r-')
# plt.xlim(0, math.ceil(max(duration1, duration2)))
# plt.ylim(0, 21)
# plt.xticks([0, math.ceil(duration1), math.ceil(duration2)])
# plt.yticks([0, 20], ['0', '20'])

plt.ylabel('$P(X < x)$')
plt.xlabel('Task duration (s)')
# plt.xticks((0, math.ceil(min(duration1, duration2)), math.ceil(max(duration1, duration2))), ('0', str(int(math.ceil(min(duration1, duration2)))), str(int(math.ceil(max(duration1, duration2))))))


plt.savefig('kmeans-map-cdf.pdf', format='pdf')

plt.show()
