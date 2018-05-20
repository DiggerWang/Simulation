#d(n)期望的平均排队时间
#q(n)期望的平均队长
#u(n)期望的平均繁忙时间
import random
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

'''
Customer_list的结构:
Customer_list = [
    [到达时间，离开时间]
    ……
]
Event_list的结构:
Event_list = [

]
'''
#定义全局变量
global cus_num,sim_time,server_status,num_customers_served,num_in_queue,time_last_event,num_customers_delayed,total_of_delays,area_num_in_queue,area_server_status,time_end,time_next_event,next_event_type,max_queue,max_delay,num_customers_delayed1min,num_customers_balked,mean_interarrival,Queue_limit,mean_service
max_queue = 0
max_delay = 0
num_customers_delayed1min=0
num_customers_balked=0
Delay_list = []
Event_list = []
time_next_event = []
time_event_list = []
num_in_queue_list = []
server_status_list = []
time_arrive_list=[]
time_departure_list=[]
time_system_list=[]
rule = 0

def Global():
    global max_queue,max_delay,num_customers_delayed1min,num_customers_balked,Delay_list,Event_list,time_next_event,time_event_list,num_in_queue_list,server_status_list,time_arrive_list,time_departure_list,time_system_list
    max_queue = 0
    max_delay = 0
    num_customers_delayed1min = 0
    num_customers_balked = 0
    Delay_list = []
    Event_list = []
    time_next_event = []
    time_event_list = []
    num_in_queue_list = []
    server_status_list = []
    time_arrive_list = []
    time_departure_list = []
    time_system_list = []

#定义输入参数
#seed = input("输入随机数种子:")
#random.seed(seed)
'''
print("1.Fixed number of serviced custiomers rule\n2.Fixed service time rule\n3.Fixed queue length rule")
rule = input("输入排队规则:")
if rule == "1":#服务到一定顾客数后立即结束
    mean_interarrival = 1/float(input("mean arrive time:"))
    mean_service = 1/float(input("mean service time:"))
    cus_num = float(input("number of customers:"))
    Queue_limit = 1.0e+30
if rule == "2":#到了结束时间后，不在接受新顾客，服务到系统为空为止
    mean_interarrival = 1/float(input("mean arrive time:"))
    mean_service = 1/float(input("mean service time:"))
    time_end = float(input("total simulation time:"))
    Queue_limit = 1.0e+30
if rule == "3":#确定队长，若高于队长，则拒绝顾客，到了服务时间立即结束
    mean_interarrival = 1/float(input("mean arrive time:"))
    mean_service = 1/float(input("mean service time:"))
    time_end = float(input("total simulation time:"))
    Queue_limit = int(input("maximum length of queue:"))
'''

seed = 10
result_list = []

'''初始化排队系统'''
def Initialize():
    global sim_time,server_status,num_in_queue,time_last_event,num_customers_delayed,total_of_delays,area_num_in_queue,area_server_status,time_next_event,num_customers_served,mean_interarrival,max_queue,max_delay
    sim_time = 0.0 #当前时间
    server_status = 0 #0代表空闲,1代表忙碌
    num_in_queue = 0 #在队列中的人数
    time_last_event = 0.0 #最后一个事件的时间
    num_customers_delayed = 0 #等待的顾客数量
    num_customers_served = 0
    total_of_delays = 0.0 #总延误时间
    area_num_in_queue = 0.0 #服务时间内队长的总和 area_num_in_queue = num_in_queue * time_since_last_event
    area_server_status = 0.0
    if rule == 1:
        time_next_event = [sim_time + random.expovariate(mean_interarrival), 1.0e+30]
    if rule == 2:
        time_next_event = [sim_time+random.expovariate(mean_interarrival), 1.0e+30, time_end]
    if rule == 3:
        time_next_event = [sim_time+random.expovariate(mean_interarrival), 1.0e+30, time_end]
    #time_arrive_list.append(time_next_event[0])修改

'''计时系统'''
def Timing():
    global sim_time,next_event_type,time_next_event
    min_time_next_event = 1.0e+29
    next_event_type = 0

    for i in range(0,len(time_next_event)):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i+1

    if next_event_type == 0:
        print("Event list empty at time "+str(float(sim_time)))

    sim_time = min_time_next_event


