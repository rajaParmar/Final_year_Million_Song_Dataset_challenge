import pickle
import sys

file_path="db_110k.txt"
tuple_count=1450933

ptr=open(file_path,"r")
pickle_file_path="listenend_songs.pickle"

user_dict={}


def entry_to_list(line):
	triplet_list=[]
	triplet_list=line.split('\t')
	return triplet_list

count=0
while(tuple_count>0):
	tuple=entry_to_list(ptr.readline())
	try:
		user_dict[tuple[0]].append(tuple[1])
	except KeyError:
		user_dict[tuple[0]]=[tuple[1]]
	tuple_count-=1
	count+=1
	sys.stdout.write("%d   \r" % (count) )

pickle_out=open(pickle_file_path,"wb")
pickle.dump(user_dict,pickle_out)
pickle_out.close()



