import random
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D as ax
import numpy as np

global sim_time,initial_inv_level,time_last_event,total_ordering_cost,area_holding,area_shortage,mean_interdemand,num_months,next_event_type,prob_distrib_demand,area_holding,area_shortage,smalls,bigs,ran,amount,inv_list
sum_demand = 0
order_num = 0
express_num = 0
time_next_event = []
cost_list = []
inv_list = []
spoiled_list = []
sim_time_list = []
inv_level_list = []
event_list = []

'''定义输入'''
'''
initial_inv_level = int(input("输入初始库存水平:"))
mean_interdemand = 1/float(input("输入需求到达参数:"))
prob_distrib_demand = input("输入需求数列:").split(",")
smalls = int(input("输入检查点:"))
bigs = int(input("输入订货量:"))
minlag = float(input("输入货物最短到达时间:"))
maxlag = float(input("输入货物最长到达时间:"))
setup_cost = float(input("输入仓库建设成本:"))
incremental_cost = float(input("输入订货成本:"))
shortage_cost = float(input("输入缺货成本:"))
holding_cost = float(input("输入持有成本:"))
num_months = int(input("输入仿真的月数:"))
evaluate_interval = float(input("输入检查间隔:"))
'''

initial_inv_level = 10
mean_interdemand = 10
number_of_demand = 4
prob_distrib_demand = [0.163,0.500,0.833,1.000]
distrib_demand = [1,2,3,4]
minlag = 0.5
maxlag = 1
setup_cost = 32
incremental_cost = 3
shortage_cost = 5
holding_cost = 1
num_months = 120
evaluate_interval = 1.0
minlag_f = 0.25
maxlag_f = 0.5
overdue_min = 1.5
overdue_max = 2.5
setup_cost_2 = 48
incremental_cost_2 = 4
seed = 10
result_list = []

min_s = 0
max_s = 40
min_S = 40
max_S = 80

'''生成需求数列'''
'''
for i in range(number_of_demand):
    a = round(1/float(input("Probability of demand size = "+str(i+1)+":")))
    for j in range(a):
        prob_distrib_demand.append(i+1)
'''

choice_1 = '0'
choice_2 = '0'

def Global():
    global sum_demand,time_next_event,cost_list,inv_list,spoiled_list,sim_time_list,inv_level_list,event_list
    sum_demand = 0
    time_next_event = []
    inv_list = []
    spoiled_list = []
    sim_time_list = []
    inv_level_list = []
    event_list = []

def Rand():
    global number_of_demand,prob_distrib_demand,distrib_demand
    for i in range(number_of_demand):
        if random.random() < prob_distrib_demand[i]:
            return distrib_demand[i]
            break


'''初始化函数'''
def Initialize():
    global sim_time,inv_level,initial_inv_level,time_last_event,total_ordering_cost,area_holding,area_shortage,amount,time_next_event,ran,inv_list,spoiled_list,cost_list,sum_demand,order_num,express_num
    sim_time = 0.0
    ran = 0
    sum_demand = 0
    order_num = 0
    express_num = 0
    inv_level = initial_inv_level
    time_last_event = 0.0
    total_ordering_cost = 0.0
    area_holding        = 0.0
    area_shortage       = 0.0
    time_next_event = [1.0e+30,sim_time + random.expovariate(mean_interdemand),num_months,0.0]
    inv_list.clear()
    if initial_inv_level > 0:
        for i in range(initial_inv_level):
            inv_list.append(random.uniform(overdue_min,overdue_max))
    #print(random.expovariate(mean_interdemand))


'''计时函数'''
def Timing():
    global next_event_type,sim_time
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(len(time_next_event)):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i+1

    #如果事件空了，则暂停仿真
    if next_event_type == 0:
        print("Event list empty at time"+str(float(sim_time)))

    sim_time = min_time_next_event


'''订货到达'''
def Order_arrival():
    global inv_level,amount,sim_time,inv_list
    if inv_level+amount > 0:
        for i in range(amount+inv_level):
            inv_list.append(sim_time+random.uniform(overdue_min,overdue_max))
    inv_level += amount
    time_next_event[0] = 1.0e+30


