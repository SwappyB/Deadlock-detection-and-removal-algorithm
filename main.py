import itertools
import time
class deadlock():
    reso=[]
    need=[]
    avail=[]
    priority=[]
    ss=[]
    d_solutions=[]
    process=[]
    previous_max=0
    n=0
    r=0
    def printchar(self,data=None):
        num=65
        for _ in range(data):
            ch=chr(num)
            num+=1
            print("{}".format(ch),end=' ')
        print('')

    def errorreport(self):
        print("Deadlock detected!!!")
        time.sleep(1)
        print("Deplpoy deadlock removal algorithm ?" , end=' ')
        ch = input()
        if ch.upper() == 'Y':
            self.deadlock_removal()
        else:
            exit(1)

    def noerror(self):
        print("No Deadlock Detected")
        print("The safe sequence is :")
        for i in range(self.n):
            print(self.process[self.ss[i]])

    def deadlock_trial(self,subset=None):
        trial_process = self.process.copy()
        avail = self.avail.copy()
        append_this=[]
        d_solutions_ss=[]
        d_solutions_remove=[]
        self.ss =[]
        command = True
        avail = self.avail.copy()
        e=0
        last=-1
        f=0
        finish=[]
        final_value=sum(self.priority)
        trial_n = self.n
        ggg=0
        for i in trial_process:
            if i in subset:
                trial_process[ggg]=-1
                trial_n-=1
                final_value-=self.priority[ggg]
                d_solutions_remove.append(self.process[ggg])
            ggg+=1
        for ex in range(self.n):
            finish.append(0)
        while command:
            for i in range(self.n):
                if trial_process[i] != -1:
                    if last==i:
                        return False
                    if f==0:
                        last=i
                        f=1
                    flag=True
                    for j in range(self.r):  #check if request < resource
                        if avail[j] < self.need[i][j] :
                            flag = False
                    if flag==True and finish[i]==0:
                        d_solutions_ss.append(i)
                        for _ in range(self.r):
                            avail[_]=avail[_]+self.reso[i][_]
                        last=i
                        finish[i]=1
            if len(d_solutions_ss)==trial_n:
                command=False
        if final_value >= self.previous_max:
            append_this.append(final_value)
            append_this.append(d_solutions_ss)
            append_this.append(d_solutions_remove)
            self.d_solutions.append(append_this)
            self.previous_max=final_value
        return True

    def deadlock_removal(self):
        print("Enter priority for each process: ")
        for i in range(self.n):
            print("{}".format(self.process[i]),end=' ')
            self.priority.append(int(input()))

        for L in range(1, len(self.process)):
            for test_set in itertools.combinations(self.process, L):
                if self.deadlock_trial(test_set):
                    time.sleep(1)
                    print(".",end="")
        print("\n")
        self.d_solutions.sort()
        max_value=self.d_solutions[-1][0]
        print("The maximum value of possible weight is :",end=' ')
        print(max_value)
        print("The possible solutons to achive this are : ")
        print_count=1
        for gg in self.d_solutions :
            if gg[0] == max_value:
                print("Solution Number : {}".format(print_count))
                print_count+=1
                print("The Safe Sequence is : ")
                for xd in gg[1]:
                    print(self.process[xd])
                print("The Process removed are : ")
                for xd in gg[2]:
                    print(xd)
        exit(1)

    def dda(self):
        command = True
        avail = self.avail.copy()
        e=0
        last=-1
        f=0
        finish=[]
        for ex in range(self.n):
            finish.append(0)
        while command:
            for i in range(self.n):
                if last==i:
                    self.errorreport()
                if f==0:
                    last=0
                    f=1
                flag=True
                for j in range(self.r):  #check if request < resource
                    if avail[j] < self.need[i][j] :
                        flag = False
                if flag==True and finish[i]==0:
                    self.ss.append(i)
                    for _ in range(self.r):
                        avail[_]=avail[_]+self.reso[i][_]
                    last=i
                    finish[i]=1
                    time.sleep(1)
                    print("{} executed.........".format(self.process[i]))
                elif finish[i]==0:
                    time.sleep(1)
                    print("{} waiting.......".format(self.process[i]))
            if len(self.ss)==self.n:
                command=False
        self.noerror()

    def main(self):
        print("Welcome to DDA")
        print("Enter number of processes: ",end=" ")
        self.n = int(input())
        print("Enter process names: ",end=" ")
        for i in range(self.n):
            self.process.append(input())
        print("Enter number of resources: ",end=' ')
        self.r = int(input())
        print("Enter resource allocation for each process as follows :")
        self.printchar(self.r)
        for _ in range(self.n):
            self.reso.append(list(map(int,input().split())))
        print("Enter resource need for each process as follows: ")
        self.printchar(self.r)
        for _ in range(self.n):
            self.need.append(list(map(int,input().split())))
        print("Enter total instances resources available: ")
        self.printchar(self.r)
        self.avail=list(map(int,input().split()))
        print("Deploy Deadlock Detection Algorithm ?? (Y/N) :",end=' ')
        choice = input()
        if choice.upper() == "Y":
            self.dda()
        else:
            print("Aborting.....")
            exit(1)

myqu=deadlock()
myqu.main()

