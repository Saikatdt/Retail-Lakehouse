# Retail-Lakehouse

This is a simple project to explore basic business scenarios but with real-time industry depth.
We will explore the use case for retail analytics.


## Getting started

### Business Usecase

We have a retail e-commerce business where customers order products from the website.
The products are then shipped to the customers' addresses. A shipment is tracked through different statuses ( shipped, delivered, cancelled). Once delivered, the customers share their feedback on the website on the product.

One order can have multiple products in them. 

### Details

- **Quick Reference**: More details about the business and the dataset can be found [here](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?datasetId=55151&searchQuery=data+engineer)


### Business Goals
- Increase in the market penetration in the geolocation where the demand is less.
- Increase the number of orders per customer by understanding how much each customer spends.
- Enhance Customer Satisfaction and Product Understanding through Reviews Analysis
- Optimize Product Sales Strategy and Seasonal Offerings


### KPI
focused on Sales & Quantity, dashboard can be enabled to have these metrics filtered on geolocation, market, date range etc.

- Sales & Quantity by Store or Seller
- Sales & Quantity by Product & Product Category
- Purchase frequency(from 55 Ecommerce KPIs and Metrics You Need to Track and Measure)
- Time between purchases(from 55 Ecommerce KPIs and Metrics You Need to Track and Measure )
- Customer rating
- Product sales
- Seller sales
- Delivery time
1. Analyze sales data to identify the products that exhibit significant seasonal purchasing patterns. Determine which products have the highest sales during different seasons.
2. Calculate the average sales and ratings for each product category. Identify the categories with the highest and lowest sales and ratings.
3. Determine the frequency of product combinations purchased together. Identify popular product bundles to optimize cross-selling strategies.
4. Calculate the average sentiment score of customer reviews i.e. Customer Sentiment Score (CSS) using natural language processing (NLP) techniques. 
2. Measure the percentage of customers who have written reviews compared to the total number of customers who made purchases i.e.  Review Participation Rate (RPR). This provides insights into customer engagement and willingness to share feedback.
3. Analyze reviews to identify the most frequently mentioned product features and their sentiment scores. This helps in understanding what aspects of the product are most important to customers.
4. Quantify the number of reviews mentioning specific pain points or issues customers are facing with products. This helps prioritize improvements.
5. Track the total number of reviews and the average ratings per product to assess popularity and customer satisfaction trends.

focused on Customer Feedback and Ratings, Reviews, dashboard can be enabled to have these metrics filtered on geolocation, market, date range, product type etc.

- average customer rating
- feedback %
- #order with feedback or reviews

focused on business operations to optimise e-commerce delivery

- delivery turnaround = no of days between order_delivered_customer_date and order_estimated_delivery_date


## Tasks Involved
- **Data Ingestion**: 