'''改变仓库货物'''
def Inv_update(ran):
    global sum_demand,inv_list
    del inv_list[:ran]
    sum_demand += ran #记录总需求


'''需求函数'''
def Demand():
    global inv_level,sim_time,ran,order_num
    ran = Rand()
    inv_level -= ran
    Inv_update(ran)
    time_next_event[1] = sim_time + random.expovariate(mean_interdemand)
    if inv_level < 0:
        order_num += 1


'''评估函数'''
def Evaluate():
    global inv_level,smalls,amount,total_ordering_cost,sim_time,order_num,express_num,setup_cost_2,incremental_cost_2
    if inv_level < smalls:
        order_num += 1
        amount = bigs-inv_level
        if choice_1 == '0':
            total_ordering_cost += setup_cost + incremental_cost * amount
            time_next_event[0] = sim_time + random.uniform(minlag,maxlag)
        if choice_1 == '1':
            if inv_level >= 0:
                total_ordering_cost += setup_cost + incremental_cost * amount
                time_next_event[0] = sim_time + random.uniform(minlag,maxlag) #订货到达
            else:
                #加急货物
                total_ordering_cost += setup_cost_2+incremental_cost_2*amount
                time_next_event[0] = sim_time + random.uniform(minlag_f,maxlag_f)
                express_num += 1
    #此处的evaluate_interval(检查间隔)原本为1个月(代表月末检查)
    time_next_event[3] = sim_time + evaluate_interval


'''检查函数'''
def Inspect():
    global sim_time,inv_level,inv_list
    for i in range(len(inv_list)):
        if sim_time > inv_list[i]:
            spoiled_list.append(inv_list[i])
            inv_list[i] = -1
            inv_level -= 1
    len_1 = len(inv_list)
    for i in inv_list:
        if i == -1:
            inv_list.remove(i)
    len_2 = len(inv_list)
    return len_1-len_2


'''报告函数'''
def Report():
    global total_ordering_cost,num_months,area_holding,area_shortage,smalls,bigs,order_num,express_num
    avg_ordering_cost = total_ordering_cost / num_months
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    '''
    print("s = "+str(smalls))
    print("S = "+str(bigs))
    print("Average ordering cost per month:"+str(avg_ordering_cost))
    print("Average holding cost per month:"+str(avg_holding_cost))
    print("Average shortage cost per month:"+str(avg_shortage_cost))
    print("Average total cost per month:"+str(avg_shortage_cost+avg_holding_cost+avg_ordering_cost))
    print("The number of items discarded:"+str(float(len(spoiled_list))))
    print("The proportion of items discarded:"+str(float(len(spoiled_list)/(len(inv_list)+len(spoiled_list)+sum_demand))))
    print("Expected proportion of backlog:"+str(float(order_num/len(sim_time_list))))
    print("Expected number of express orders:"+str(float(express_num)))
    '''
    result_list = [str(round(avg_ordering_cost,3)),str(round(avg_holding_cost,3)),str(round(avg_shortage_cost,3)),str(round(avg_shortage_cost+avg_holding_cost+avg_ordering_cost,3)),
                   str(round(float(len(spoiled_list)),3)),str(round(float(len(spoiled_list)/(len(inv_list)+len(spoiled_list)+sum_demand)),3)),
                   str(round(float(order_num / len(sim_time_list)),3)),str(round(float(express_num),3))]
    return result_list


'''总成本函数'''
def Cost():
    global total_ordering_cost, num_months, area_holding, area_shortage
    avg_ordering_cost = total_ordering_cost / num_months
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    return avg_ordering_cost+avg_holding_cost+avg_shortage_cost


'''时间更新函数'''
def Update_time_avg_stats():
    global sim_time,time_last_event,inv_level,area_holding,area_shortage
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    if inv_level < 0:
        area_shortage -= inv_level * time_since_last_event
    elif inv_level >= 0:
        area_holding += inv_level * time_since_last_event
    sim_time_list.append(sim_time)
    inv_level_list.append(inv_level)


