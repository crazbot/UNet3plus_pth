from tqdm import tqdm
import time

for i in tqdm(range(300)):
    for j in tqdm(range(200)):
        time.sleep(0.1)
