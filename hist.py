import matplotlib.pyplot as plt
import numpy as np

# Number of workers
x = ["1", "2", "4", "8"]

# Average Req/Sec of three runs for each number of workers
y = [815.61, 648.54, 543.90, 548.91]

plt.title("Performance of service per number of nodes (n=3)")
plt.xlabel("Number of nodes")
plt.ylabel("Average Req/Sec")
plt.bar(x, y)
plt.show()