import pandas as pd

df = pd.read_excel("Online Retail.xlsx")

print("Original Shape:", df.shape)

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# CustomerID missing rows remove
df = df.dropna(subset=['CustomerID'])

# Negative quantity remove
df = df[df['Quantity'] > 0]

# Negative price remove
df = df[df['UnitPrice'] > 0]

print("\nCleaned Shape:", df.shape)
# Total Amount column
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Latest purchase date
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# RFM Table
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM Table:")
print(rfm.head())

print("\nRFM Shape:")
print(rfm.shape)
from sklearn.preprocessing import StandardScaler

# Scaling
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

print("Scaled Data Shape:", rfm_scaled.shape)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )
    
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()
# Final KMeans
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

print(rfm['Cluster'].value_counts())
print(rfm.head())
cluster_summary = rfm.groupby('Cluster').mean()

print("\nCluster Summary:")
print(cluster_summary)
# Data Loading
import pandas as pd

# Data Cleaning
...

# RFM Analysis
...

# Scaling
...

# Elbow Method
...

# Final Clustering
...

# Cluster Summary
...

# Visualization  <-- YAHAN paste karna hai
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=rfm,
    x='Frequency',
    y='Monetary',
    hue='Cluster',
    palette='Set1'
)

plt.title("Customer Segments")
plt.show()
print("\nCustomers in each Cluster:")
print(rfm['Cluster'].value_counts())

print("\nCluster Summary:")
print(rfm.groupby('Cluster').mean())
rfm.to_csv("customer_segments.csv")
print("File saved successfully")