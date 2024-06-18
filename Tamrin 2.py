import numpy as np
from collections import Counter

student_id = 400121045  
np.random.seed(student_id)

vector = np.random.randint(0, 21, size=10000)

count = Counter(vector)

for number in range(21):
    print(f"Number {number}: {count[number]}")
