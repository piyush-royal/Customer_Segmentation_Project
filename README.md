 📌 Project Overview

Customer segmentation is a crucial business strategy that helps organizations understand customer behavior and design targeted marketing campaigns.

In this project, customer transaction data from an online retail store was analyzed using **RFM (Recency, Frequency, Monetary) Analysis** and **K-Means Clustering** to identify distinct customer groups based on purchasing behavior.

The objective was to classify customers into meaningful segments such as VIP, Loyal, Regular, and At-Risk customers, enabling businesses to make data-driven decisions for customer retention and revenue growth.


🎯 Business Problem

Businesses often struggle to understand:

- Which customers generate the highest revenue?
- Which customers are likely to stop purchasing?
- Which customers should receive promotional offers?
- How can marketing campaigns be personalized?

Customer segmentation addresses these challenges by grouping customers with similar purchasing patterns.



📊 Dataset Information

**Dataset:** Online Retail Dataset

The dataset contains transactional records of an online retail company.

Features

| Feature | Description |
|----------|-------------|
| InvoiceNo | Invoice Number |
| StockCode | Product Code |
| Description | Product Description |
| Quantity | Quantity Purchased |
| InvoiceDate | Transaction Date |
| UnitPrice | Price Per Unit |
| CustomerID | Unique Customer Identifier |
| Country | Customer Country |

Dataset Size

- Total Records: **541,909**
- Total Features: **8**



🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- VS Code



🔄 Project Workflow

1. Data Collection

Imported the Online Retail dataset into Python for analysis.

2. Data Cleaning

Performed the following preprocessing steps:

- Removed missing Customer IDs
- Removed invalid transactions
- Removed negative quantities
- Removed negative unit prices
- Handled inconsistent records

3. Feature Engineering

Created a new feature:

```python
TotalAmount = Quantity * UnitPrice
```

This metric represents the total value of each transaction.

4. RFM Analysis

Calculated customer-level metrics:

 Recency (R)
Number of days since the customer's last purchase.

 Frequency (F)
Number of unique purchases made by the customer.

 Monetary (M)
Total amount spent by the customer.

 5. Data Standardization

Applied StandardScaler to normalize the RFM features.

 6. K-Means Clustering

Used the Elbow Method to determine the optimal number of clusters and performed customer segmentation using K-Means.

 7. Data Visualization

Generated visualizations including:

- Elbow Method Graph
- Customer Segmentation Scatter Plot
- Cluster Summary Analysis



📈 Results

The clustering model identified four distinct customer segments.

  Cluster 2 — VIP Customers

Characteristics:

- Highest spending customers
- Highest purchase frequency
- Most valuable customer group

Business Action:

- Premium memberships
- Exclusive offers
- Loyalty rewards



 Cluster 3 — Loyal Customers

Characteristics:

- Frequent purchases
- Strong engagement
- Consistent revenue contributors

Business Action:

- Personalized recommendations
- Membership programs
- Cross-selling opportunities



 Cluster 0 — Regular Customers

Characteristics:

- Average spending behavior
- Moderate purchase frequency

Business Action:

- Promotional campaigns
- Product recommendations



 Cluster 1 — At-Risk Customers

Characteristics:

- Long time since last purchase
- Low spending activity
- Low engagement

Business Action:

- Re-engagement campaigns
- Discount offers
- Retention strategies



📊 Key Insights

- A small percentage of customers generate a significant portion of revenue.
- VIP customers require retention-focused strategies.
- At-risk customers can be targeted using personalized marketing campaigns.
- Customer segmentation improves business decision-making and marketing efficiency.



 Project Screenshots

 Elbow Method
 Customer Segmentation
 Cluster Summary

 Project Structure

```text
Customer-Segmentation/
│
├── Online Retail.xlsx
├── customer_segmentation.py
├── README.md
│
└── screenshots/
    ├── elbow_method.png
    ├── customer_segments.png
    └── cluster_summary.png
```

▶️ How to Run

Clone Repository

```bash
git clone https://github.com/your-username/customer-segmentation-project.git
```

Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

Run Project

```bash
python customer_segmentation.py
```


Future Enhancements

- Streamlit Dashboard Integration
- Interactive Customer Analytics
- Customer Lifetime Value (CLV) Analysis
- Advanced Clustering Techniques
  - Hierarchical Clustering
  - DBSCAN
  - Gaussian Mixture Models



Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- RFM Analysis
- Customer Analytics
- Machine Learning
- K-Means Clustering
- Data Visualization
- Business Intelligence



 Author

**Piyush Royal**

Customer Segmentation Project using Machine Learning and Customer Analytics.
