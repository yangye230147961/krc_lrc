import zlib,re,os
def decode_krc(krc_name):
	a = open(krc_name, "rb").read()
	encrypt_key = (64, 71, 97, 119, 94, 50, 116, 71, 81, 54, 49, 45, 206, 210, 110, 105)
	content = a[4:]  # 前四个字节是magic number，表示版本号等
	compress_content = bytes(content[i] ^ encrypt_key[i % len(encrypt_key)] for i in range(len(content)))
	text_bytes = zlib.decompress(bytes(compress_content))
	text = text_bytes.decode("utf8")
	text=re.sub("\<\w+,\w+,\w+\>","",text)#去除单字时间
	numlist=re.findall("\[\w+,\w+\]",text)
	for i in numlist:
	#	print(i)
		num=re.findall("\d+",i)
		num=int(num[0])/1000
		times='[%02d:%05.2f]'%(num//60,num%60)
		if i in text:
			text=text.replace(i,times)
	return text
if __name__=="__main__":
	music_dir="/sdcard/kgmusic/download/"
	krc_dir="/sdcard/kugou/lyrics/"
	
	music_list=os.listdir(music_dir)
	krc_list=os.listdir(krc_dir)
	for i in range(0,len(music_list)):
		if ".mp3" not in music_list[i]:
			music_list[i]=False
	for j in krc_list:
		for s in music_list:
			if s:
				if s[:-4] in j:
					dc_krc=decode_krc("{}{}".format(krc_dir,j))
					with open("{}{}.lrc".format(music_dir,s[:-4]),"a") as f:
						f.write(dc_krc)
						print("{}转换完成".format(s))
						f.close
