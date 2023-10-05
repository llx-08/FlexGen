import pandas  as pd
from pandas import DataFrame


with open('debug_13b_1x4_1_12.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

    writer = pd.ExcelWriter('13b_1_12.xlsx')

    # 整理每个rank的数据
    for rank in [0, 1, 2, 3]:
        mask_time = []
        send_time = []
        load_weight_time = []
        load_time = []  # cache & hidden
        compute_time = []
        store_time = []

        for i in range(len(data)):
            if data[i][:7] == "rank #" + str(rank):
                if "mask time" in data[i]:
                    mask_time.append(float(data[i].removeprefix("rank #"+str(rank)+": mask time:  ")))
                elif "send time" in data[i]:
                    send_time.append(float(data[i].removeprefix("rank #"+str(rank)+": send time:  ")))
                elif "load weight time" in data[i]:
                    load_weight_time.append(float(data[i].removeprefix("rank #"+str(rank)+": load weight time:  ")))
                elif "load time" in data[i]:
                    load_time.append(float(data[i].removeprefix("rank #"+str(rank)+": load time:  ")))
                elif "compute time" in data[i]:
                    compute_time.append(float(data[i].removeprefix("rank #"+str(rank)+": compute time:  ")))
                elif "store time" in data[i]:
                    store_time.append(float(data[i].removeprefix("rank #"+str(rank)+": store time:  ")))
                else:
                    continue
        df = pd.concat([
            DataFrame({"mask time": mask_time}),
            DataFrame({"send time": send_time}),
            DataFrame({"load weight time": load_weight_time}),
            DataFrame({"load time": load_time}),
            DataFrame({"compute time": compute_time}),
            DataFrame({"store time": store_time})
        ], axis=1)
        df.fillna(0)
        df.to_excel(writer, sheet_name=str(rank))
        print(str(rank)+" finished")

    writer._save()
    writer.close()

f.close()

