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
rc('figure.subplot', left=0.25, right=0.95, top=0.95, bottom=0.2)
rc('axes', linewidth=0.5)
rc('lines', linewidth=0.5)


with open(sys.argv[1]) as first:
    series1 = [[float(y.strip()) for y in x.split()] for x in first.readlines()]

with open(sys.argv[2]) as second:
    series2 = [[float(y.strip()) for y in x.split()] for x in second.readlines()]

#fig = plt.figure()

#plt.subplots_adjust(wspace=0.2)

plt.subplot(111)

plt.errorbar([x[0] for x in series2], 
             [x[2] for x in series2], 
             yerr=[[x[2] - x[1] for x in series2], [x[3] - x[2] for x in series2]], 
             color='0.6', marker='x', markersize=3, linestyle='-', label=r'Hadoop')

plt.errorbar([x[0] for x in series1], 
             [x[2] for x in series1], 
             yerr=[[x[2] - x[1] for x in series1], [x[3] - x[2] for x in series1]], 
             fmt='0.0', marker='o', markersize=3, linestyle='-', label=r'\textsc{Ciel}')


leg = plt.legend(loc=2)
leg.get_frame().set_lw(0.5)

plt.xlim(0, 110)
plt.ylim(0, 1000)
plt.yticks([0, 200, 400, 600, 800, 1000])#, ['0', '200', '400', '600', '800', '1000'])
plt.xticks([20, 40, 60, 80, 100])#, ['20', '40', '60', '80', '100'])

# plt.plot(xseries1, yseries1, 'b-')
# plt.xlim(0, math.ceil(max(duration1, duration2)))
# plt.ylim(0, 21)
# plt.xticks([])
# plt.yticks([0, 20], ['0', '20'])

# plt.ylabel(r'\textsc{Ciel}')

# plt.subplot(212)
# plt.plot(xseries2, yseries2, 'r-')
# plt.xlim(0, math.ceil(max(duration1, duration2)))
# plt.ylim(0, 21)
# plt.xticks([0, math.ceil(duration1), math.ceil(duration2)])
# plt.yticks([0, 20], ['0', '20'])

plt.ylabel('Iteration length (s)')
plt.xlabel('Number of tasks')
# plt.xticks((0, math.ceil(min(duration1, duration2)), math.ceil(max(duration1, duration2))), ('0', str(int(math.ceil(min(duration1, duration2)))), str(int(math.ceil(max(duration1, duration2))))))


plt.savefig('kmeans-vary-tasks.pdf', format='pdf')

plt.show()
