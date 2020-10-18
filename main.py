import os;
import threading;

def inputInfo():
    bv = input("输入视频av或BV号:")
    print("默认保存路径为d:\\bilibili\\{你输入的BV号}")
    ji = input("保存的p数(也可以是线程数):")
    print("启动p个线程能同时获取p级，但p级过多会引起卡顿或OOM")
    return ji,bv
def down(p,bv):
    Dir= "d:\\bilibili\\" + bv
    if os.path.exists(Dir) == False:
        os.makedirs(Dir)
    Url = r"https://www.bilibili.com/video/" + bv + "?p={}"
    os.system(r"you-get --no-proxy --format=dash-flv " + Url.format(p)+" -o " +Dir)
def download(info):
    threads=[]
    for i in range(int(info[0])):
        th = threading.Thread(target=down,args=(i+1,info[1],))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()

if __name__ == '__main__':
    info = inputInfo()
    download(info)