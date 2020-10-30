from apscheduler.schedulers.blocking import BlockingScheduler
import time
sched = BlockingScheduler()




@sched.scheduled_job('interval', seconds=3)
def timed_job1():
    f=open("number.txt","w")
    num=time.clock()
    num=str(num)
    f.write(num)
    f.close()
    print('This job is run every three seconds.')

@sched.scheduled_job('interval', seconds=3)
def timed_job2():
    f=open("number1.txt","w")
    num=time.clock()
    num=str(num)
    f.write(num)
    f.close()
    print('This job is run every three seconds.')

sched.start()