'''最优化(s,S)函数'''
def Opimizer():
    global smalls, bigs, amount, ran, inv_level, seed, result_list, num_months,cost_list
    min_total_cost = 1.0e+30
    for i in range(min_s,max_s):
        for j in range(min_S,max_S):
            smalls = i
            bigs = j
            random.seed(seed)
            Global()
            Initialize()
            Evaluate()
            while True:
                Timing()
                Update_time_avg_stats()
                if next_event_type == 1:
                    Order_arrival()
                elif next_event_type == 2:
                    if choice_2 == '1':
                        Inspect()
                    Demand()
                elif next_event_type == 4:
                    Evaluate()
                elif next_event_type == 3:
                    break
            total_cost = Cost()
            cost_list.append(total_cost)
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                best_s = smalls
                best_S = bigs
    return best_s, best_S, cost_list


'''画图函数'''
def Plot_surf(cost_list): #画出曲面图
    ax = plt.figure().add_subplot(111,projection='3d')
    x = np.arange(min_s,max_s,1)
    y = np.arange(min_S,max_S,1)
    '''
    for i in range(s_range):
        for j in range(S_range):
            x.append(i)
            y.append(j)
    '''
    s,S = np.meshgrid(x,y)
    z = np.array(cost_list)
    Total_Cost = z.reshape(s.shape)
    surf = ax.plot_surface(s,S,Total_Cost,rstride=1,cstride=1,cmap='coolwarm')
    plt.colorbar(surf,shrink=0.5,aspect=5)
    #ax.plot_trisurf(x,y,z)
    '''
    plt.pcolor(total_cost)
    plt.colorbar()
    plt.axis("tight")
    plt.title("Average total cost")
    plt.xlabel("bigs")
    plt.ylabel("smalls")
    '''
    plt.show()

'''
def Plot_scatter(): #画出散点图
    ax = plt.figure().add_subplot(111,projection='3d')
    x = np.arange(10,s_range,1)
    y = np.arange(50,S_range,1)
    s,S = np.meshgrid(x,y)
    z = np.array(cost_list)
    Total_Cost = z.reshape(s.shape)
    ax.scatter(s,S,Total_Cost)
    plt.show()
'''

#画出货物水平随时间的变化图
def Plot_inv(p,q):
    global inv_level_list,sim_time_list
    for i in range(len(sim_time_list)):
        if p <= sim_time_list[i]:
            p = i
            break
    for i in range(len(sim_time_list)):
        if q <= sim_time_list[i]:
            q = i-1
            break
    x = sim_time_list[p:q]
    y = inv_level_list[p:q]
    a = []
    for i in range(1,len(x)):
        a.append(x[i]-0.0000001)
    for i in range(len(a)):
        x.insert(2*i+1,a[i])
    a.clear()

    for i in range(1,len(y)):
        a.append(y[i-1])
    for i in range(len(a)):
        y.insert(2*i+1,a[i])
    a.clear()

    plt.figure()
    plt.plot(x,y,color='orange',linewidth=1)
    plt.xlabel('Sim time')
    plt.ylabel('Inventory Level')
    plt.grid(alpha=0.5)
    plt.savefig('Pic_data/Inventory/Inventory.png',bbox_inches = "tight")

#写入文件
def to_txt():
    global sim_time_list,event_list
    time = np.array(sim_time_list[1:])
    event = np.array(event_list)
    txt = np.concatenate([time,event]).reshape(2,len(time))
    file = pd.DataFrame(txt.T,columns=['Sim time','Event'])
    file.to_csv('Inventory_data/event.csv')


def Run():
    global smalls,bigs,amount,ran,inv_level,seed,result_list,num_months
    num_discard = 0
    random.seed(seed)
    Global()
    Initialize()
    Evaluate()
    while True:
        Timing()
        Update_time_avg_stats()
        if next_event_type == 1:
            Order_arrival()
            event_list.append(str(amount)+' goods have arrived.')
        elif next_event_type == 2:
            if choice_2 == '1':
                num_discard = Inspect()
            Demand()
            event_list.append('There occurs '+str(ran)+' demands. '+str(num_discard)+' overdue inventories are discarded.')
        elif next_event_type == 4:
            Evaluate()
            if inv_level >= 0:
                event_list.append('Order '+str(amount)+' goods.')
            else:
                event_list.append('Order '+str(amount)+' goods in express.')
        elif next_event_type == 3:
            break
    result_list = Report()
    to_txt()
    Plot_inv(0,num_months)
    #Plot_surf()
