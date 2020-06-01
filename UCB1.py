from numpy import random
import matplotlib.pyplot as plt
import math

N=10 # 100, 1000
K=[i+1 for i in range(N)] # Total number of arms
R = {}  # Reward corresponding to each arm
for i in range(N):
    R[i+1]=1
prob = {}  # Probability corresponding to each arm
equi_space=1/N
prob_start=round(1/N-1/(N*10),6)
for i in range(N):
    prob[i + 1] = prob_start
    prob_start = round(prob_start + equi_space, 6)
T = 10000
count = dict(zip(list(range(1, N+1)), [0] * N))  # Record the times of each arm
u={}
for i in range(N):
    u[i+1]=R[i+1]*prob[i+1]
u=sorted(u.items(), key=lambda d:d[1], reverse = True)
best_k=u[0][0]
best_u=u[0][1]

alpha=10
v_list = dict(zip(list(range(1, N+1)), [0] * N))

t=N
r = 0
u_list=[]
turn=1
for i in range(t):
    v = random.choice([R[i + 1], 0], p=[prob[i + 1], 1 - prob[i + 1]])
    v_list[i + 1] = v *prob[i+1]+ v_list[i + 1]
    count[i + 1] += 1
    r+=v
    temp_u = round(best_u * turn - r, 2)
    turn+=1
    u_list.append(temp_u)

for i in range(t,T):
    v_list1={}
    for j in range(N):
        v_list1[j+1]=(v_list[j+1] / count[j+1]) + math.sqrt(alpha * math.log(i+1) / count[j+1])
    v_list1 = sorted(v_list1.items(), key=lambda d: d[1], reverse=True)
    choose_k = v_list1[0][0]
    choose_u = R[choose_k]
    v=random.choice([R[choose_k], 0], p=[prob[choose_k], 1 - prob[choose_k]])
    count[choose_k] = count[choose_k] + 1
    v_list[choose_k]=v_list[choose_k]+v*prob[choose_k]
    r+=v*prob[choose_k]
    temp_u = round((best_u * turn) - r,2)
    turn+=1
    u_list.append(temp_u)

print("The total reward is {}".format(r))
print('Number of times each slot machine is selected: ',count)
print('The best slot machine to choose: ',best_k)
# print(best_u)
plt.plot(list(range(T)),u_list)
plt.xlabel('turn')
plt.ylabel('regret')
plt.show()



