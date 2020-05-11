count = 10000

with open("/home/anandita/darknet/data/train_new.txt" , 'w') as f:

	while(count <= 10228):
		f.write("/home/anandita/MEGAsync Downloads/FLIR/FLIR_ADAS/validation/PreviewData/FLIR_" + str(count) + ".jpeg" +'\n')
		count +=1

