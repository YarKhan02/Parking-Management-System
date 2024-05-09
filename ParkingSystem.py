from threading import Thread, Lock, Condition
from threading import BoundedSemaphore, Thread
from collections import defaultdict
from time import sleep
import random


class CustomBoundedSemaphore(BoundedSemaphore):
    def __init__(self, value=1):
        super().__init__(value)
        self.max_value = value

    def is_full(self):
        return self._value == 0


class Car:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0


lock = Lock()
semaphore_slots = CustomBoundedSemaphore(value = 4)

lock_holder = None


class Gate:
    def __init__(self):
        pass

    def priority_process(self, car):
        sleep(car.arrival_time)
        global lock_holder
        if lock.locked():
            print(f'\ncar {car.pid} is waiting...')
            print(f'lock is acquire by {lock_holder}\n')

        if semaphore_slots.is_full():
            print(f'\nCar {car.pid} waiting for a parking slot')
        
        semaphore_slots.acquire()

        print(f'\nCar {car.pid} reserved a parking slot')

        lock.acquire()
        
        lock_holder = car.pid
        
        print(f'car {lock_holder} is in process\n')
        
        sleep(car.burst_time)
        
        print(f'car {lock_holder} releases lock\n')
        
        semaphore_slots.release()
        lock.release()



def priority_scheduling(priority_queues):
    next = None
    
    # print()
    # for k in priority_queues:
    #     for c in priority_queues[k]:
            # print(c.priority, c.arrival_time, end = ' -- ')
    #     print()
    # print()

    h = -1
    a = 99
    s = -1
        
    for p in priority_queues:
        x = 0
        for c in priority_queues[p]:
            if (c.arrival_time < a):
                a = c.arrival_time
                h = c.priority
                next = c
                s = x
                # print(a, h, s, end = '\n')
            x += 1

    # print('\npop: ', s, h, end = '\n')
    priority_queues[h].pop(s)

    return next



class ParkingSystem:
    def __init__(self):
        self.priority_queues = defaultdict(list)
        self.priorities = [2, 3, 1]
        self.gates = []
        self.threads = []

    def initialized_gates(self):
        for j in range(3):
            gate = Gate()
            self.gates.append(gate) 

    def entry(self):
        gate = random.randint(0, 2)

        car_id = random.randint(100, 1000)
        priority = random.choice(self.priorities)
        burst_time = random.randint(1, 10)
        arrival_time = random.randint(0, 10)

        
        car = Car(car_id, arrival_time, burst_time, priority)
        
        self.priority_queues[priority].append(car)

        current = priority_scheduling(self.priority_queues)

        print(f'Car {car_id} is at gate {gate} - arrival time {arrival_time} - burst time {burst_time} - priority {priority}\n')
            
        t = Thread(target = self.gates[gate].priority_process, args = (current,))
        self.threads.append(t)
            
        t.start()

        car_id += 1

    def system(self):
        self.initialized_gates()

        i = 0
        while (i < 15):
            sleep(2)
            self.entry()
            i += 1

        # self.entry()


def main():
    ps = ParkingSystem()
    ps.system()


if __name__ == "__main__":
    main()