time=0
q=10
s=2
class traffic_light:

	def __init__(self,color,timer):

		self.color=color
		self.timer=timer


class lane:

	def __init__(self,incoming,outgoing):

		self.incoming=incoming
		self.outgoing=outgoing

	def set_traffic_light(self,color,timer):

		tl=traffic_light(color,timer)

def schedule(l):
	q=10
	s=2
	t=0
	li=[x.incoming for x in l]	#incoming
	lo=[x.outgoing for x in l]	#outgoing

	q1=[x.incoming for x in l]
	q2=[]
	print(q1)
	print(q2)

	while(len(q1)>0 or len(q2)>0):
		print("Queue 1 ",q1)
		print("Queue 2 ",q2)
		while(len(q1)>0):

			mini=max(q1)
			minipos=q1.index(mini)
			print("Lane ",minipos+1," is selected from Queue 1")
			q1[minipos]-=(q*s)

			if(q1[minipos]==0):
				t+=q
				q1.pop(minipos)
			elif(q1[minipos]<0):
				t+=q1[minipos]
				q1.pop(minipos)
			else:
				q2.append(q1[minipos])
				q1.pop(minipos)
				t+=q
		q*=2
		while(len(q2)>0):
			mini=max(q2)
			minipos=q2.index(mini)

			q2[minipos]-=(q*s)
			print("Lane ",minipos+1," is selected from Queue 2")
			if(q2[minipos]==0):
				t+=q
				q2.pop(minipos)

			elif(q2[minipos]<0):
				t+=q2[minipos]
				q2.pop(minipos)
			else:
				q1.append(q2[minipos])
				q2.pop(minipos)
				t+=q	

		q*=2


	'''uni=[0,0,0,0]
	li_max=-1
	max_pos=-1
	k=0
	while():
		for i in range(1,5):

			print("Incoming Count of lane ",i," is ",li[i])
			if(li[i]>li_max):
				li_max=li[i]
				max_pos=i

		li[max_pos]-=(q/s)
		if(li[max_pos]<=0):
			uni[max_pos]=-1
		else:
			uni[max_pos]+=1

	'''


#take from 4 csv files
l1=lane(3,0)
l2=lane(5,0)
l3=lane(6,0)
l4=lane(7,0)
l=[l1,l2,l3,l4]
print(l)
q=10
schedule(l)



