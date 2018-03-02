import pickle
import sys

final="final_rec2.txt"
final_ptr=open(final,"w+")
# rec_dict_file="recommend_user_dict_file.pickle"
pickle_out=open("recommend_user_dict_file.pickle","wb")

def mul(a,b):
	sum=0
	for i in range(0,9):
		sum+=a[i]*b[i]
	return sum

def add_rat(songs,rat,song):#song_dictionary,rating,actual_song
	try:
		songs[rat].append(song)
	except KeyError:
		songs[rat]=[song]

def add_to_dict(name,user_id,song_id):
	try:
		name[user_id].append(song_id)
	except KeyError:
		name[user_id]=[song_id]

user_p_obj=open("user_pref_dict.pickle","rb")
song_p_obj=open("song_feat_dict.pickle","rb")
song_already_listended=open("listenend_songs.pickle","rb")


user_dict=pickle.load(user_p_obj)
#user_dict={'00007a02388c208ea7176479f6ae06f8224355b3':[-0.1259174727442511, 1.3540312592529626, -0.3311910158157287, 1.5262656835868615, -1.694573281505963, 1.8215974936965151, 0.9416931595285054, 1.4629223826171143, -1.7167428937320695, 0.5473116969198101]}
song_dict=pickle.load(song_p_obj)
already=pickle.load(song_already_listended)

# count=0
number_of_users_recommended=0
# previous_user=""
# temp_count=1504368
# count=0
already_recommended=11730
songs={}
recommended_dict={}
for user_key in user_dict:
	if(already_recommended>0):
		print("Already recommended:",user_key)
		already_recommended-=1
		continue
	for song_key in song_dict:
		rat=mul(user_dict[user_key],song_dict[song_key])
		add_rat(songs,rat,song_key)
		#print(rat)

	all_ratings=songs.keys()
	all_ratings_sorted=sorted(all_ratings)
	# all_ratings.sort()#sorted keys in all_ratings!
	count=0
	all_ratings_sorted.reverse()
	final_ptr.write("{}\n".format(user_key))
	for key in all_ratings_sorted:
		for i in songs[key]:
			if(i in already[user_key]):
				print("%s already listenend" % (i))
				continue
			#print("%d:%s" % (key,i))
			add_to_dict(recommended_dict,user_key,i)
			final_ptr.write("{}\n".format(i))
			count+=1
			if(count==500):
				break
		if(count==500):
			break
	songs={}
	number_of_users_recommended+=1
	sys.stdout.write("Finished for %d users  \r" % (number_of_users_recommended) )

pickle.dump(recommended_dict,pickle_out)
pickle_out.close()


# 	sys.stdout.write("%d%%   \r" % (a) )
# 	sys.stdout.flush()
#11730 users sucessfully recommended!