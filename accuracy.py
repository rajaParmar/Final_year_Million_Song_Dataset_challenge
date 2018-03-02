from collections import defaultdict
import sys
import pickle

with open("hidden_dict.pickle","rb") as file:
	hidden_dict=pickle.load(file)

rec_dict=defaultdict(list)
count=0
uid=""
with open("final_rec.txt") as file:
	for line in file:
		if len(line)>20 :
			uid=line[:-1]
		else:
			rec_dict[uid].append(line[:-1])

accuracy_dict={}
# l=hidden_dict["3c346fa4de367db3b91d7d9f215b85f760dc03d3"]
# rec_dict["3c346fa4de367db3b91d7d9f215b85f760dc03d3"]+=hidden_dict["3c346fa4de367db3b91d7d9f215b85f760dc03d3"]
for key in rec_dict.keys():
	accuracy_dict[key]=(len(set(hidden_dict[key]).intersection(rec_dict[key]))/len(hidden_dict[key]))*100
	count=count+1
	sys.stdout.write("\rUsers done : "+str(count)+" out of "+str(len(rec_dict)))

print("\n")
with open("accuracy_dict.pickle","wb") as file:
	pickle.dump(accuracy_dict,file)
final_accuracy=sum(accuracy_dict.values())/len(accuracy_dict)
print("Final Accuracy : "+str(final_accuracy))