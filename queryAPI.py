
from get_stations import *

data=[]
type_data=[]
def query(from_station,to_station,date):
    data.clear()
    stations = eval(read())
    from_station=stations[from_station]
    to_station=stations[to_station]
    hds = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
            'Cookie': 'jc_save_fromDate={};_jc_save_fromStation={};_jc_save_toDate={};_jc_save_toStation={};_jc_save_wfdc_flag=dc;BIGipServerotn=434635018.50210.0000;BIGipServerpassport=921174282.50215.0000;RAIL_DEVICEID=qQI5vmuVzc7JxyJAdE5xhTOvqS-IdeB9cxXfx_Ir_sYhi8BlnQmxV1ZTPqhQg2en-JAyB5EhfVwDKUueyh07w_wi8m-GECiI-VhGVnPS_kKn76aNwvSuq121AnClHX7nACcVUTK39CXy6kxQSpRb8j6tGM5W7i19;RAIL_EXPIRATION=1593516578886;route=6f50b51faa11b987e576cdb301e545c4;JSESSIONID=3852314D3D765B0F35EC556CFEC958B6'.format(date,from_station,date,to_station)

        }

    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)

    res=requests.get(url,headers=hds)
    res.encoding='utf_8'
    result=res.json()
    result=result['data']['result']
    if isStations() == True:
            # 读取所有车站并转换为dic类型，eval()获取字符串值
            stations = eval(read())
            if len(result) != 0:  # 判断返回数据是否为空
                for i in result:
                    # 分割数据并添加到列表中
                    tmp_list = i.split('|')
                    # 因为查询结果中出发站和到达站为站名的缩写字母，所以需要在车站库中找到对应的车站名称
                    from_station = list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                    to_station = list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                    # 创建座位数组，由于返回的座位数据中含有空既“”，所以将空改成--这样好识别
                    seat = [tmp_list[3], from_station, to_station, tmp_list[8], tmp_list[9], tmp_list[10]
                        , tmp_list[32], tmp_list[31], tmp_list[30], tmp_list[21]
                        , tmp_list[23], tmp_list[33], tmp_list[28], tmp_list[24], tmp_list[29], tmp_list[26]]
                    newSeat = []
                    # 循环将座位信息中的空改成--
                    for s in seat:
                        if s == "":
                            s = "--"
                        else:
                            s = s
                        newSeat.append(s)  # 保存新的座位信息
                    data.append(newSeat)
    print(data)
    return data

# 获取高铁信息的方法
def g_vehicle():
    if len(data) != 0:
        for g in data:  # 循环所有火车数据
            i = g[0].startswith('G')  # 判断车次首字母是不是高铁
            if i:  # 如果是将该条信息添加到高铁数据中
                type_data.append(g)


# 移除高铁信息的方法
def r_g_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for g in data:
            i = g[0].startswith('G')
            if i:  # 移除高铁信息
                type_data.remove(g)


# 获取动车信息的方法
def d_vehicle():
    if len(data) != 0:
        for d in data:  # 循环所有火车数据
            i = d[0].startswith('D')  # 判断车次首字母是不是动车
            if i == True:  # 如果是将该条信息添加到动车数据中
                type_data.append(d)


# 移除动车信息的方法
def r_d_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for d in data:
            i = d[0].startswith('D')
            if i == True:  # 移除动车信息
                type_data.remove(d)


# 获取直达车信息的方法
def z_vehicle():
    if len(data) != 0:
        for z in data:  # 循环所有火车数据
            i = z[0].startswith('Z')  # 判断车次首字母是不是直达
            if i == True:  # 如果是将该条信息添加到直达数据中
                type_data.append(z)


# 移除直达车信息的方法
def r_z_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for z in data:
            i = z[0].startswith('Z')
            if i == True:  # 移除直达车信息
                type_data.remove(z)


# 获取特快车信息的方法
def t_vehicle():
    if len(data) != 0:
        for t in data:  # 循环所有火车数据
            i = t[0].startswith('T')  # 判断车次首字母是不是特快
            if i == True:  # 如果是将该条信息添加到特快车数据中
                type_data.append(t)


# 移除特快车信息的方法
def r_t_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for t in data:
            i = t[0].startswith('T')
            if i == True:  # 移除特快车信息
                type_data.remove(t)


# 获取快速车数据的方法
def k_vehicle():
    if len(data) != 0:
        for k in data:  # 循环所有火车数据
            i = k[0].startswith('K')  # 判断车次首字母是不是快车
            if i == True:  # 如果是将该条信息添加到快车数据中
                type_data.append(k)


# 移除快速车数据的方法
def r_k_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for k in data:
            i = k[0].startswith('K')
            if i == True:  # 移除快车信息
                type_data.remove(k)

