#Daily-Coding_problem-#53
#Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
#data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


class queue:

	def __init__(self):

		self.s1 = list()  	#main stack	
		self.s2 = list()	#auxiliary stack

	def __repr__(self):

		return str(self.s1)

	def enqueue(self,value):

		self.s1.append(value)  	#insert the value in main stack

	def dequeue(self):

		if not self.s1:		#if queue is empty return 
			return None
		

		while self.s1:         
			self.s2.append(self.s1.pop())  #push every value from s1 to s2. if s1=[1,2,3] then s2 becomes [3,2,1]

		self.s2.pop() #pop the last element os s2

		while self.s2:
			self.s1.append(self.s2.pop())  #push every remaining value in s1. is s2=[3,2] then s1 becomes [2,3]

q = queue()
q.enqueue(1)
assert q.s1== [1]

q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

assert q.s1 == [1,2,3,4]

q.dequeue()
q.enqueue(6)

assert q.s1 == [2,3,4,6]