'''到达函数'''
def Arrive():
    global server_status,num_in_queue,time_next_event,total_of_delays,num_customers_delayed,next_event_type,sim,max_queue,num_customers_balked,Queue_limit,mean_service
    time_next_event[0] = sim_time + random.expovariate(mean_interarrival)
    #time_arrive_list.append(time_next_event[0])
    time_arrive_list.append(sim_time)#修改
    if server_status == 1:
        #num_in_queue += 1
        if num_in_queue > Queue_limit:
            print("The queue is overflow at time "+str(float(sim_time)))
            del time_arrive_list[-1]
            #num_in_queue -= 1
            num_customers_balked += 1
        else:
            Delay_list.append(sim_time)
            num_customers_delayed += 1
            num_in_queue += 1
    else:
        delay = 0.0
        total_of_delays += delay
        #num_customers_delayed += 1
        server_status = 1
        time_next_event[1] = sim_time + random.expovariate(mean_service)
        #time_departure_list.append(time_next_event[1])
    if num_in_queue > max_queue:
        max_queue = num_in_queue



'''离开函数'''
def Depart():
    global server_status,num_in_queue,time_next_event,total_of_delays,num_customers_delayed,max_delay,num_customers_delayed1min,num_customers_served
    time_departure_list.append(sim_time)#修改
    num_customers_served += 1
    if num_in_queue == 0:
        server_status = 0
        time_next_event[1] = 1.0e+30
    else:
        num_in_queue -= 1
        delay = sim_time - float(Delay_list[0])
        if delay > max_delay:
            max_delay = delay
        total_of_delays += delay
        #num_customers_delayed += 1
        if delay >1:
            num_customers_delayed1min +=1
        time_next_event[1] = sim_time + random.expovariate(mean_service)
        #time_departure_list.append(time_next_event[1])修改
        del Delay_list[0]


'''时间状态更新'''
def Update_time_avg_stats():
    global sim_time,time_last_event,num_in_queue,area_num_in_queue,area_server_status,server_status
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_queue += num_in_queue * time_since_last_event
    area_server_status += server_status * time_since_last_event
    #将信息存入list
    time_event_list.append(sim_time)
    num_in_queue_list.append(num_in_queue)
    server_status_list.append(server_status)



'''输出排队结果'''
def Report():
    global total_of_delays,num_customers_delayed,area_num_in_queue,sim_time,area_server_status,num_customers_delayed,time_system_list,result_list
    '''
    print("The average delay in queue:"+str(float(total_of_delays/num_customers_served)))
    print("The average length of the queue:"+str(float(area_num_in_queue/sim_time)))
    print("Utilization:"+str(float(area_server_status/sim_time)))
    
    print("The time-average number in the system:"+str(float((area_server_status+area_num_in_queue)/sim_time)))
    time_system_list=(pd.Series(time_departure_list)-pd.Series(time_arrive_list)).dropna()
    print("The average total time in the system:"+str(sum(time_system_list)/len(time_system_list)))
    print("The maximum queue length:"+str(max_queue))
    print("The maximum delay in queue:"+str(max_delay))
    print("The maximum time in the system:"+str(max(time_system_list)))
    print("The proportion of customers having a delay in queue in excess of 1 minute :"+str(num_customers_delayed1min/num_customers_served))
    
    print("The number of customers balked:"+str(num_customers_balked))
    
    print("The number of customers served:"+str(num_customers_served))
    print("The number of customers delayed:"+str(num_customers_delayed))
    print("The simulation time:"+str(sim_time))
    '''
    time_system_list = (pd.Series(time_departure_list) - pd.Series(time_arrive_list)).dropna()
    result_list = [str(round(float(total_of_delays/num_customers_served),3)),str(round(float(area_num_in_queue/sim_time),3)),str(round(float(area_server_status/sim_time),3)),
                   str(round(float((area_server_status + area_num_in_queue) / sim_time),3)),str(round(sum(time_system_list)/len(time_system_list),3)),
                   str(round(max_queue,3)),str(round(max_delay,3)),str(round(max(time_system_list),3)),str(round(num_customers_delayed1min/num_customers_served,3)),
                   str(num_customers_balked),str(num_customers_served),str(num_customers_delayed),str(sim_time)]
    return result_list


