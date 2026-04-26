import statistics
from utils.helpers import calculate_average

def class_average(students):
    avgs = [calculate_average(s.marks) for s in students if s.marks]
    return statistics.mean(avgs) if avgs else 0

def class_median(students):
    avgs = [calculate_average(s.marks) for s in students if s.marks]
    return statistics.median(avgs) if avgs else 0

def class_variance(students):
    avgs = [calculate_average(s.marks) for s in students if s.marks]
    return statistics.variance(avgs) if len(avgs) > 1 else 0