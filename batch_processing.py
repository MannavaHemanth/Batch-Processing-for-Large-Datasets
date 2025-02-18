#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import time

# Load the large CSV file normally (all at once)
start_time = time.time()

# Perform some operations after loading
large_data_normal = pd.read_csv('C:/Users/heman/Downloads/large_sample_data.csv')  # Replace with actual path
processed_data_normal = large_data_normal.dropna()  # Example operation (drop missing values)

end_time = time.time()
print(f"Time taken to load and process normally: {end_time - start_time:.2f} seconds")


# Now batch processing
start_time = time.time()

# Batch processing with chunked reads
chunk_size = 500000
chunks = pd.read_csv('C:/Users/heman/Downloads/large_sample_data.csv', chunksize=chunk_size)

# Process chunks one by one
processed_data_chunks = []
for chunk in chunks:
    processed_data_chunks.append(chunk.dropna())  # Example operation (drop missing values)

# Concatenate processed chunks
batch_processed_data = pd.concat(processed_data_chunks)

end_time = time.time()
print(f"Time taken to load and process with batch processing: {end_time - start_time:.2f} seconds")


# In[ ]:




