
import numpy 
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)#median||mode

print(x)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)
x = numpy.percentile(speed, 90)
print(x)