'''画出area图'''
def Plot():
    global area_num_in_queue,area_server_status
    x = time_event_list
    y_1 = num_in_queue_list
    y_2 = server_status_list
    a = []
    for i in range(1,len(x)):
        a.append(x[i]-0.0000001)
    for i in range(len(a)):
        x.insert(2*i+1,a[i])
    a.clear()

    for i in range(1,len(y_1)):
        a.append(y_1[i-1])
    for i in range(len(a)):
        y_1.insert(2*i+1,a[i])
    a.clear()

    for i in range(1,len(y_2)):
        a.append(y_2[i-1])
    for i in range(len(a)):
        y_2.insert(2*i+1,a[i])
    #plt.figure(figsize=(15,8),dpi=100)
    #plt.plot(x, y_2, color="red")
    #plt.figure(figsize=(15,8),dpi=100)
    plt.figure()
    plt.plot(x, y_1, color="orange",linewidth=1)
    plt.xlabel('Sim time')
    plt.ylabel('Customer number in queue')
    plt.grid(alpha=0.5)
    plt.savefig('./Pic_data/Queue/Queue_1.png',bbox_inches = "tight")
    #plt.show()

def Write(a):
    global area_num_in_queue,area_server_status
    x = time_event_list
    y_1 = num_in_queue_list
    y_2 = server_status_list
    data = pd.DataFrame(np.array([x,y_1,y_2]).T,columns=('Sim time','Length of queue','Service status'))
    data.to_csv('./File_data/Queue/Queue_Data_'+str(a)+'.csv')

def Plot_2(p,q):
    global area_num_in_queue,area_server_status
    for i in time_event_list:
        if p <= i:
            m = time_event_list.index(i)
            break
    for i in time_event_list:
        if q <= i:
            n = time_event_list.index(i)-1
            break
    x = time_event_list[m:n]
    y_1 = num_in_queue_list[m:n]
    y_2 = server_status_list[m:n]
    a = []
    for i in range(1,len(x)):
        a.append(x[i]-0.0000001)
    for i in range(len(a)):
        x.insert(2*i+1,a[i])
    a.clear()

    for i in range(1,len(y_1)):
        a.append(y_1[i-1])
    for i in range(len(a)):
        y_1.insert(2*i+1,a[i])
    a.clear()

    for i in range(1,len(y_2)):
        a.append(y_2[i-1])
    for i in range(len(a)):
        y_2.insert(2*i+1,a[i])
    plt.figure()
    plt.plot(x, y_1, color="orange",linewidth=1)
    plt.xlabel('Sim time')
    plt.ylabel('Customer number in queue')
    plt.grid(alpha=0.5)
    plt.savefig("./Pic_data/Queue/Queue_"+str(p)+"_"+str(q)+".png",bbox_inches = "tight")


def Run():
    global next_event_type, num_in_queue, num_customers_delayed,result_list
    random.seed(seed)
    Global()
    if rule == 1:
        Initialize()
        while num_customers_served < cus_num:
            Timing()
            Update_time_avg_stats()
            if next_event_type == 1:
                Arrive()
            elif next_event_type == 2:
                Depart()
        result_list = Report()
        Plot()
    if rule == 2:
        Initialize()
        while True:
            Timing()
            Update_time_avg_stats()
            if next_event_type == 1:
                Arrive()
            elif next_event_type == 2:
                Depart()
            elif next_event_type == 3:
                break
        time_next_event[0] = 1.0e+30
        time_next_event[2] = 1.0e+30
        while server_status == 1:
            Timing()
            Update_time_avg_stats()
            Depart()
        result_list = Report()
        Plot()
    if rule == 3:
        Initialize()
        while True:
            Timing()
            Update_time_avg_stats()
            if next_event_type == 1:
                Arrive()
            elif next_event_type == 2:
                Depart()
            elif next_event_type == 3:
                break
        result_list = Report()
        Plot()


