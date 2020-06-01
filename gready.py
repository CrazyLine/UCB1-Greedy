from numpy import random
import matplotlib.pyplot as plt

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
eplison = 1
count = dict(zip(list(range(1, N+1)), [0] * N))  # Record the times of each arm
u={}
for i in range(N):
    u[i+1]=R[i+1]*prob[i+1]
u=sorted(u.items(), key=lambda d:d[1], reverse = True)
best_k=u[0][0]
best_u=u[0][1]

Q = dict(zip(list(range(1, N+1)), [0] * N))
r = 0
c=0.5
d_list=[]
u_list=[]
for i in range(T):
    if random.random() < eplison:
        k = random.choice(K)
    else:
        k = max(Q, key=Q.get)
    v = random.choice([R[k], 0], p=[prob[k], 1 - prob[k]])
    r += v*prob[k]
    Q[k] = (Q[k] * count[k] + v*prob[k]) / (count[k] + 1)
    temp_u=round(best_u*(i+1)-r,2)
    u_list.append(temp_u)
    count[k] = count[k] + 1
    d=best_u-prob[k]*v
    if d!=0:
        d_list.append(d)
    d = min(d_list)
    eplison=min(1,c*(N)/((i+1)*(d**2)))

print('eplision: ',eplison)
print("The total reward is {}".format(r))
plt.plot(list(range(T)),u_list)
plt.xlabel('turn')
plt.ylabel('regret')
print('Number of times each slot machine is selected: ',count)
print('The best slot machine to choose: ',best_k)
plt.show()