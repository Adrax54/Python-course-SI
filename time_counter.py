import time
from Onsets import Onsets_By_Insertion
from Onsets import Onsets_By_Bubble


def Timer(list,function):
    start = time.time()
    function(list)
    end = time.time()
    timer = end - start

    return timer

list_demo = ([1,9,55,4,2],3)


def TimerCompare(data):

  times = []

  times.append(Timer(data,Onsets_By_Insertion))
  times.append(Timer(data,Onsets_By_Bubble))

  return times

time_list = TimerCompare(list_demo)

print('Time Insertion Algorithm: =======>',time_list[0],'\nTime Bubble Algorithm: =======>',time_list[1])



